from vec3 import Vec3

class Ray:
    def __init__(self, origin, direction):
        if not isinstance(origin, Vec3) or not isinstance(direction, Vec3):
            raise TypeError("origin and direction must be vec3 instances")
        self.origin = origin
        self.direction = direction

    def at(self, t):
        """Return the point along the ray at parameter t: origin + t * direction"""
        return self.origin + self.direction * t

    def __eq__(self, other):
        return isinstance(other, Ray) and self.origin == other.origin and self.direction == other.direction

    def __str__(self):
        return f"ray(origin={self.origin}, direction={self.direction})"

    def __repr__(self):
        return f"ray(origin={repr(self.origin)}, direction={repr(self.direction)})"
