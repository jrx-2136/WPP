import math

class Vector2D:
    def __init__(self, x, y):
        """Initialize a 2D vector with x and y components."""
        self.x = x
        self.y = y

    def magnitude(self):
        """Return the magnitude (length) of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_with_x_axis(self):
        """Return the angle (in degrees) the vector makes with the X-axis."""
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        """Calculate the distance between two vectors (points)."""
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def dot_product(self, other):
        """Calculate the dot product with another 2D vector."""
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        """Calculate the cross product with another 2D vector (returns a scalar)."""
        return self.x * other.y - self.y * other.x

    def display(self):
        """Display vector components."""
        print(f"Vector: ({self.x}, {self.y})")

# Extend to 3D using inheritance
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        """Initialize a 3D vector with x, y, and z components."""
        super().__init__(x, y)  # Initialize x and y from Vector2D
        self.z = z

    def magnitude(self):
        """Return the magnitude of the 3D vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dot_product(self, other):
        """Calculate the dot product with another 3D vector."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        """Calculate the cross product with another 3D vector (returns a new vector)."""
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

    def distance(self, other):
        """Calculate the distance between two 3D vectors (points)."""
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)

    def display(self):
        """Display vector components."""
        print(f"Vector: ({self.x}, {self.y}, {self.z})")

# Example Usage
v2d_1 = Vector2D(3, 4)
v2d_2 = Vector2D(1, 2)
print("2D Vector Operations:")
v2d_1.display()
print("Magnitude:", v2d_1.magnitude())
print("Angle with X-axis:", v2d_1.angle_with_x_axis())
print("Distance:", v2d_1.distance(v2d_2))
print("Dot Product:", v2d_1.dot_product(v2d_2))
print("Cross Product:", v2d_1.cross_product(v2d_2))
print()

v3d_1 = Vector3D(3, 4, 5)
v3d_2 = Vector3D(1, 2, 3)
print("3D Vector Operations:")
v3d_1.display()
print("Magnitude:", v3d_1.magnitude())
print("Distance:", v3d_1.distance(v3d_2))
print("Dot Product:", v3d_1.dot_product(v3d_2))
cross_prod_3d = v3d_1.cross_product(v3d_2)
print("Cross Product:", (cross_prod_3d.x, cross_prod_3d.y, cross_prod_3d.z))
