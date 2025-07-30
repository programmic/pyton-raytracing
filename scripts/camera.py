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
    
    def render_frane(self, width, height, camera, spheres, max_bounces):
        img = np.zeros((height, width, 3), dtype=np.uint8)
        aspect = width / height
        fov = camera.fov
        cam_pos = camera.pos

        # Calculate forward, right, and up vectors from camera rotation
        yaw = np.deg2rad(camera.rot.y)
        pitch = np.deg2rad(camera.rot.x)
        roll = np.deg2rad(camera.rot.z)

        forward = Vec3(
            np.cos(pitch) * np.sin(yaw),
            np.sin(pitch),
            np.cos(pitch) * np.cos(yaw)
        ).normalize()

        right = Vec3(
            np.sin(yaw - np.pi/2),
            0,
            np.cos(yaw - np.pi/2)
        ).normalize()

        up = right.cross(forward).normalize()

        scale = np.tan(np.deg2rad(fov * 0.5))
        for y in range(height):
            for x in range(width):
                px = (2 * ((x + 0.5) / width) - 1) * aspect * scale
                py = (1 - 2 * ((y + 0.5) / height)) * scale
                direction = (forward + right * px + up * py).normalize()
                ray_origin = cam_pos
                ray_dir = direction
                color = np.array([0, 0, 0], dtype=np.float32)
                attenuation = 1.0

                for bounce in range(max_bounces):
                    hit = False
                    nearest_t = float('inf')
                    hit_sphere = None
                    hit_point = None
                    hit_normal = None

                    # Find nearest intersection
                    for sphere in spheres:
                        oc = ray_origin - sphere.center
                        a = ray_dir.dot(ray_dir)
                        b = 2.0 * oc.dot(ray_dir)
                        c = oc.dot(oc) - sphere.radius * sphere.radius
                        discriminant = b * b - 4 * a * c
                        if discriminant < 0:
                            continue
                        sqrt_disc = np.sqrt(discriminant)
                        t1 = (-b - sqrt_disc) / (2 * a)
                        t2 = (-b + sqrt_disc) / (2 * a)
                        t = None
                        if t1 > 1e-4 and t1 < nearest_t:
                            t = t1
                        elif t2 > 1e-4 and t2 < nearest_t:
                            t = t2
                        if t is not None:
                            nearest_t = t
                            hit = True
                            hit_sphere = sphere

                    if hit and hit_sphere is not None:
                        # Compute intersection point and normal
                        hit_point = ray_origin + ray_dir * nearest_t
                        hit_normal = (hit_point - hit_sphere.center).normalize()
                        # Add color (attenuated by bounces)
                        if hasattr(hit_sphere, "material") and hasattr(hit_sphere.material, "color"):
                            base_color = np.array(hit_sphere.material.color, dtype=np.float32)
                        else:
                            base_color = np.array((255, 255, 255), dtype=np.float32)
                        color += attenuation * base_color
                        # Prepare for next bounce (reflection)
                        ray_origin = hit_point + hit_normal * 1e-4  # Offset to avoid self-intersection
                        ray_dir = ray_dir - hit_normal * 2 * ray_dir.dot(hit_normal)
                        attenuation *= getattr(getattr(hit_sphere, "material", None), "specularity", 0.5)  # Default reflectivity
                    else:
                        break  # No hit, end bounces

                img[y, x] = np.clip(color, 0, 255).astype(np.uint8)
        return img
