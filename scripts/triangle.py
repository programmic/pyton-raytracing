from vec3 import Vec3

class Triangle:
    def __init__(self, v0: Vec3, v1: Vec3, v2: Vec3):
        if not all(isinstance(v, Vec3) for v in (v0, v1, v2)):
            raise TypeError("All vertices must be vec3 instances")
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

    def __eq__(self, other):
        return (
            isinstance(other, Triangle) and
            self.v0 == other.v0 and
            self.v1 == other.v1 and
            self.v2 == other.v2
        )

    def __getitem__(self, idx):
        if idx == 0: return self.v0
        elif idx == 1: return self.v1
        elif idx == 2: return self.v2
        else: raise IndexError("triangle only has 3 vertices (0, 1, 2)")

    def __setitem__(self, idx, value):
        if not isinstance(value, Vec3):
            raise TypeError("vertex must be a vec3")
        if idx == 0: self.v0 = value
        elif idx == 1: self.v1 = value
        elif idx == 2: self.v2 = value
        else: raise IndexError("triangle only has 3 vertices (0, 1, 2)")

    def __str__(self):
        return f"triangle({self.v0}, {self.v1}, {self.v2})"

    def __repr__(self):
        return f"triangle({repr(self.v0)}, {repr(self.v1)}, {repr(self.v2)})"

    def normal(self):
        # Returns the normal vector of the triangle (not normalized)
        return (self.v1 - self.v0).cross(self.v2 - self.v0)

    def area(self):
        # Returns the area of the triangle
        return 0.5 * (self.v1 - self.v0).cross(self.v2 - self.v0).magnitude()