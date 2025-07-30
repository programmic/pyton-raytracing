import unittest
from scripts.vec3 import Vec3
from scripts.sphere import Sphere
from scripts.material import Material
from scripts.camera import Camera
import numpy as np

class TestCamera(unittest.TestCase):
    def test_render_frane_runs(self):
        camera = Camera((10, 10), Vec3(0, 0, -3), Vec3(0, 0, 0), 60.0)
        spheres = [Sphere(Vec3(0, 0, 2), 0.5, Material((255, 0, 0), 0.5))]
        img = camera.render_frane(10, 10, camera, spheres, 1)
        self.assertIsInstance(img, np.ndarray)
        self.assertEqual(img.shape, (10, 10, 3))
        self.assertEqual(img.dtype, np.uint8)

if __name__ == "__main__":
    unittest.main()