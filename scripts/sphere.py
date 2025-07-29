from vec3 import Vec3

class Sphere:
    def __init__(
            self, center: Vec3,
            radius: float | int,
            material = None):
        self.center = center
        self.radius = radius
        self.material = material

    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius
