import logging

class Vec3:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return isinstance(other, Vec3) and self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vec3(self.x + other, self.y + other, self.z + other)
        logging.info("Vec3.__add__: invalid operand type")
        return None

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):
            return Vec3(self.x - other, self.y - other, self.z - other)
        logging.info("Vec3.__sub__: invalid operand type")
        return None

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vec3(self.x * other, self.y * other, self.z * other)
        logging.info("Vec3.__mul__: invalid operand type")
        return None

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x / other, self.y / other, self.z / other)
        logging.info("Vec3.__truediv__: invalid operand type")
        return None
        
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __getitem__(self, key):
        if key == 0 or key == "x": return self.x
        elif key == 1 or key == "y": return self.y
        elif key == 2 or key == "z": return self.z
        logging.info("Vec3.__getitem__: invalid key")
        return None

    def __setitem__(self, key, value):
        if key == 0 or key == "x": self.x = value
        elif key == 1 or key == "y": self.y = value
        elif key == 2 or key == "z": self.z = value
        else:
            logging.info("Vec3.__setitem__: invalid key")
        return None

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        return f"vec3({self.x}, {self.y}, {self.z})"
    
    def magnitude(self):
        x, y, z = self.x, self.y, self.z
        return (x * x + y * y + z * z) ** 0.5
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vec3(0, 0, 0)
        return self / mag

