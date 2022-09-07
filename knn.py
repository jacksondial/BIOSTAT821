"""Implement a KNN from 'scratch' only using numpy and plot with matplotlib."""
import numpy as np
import matplotlib.pyplot as plt


def generate_data() -> np.array:
    """Generate data."""
    mu0 = np.array([0, 0])
    mu1 = np.array([5, 0])
    Sigma0 = np.array([[1, 0], [0, 1]])
    Sigma1 = np.array([[1, 0], [0, 1]])
    points0 = np.random.multivariate_normal(mu0, Sigma0, size=100)
    points1 = np.random.multivariate_normal(mu1, Sigma1, size=100)
    return points0, points1


# print(generate_data()[1][1])


def distances(
    data1: np.array, data2: np.array, new_point: list[float]
) -> list[list[float]]:
    """Calculate distances."""
    distances1 = []
    j = 0
    b = np.array(new_point)
    for el in data1:
        a = np.array((data1))
        dist = np.linalg.norm(a[j] - b)
        distances1.append(dist)
        j += 1
    distances2 = []
    i = 0
    for el in data2:
        c = np.array(data2)
        dist = np.linalg.norm(c[i] - b)
        distances2.append(dist)
        i += 1
    distances1.sort()
    distances2.sort()
    return [distances1, distances2]


# print(distances(generate_data()[0], generate_data()[1], [5.0, 2.0]))

# sort each of the two lists, then compare the


def classify(distances: list[list[float]], k: int) -> int:
    """Classify single point."""
    total_obs = len(distances[0]) + len(distances[1])
    length1 = len(distances[0])
    length2 = len(distances[1])
    dist1 = distances[0]
    dist2 = distances[1]
    k_count = 0
    # print(distances)
    while k_count < k:
        if dist1[0] < dist2[0]:
            dist1.pop()
        else:
            dist2.pop()
        k_count += 1
    if len(dist1) < len(dist2):
        return 1
    else:
        return 2


# print(classify(distances(generate_data()[0], generate_data()[1], [0.0, 1.0]), 10))


def knn(
    points: list[list[float]], data1: np.array, data2: np.array, k: int
) -> np.array:
    """Classify list of points."""
    i = 0
    new_array1 = data1
    new_array2 = data2
    for list in points:
        new_point = points[i]
        # print(new_point)
        group = classify(distances(data1, data2, new_point), k)
        # print(group)
        if group == 1:
            new_point_arr = np.array(new_point).reshape(1, 2)
            new_array1 = np.concatenate((new_array1, new_point_arr))
            i += 1
        else:
            new_point_arr = np.array(new_point).reshape(1, 2)
            new_array2 = np.concatenate((new_array2, new_point_arr))
            i += 1
    return [new_array1, new_array2]


# print(classify(distances(generate_data()[0], generate_data()[1], [5.0, 2.0]), 10))

test_list = [
    [2.0, 4.0],
    [3.0, 4.9],
    [5.3, 1.1],
    [-1.0, 5.0],
    [0.2, 1.3],
    [-2.1, 0.0],
    [4.0, -0.2],
]

# print(
#     knn(
#         test_list,
#         generate_data()[0],
#         generate_data()[1],
#         10,
#     )
# )

plot_group1 = knn(
    test_list,
    generate_data()[0],
    generate_data()[1],
    10,
)[0]

plot_group2 = knn(
    test_list,
    generate_data()[0],
    generate_data()[1],
    10,
)[1]

# print(plot_group1[0])
# print(plot_group1[0][0])
# print(plot_group1[0][1])
# print(plot_group1[1])
# print(type(plot_group1))

x1train = []
y1train = []
i = 0
# print(plot_group1.shape[0])
# range(0, plot_group1.shape[0])

# do this while because the original train data is only 100 points
for point in plot_group1:
    while i < 100:
        single_point = plot_group1[i]
        x1train.append(single_point[0])
        y1train.append(single_point[1])
        i += 1

x1test = []
y1test = []
itest = 100
for point in plot_group1:
    while itest < plot_group1.shape[0]:
        single_point = plot_group1[itest]
        x1test.append(single_point[0])
        y1test.append(single_point[1])
        itest += 1

x2train = []
y2train = []
j = 0
# do this while because the original train data is only 100 points
for point in plot_group2:
    while j < 100:
        single_point = plot_group2[j]
        x2train.append(single_point[0])
        y2train.append(single_point[1])
        j += 1


x2test = []
y2test = []
jtest = 100
for point in plot_group2:
    while jtest < plot_group2.shape[0]:
        single_point = plot_group2[jtest]
        x2test.append(single_point[0])
        y2test.append(single_point[1])
        jtest += 1


plt.scatter(x1train, y1train, color="red")
plt.scatter(x2train, y2train, color="blue")
plt.scatter(x1test, y1test, color="red", marker="+")
plt.scatter(x2test, y2test, color="blue", marker="+")
plt.show()
