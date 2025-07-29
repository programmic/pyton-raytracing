import unittest
from scripts.vec3 import Vec3
from scripts.ray import Ray
from scripts.triangle import Triangle
import scripts.intersect as intersect

class TestIntersect(unittest.TestCase):
    def test_ray_ray_intersect(self):
        r1 = Ray(Vec3(0, 0, 0), Vec3(1, 0, 0))
        r2 = Ray(Vec3(0, 1, 0), Vec3(0, -1, 0))
        self.assertFalse(intersect.intersect_ray_ray(r1, r2))
        # Intersecting rays (meet at x=1)
        r3 = Ray(Vec3(0, 0, 0), Vec3(1, 0, 0))
        r4 = Ray(Vec3(2, 0, 0), Vec3(-1, 0, 0))
        self.assertTrue(intersect.intersect_ray_ray(r3, r4))

    def test_ray_sphere_intersect(self):
        origin = Vec3(0, 0, 0)
        dir = Vec3(1, 0, 0)
        center = Vec3(5, 0, 0)
        radius = 1
        # Should intersect
        self.assertTrue(intersect.intersect_ray_sphere(origin, dir, center, radius))
        # Should not intersect
        center2 = Vec3(0, 5, 0)
        self.assertFalse(intersect.intersect_ray_sphere(origin, dir, center2, radius))

    def test_ray_triangle_intersect(self):
        tri = Triangle(Vec3(0, 0, 0), Vec3(1, 0, 0), Vec3(0, 1, 0))
        # Ray perpendicular to triangle, should intersect
        origin = Vec3(0.25, 0.25, -1)
        dir = Vec3(0, 0, 1)
        self.assertTrue(intersect.intersect_ray_triangle(origin, dir, tri))
        # Ray misses triangle
        origin2 = Vec3(2, 2, -1)
        self.assertFalse(intersect.intersect_ray_triangle(origin2, dir, tri))
        # Ray parallel to triangle
        dir2 = Vec3(1, 0, 0)
        self.assertFalse(intersect.intersect_ray_triangle(origin, dir2, tri))

if __name__ == "__main__":
    unittest.main()