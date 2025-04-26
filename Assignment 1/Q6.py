import math
points = []
current_point = []
nearest_neighbors_list = []
distances = []

for i in range(10):
    print("Enter the 3d point for point P" + str(i + 1))
    for j in range(3):
        if j == 0:
            x = int(input("Enter x point: "))
            current_point.append(x)
        elif j == 1:
            y = int(input("Enter y point: "))
            current_point.append(y)
        elif j == 2:
            z = int(input("Enter z point: "))
            current_point.append(z)
    points.append(current_point)
    current_point = []

for i in range(10):
    for j in range(10):
        if j != i:
            under_root = ((points[j][0] - points[i][0]) ** 2 +
                          (points[j][1] - points[i][1]) ** 2 +
                          (points[j][2] - points[i][2]) ** 2)
            distances.append((math.sqrt(under_root), j + 1))
    nearest_neighbor = min(distances, key=lambda x: x[0])
    nearest_neighbors_list.append(nearest_neighbor)
    distances = []

print("The given 3d points:")
for i in range(10):
    print("P" + str(i + 1) + ": " + str(points[i]))

print("\n")
for i in range(10):
    print("P" + str(i + 1) + "'s nearest point is P" + str(nearest_neighbors_list[i][1]) + " with the distance of {:.2f}".format(nearest_neighbors_list[i][0]))















