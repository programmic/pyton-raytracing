from vec3 import Vec3
from triangle import Triangle
import math

def intersect_ray_ray(ray1, ray2, epsilon=1e-6) -> bool:
    cross = ray1.direction.cross(ray2.direction)
    cross_mag_sq = cross.dot(cross)
    diff = ray2.origin - ray1.origin

    if cross_mag_sq < epsilon:
        # Directions are parallel or anti-parallel
        # Check if origins are colinear
        if diff.cross(ray1.direction).magnitude() > epsilon:
            return False  # Not colinear
        # Check if the rays overlap (t >= 0 for both)
        t1 = 0
        t2 = 0
        if ray1.direction.dot(ray2.direction) > 0:
            # Same direction
            t2 = (ray1.origin - ray2.origin).dot(ray1.direction) / ray1.direction.dot(ray1.direction)
        else:
            # Opposite direction
            t2 = (ray1.origin - ray2.origin).dot(-ray1.direction) / ray1.direction.dot(ray1.direction)
        return t2 >= 0
    return False

def intersect_ray_sphere(ray_origin: Vec3, ray_dir: Vec3, sphere_center: Vec3, sphere_radius: float) -> bool:
    oc = ray_origin - sphere_center
    a = ray_dir.dot(ray_dir)
    b = 2.0 * oc.dot(ray_dir)
    c = oc.dot(oc) - sphere_radius * sphere_radius

    discriminant = b * b - 4 * a * c
    if discriminant < 0: return False
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        t1 = (-b - sqrt_discriminant) / (2 * a)
        t2 = (-b + sqrt_discriminant) / (2 * a)
        if t1 >= 0 or t2 >= 0: return True

def intersect_ray_triangle(ray_origin: Vec3, ray_dir: Vec3, tri: Triangle, epsilon=1e-6) -> bool:
    v0, v1, v2 = tri.v0, tri.v1, tri.v2
    edge1 = v1 - v0
    edge2 = v2 - v0
    h = ray_dir.cross(edge2)
    a = edge1.dot(h)
    if abs(a) < epsilon:
        return False
    f = 1.0 / a
    s = ray_origin - v0
    u = f * s.dot(h)
    if u < 0.0 or u > 1.0:
        return False
    q = s.cross(edge1)
    v = f * ray_dir.dot(q)
    if v < 0.0 or u + v > 1.0:
        return False
    t = f * edge2.dot(q)
    if t > epsilon:
        return True
    else:
        return