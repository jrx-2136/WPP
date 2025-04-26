import numpy as np

N = 10
cartesian_points = np.random.rand(N, 2) * 100  # Random points in the range [0, 100)


# r = sqrt(x^2 + y^2), theta = arctan(y / x)
x = cartesian_points[:, 0]
y = cartesian_points[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

polar_points = np.column_stack((r, theta))

print("Cartesian Points:\n", cartesian_points)
print("\nPolar Coordinates:\n", polar_points)