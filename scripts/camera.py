from vec3 import Vec3
from sphere import Sphere
from triangle import Triangle
from ray import Ray
import intersect
import numpy as np

class Camera:
    def __init__(
            self,
            resolution: tuple[int, int],
            pos: Vec3 = Vec3(0, 0, 0),
            rot: Vec3 = Vec3(0, 0, 0),
            fov: float = 60.0,
            near: float = 0.1,
            far: float = 100
            ):
        self.resolution = resolution
        self.pos = pos
        self.rot = rot
        self.fov = fov
        self.near = near
        self.far = far
    
    def render_frane(self, width, height, camera, spheres):
        img = np.zeros((height, width, 3), dtype=np.uint8)
        aspect = width / height
        fov = camera.fov
        cam_pos = camera.pos

        # Calculate forward, right, and up vectors from camera rotation
        yaw = np.deg2rad(camera.rot.y)
        pitch = np.deg2rad(camera.rot.x)
        roll = np.deg2rad(camera.rot.z)

        # Forward vector
        forward = Vec3(
            np.cos(pitch) * np.sin(yaw),
            np.sin(pitch),
            np.cos(pitch) * np.cos(yaw)
        ).normalize()

        # Right vector
        right = Vec3(
            np.sin(yaw - np.pi/2),
            0,
            np.cos(yaw - np.pi/2)
        ).normalize()

        # Up vector (using cross product)
        up = right.cross(forward).normalize()

        scale = np.tan(np.deg2rad(fov * 0.5))
        for y in range(height):
            for x in range(width):
                px = (2 * ((x + 0.5) / width) - 1) * aspect * scale
                py = (1 - 2 * ((y + 0.5) / height)) * scale
                direction = (forward + right * px + up * py).normalize()
                r = Ray(cam_pos, direction)
                color = np.array([0, 0, 0], dtype=np.uint8)
                for sphere in spheres:
                    if intersect.intersect_ray_sphere(r.origin, r.direction, sphere.center, sphere.radius):
                        color = np.array(sphere.color if sphere.color is not None else (255, 255, 255), dtype=np.uint8)
                        break
                img[y, x] = color
        return img
