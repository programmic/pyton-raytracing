import unittest
from scripts.vec3 import Vec3

class TestVec3(unittest.TestCase):

    def setUp(self):
        self.v1 = Vec3(1, 2, 3)
        self.v2 = Vec3(4, 5, 6)
        self.scalar = 2

    def test_init_and_eq(self):
        v = Vec3(1, 2, 3)
        self.assertEqual(v, self.v1)
        self.assertNotEqual(v, self.v2)

    def test_add_vec3(self):
        result = self.v1 + self.v2
        expected = Vec3(5, 7, 9)
        self.assertEqual(result, expected)

    def test_add_scalar(self):
        result = self.v1 + self.scalar
        expected = Vec3(3, 4, 5)
        self.assertEqual(result, expected)

    def test_add_invalid(self):
        with self.assertLogs(level='INFO') as log:
            result = self.v1 + "invalid"
        self.assertIsNone(result)

    def test_sub_vec3(self):
        result = self.v2 - self.v1
        expected = Vec3(3, 3, 3)
        self.assertEqual(result, expected)

    def test_sub_scalar(self):
        result = self.v2 - self.scalar
        expected = Vec3(2, 3, 4)
        self.assertEqual(result, expected)

    def test_sub_invalid(self):
        with self.assertLogs(level='INFO') as log:
            result = self.v1 - [1, 2, 3]
        self.assertIsNone(result)

    def test_mul_vec3(self):
        result = self.v1 * self.v2
        expected = Vec3(4, 10, 18)
        self.assertEqual(result, expected)

    def test_mul_scalar(self):
        result = self.v1 * self.scalar
        expected = Vec3(2, 4, 6)
        self.assertEqual(result, expected)

    def test_mul_invalid(self):
        with self.assertLogs(level='INFO') as log:
            result = self.v1 * {"a":1}
        self.assertIsNone(result)

    def test_truediv_scalar(self):
        result = self.v2 / self.scalar
        expected = Vec3(2, 2.5, 3)
        self.assertEqual(result, expected)

    def test_truediv_invalid(self):
        with self.assertLogs(level='INFO') as log:
            result = self.v1 / self.v2
        self.assertIsNone(result)

    def test_getitem(self):
        self.assertEqual(self.v1[0], 1)
        self.assertEqual(self.v1[1], 2)
        self.assertEqual(self.v1[2], 3)
        self.assertEqual(self.v1["x"], 1)
        self.assertEqual(self.v1["y"], 2)
        self.assertEqual(self.v1["z"], 3)

    def test_getitem_invalid(self):
        with self.assertLogs(level='INFO') as log:
            result = self.v1[3]
        self.assertIsNone(result)

    def test_setitem(self):
        v = Vec3(0, 0, 0)
        v[0] = 10
        v[1] = 20
        v[2] = 30
        self.assertEqual(v.x, 10)
        self.assertEqual(v.y, 20)
        self.assertEqual(v.z, 30)
        v["x"] = 40
        v["y"] = 50
        v["z"] = 60
        self.assertEqual(v.x, 40)
        self.assertEqual(v.y, 50)
        self.assertEqual(v.z, 60)

    def test_setitem_invalid(self):
        v = Vec3(0, 0, 0)
        with self.assertLogs(level='INFO') as log:
            v[3] = 100
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.z, 0)

    def test_str_and_repr(self):
        self.assertEqual(str(self.v1), "(1, 2, 3)")
        self.assertEqual(repr(self.v1), "vec3(1, 2, 3)")

    def test_magnitude(self):
        self.assertAlmostEqual(self.v1.magnitude(), (1**2 + 2**2 + 3**2)**0.5)

    def test_dot(self):
        result = self.v1.dot(self.v2)
        expected = 1*4 + 2*5 + 3*6
        self.assertEqual(result, expected)

    def test_cross(self):
        result = self.v1.cross(self.v2)
        expected = Vec3(
            self.v1.y * self.v2.z - self.v1.z * self.v2.y,
            self.v1.z * self.v2.x - self.v1.x * self.v2.z,
            self.v1.x * self.v2.y - self.v1.y * self.v2.x
        )
        self.assertEqual(result, expected)

    def test_normalize(self):
        norm = self.v1.normalize()
        mag = self.v1.magnitude()
        expected = Vec3(self.v1.x / mag, self.v1.y / mag, self.v1.z / mag)
        self.assertAlmostEqual(norm.x, expected.x)
        self.assertAlmostEqual(norm.y, expected.y)
        self.assertAlmostEqual(norm.z, expected.z)

if __name__ == "__main__":
    unittest.main()
