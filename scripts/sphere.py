from vec3 import Vec3
from material import Material

class Sphere:
    def __init__(
            self, center: Vec3,
            radius: float | int,
            material: Material = None):
        self.center = center
        self.radius = radius
        self.material = material

    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius
