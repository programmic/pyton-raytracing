import unittest
from scripts.material import Material

class TestMaterial(unittest.TestCase):
    def test_init(self):
        m = Material((1, 2, 3), 0.5)
        self.assertEqual(m.color, (1, 2, 3))
        self.assertEqual(m.specularity, 0.5)

if __name__ == "__main__":
    unittest.main()