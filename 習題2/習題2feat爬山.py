import random

# 旅行點的坐標
points = [(2, 5), (5, 1), (7, 2), (3, 6), (8, 3), (6, 5), (1, 8), (4, 9), (9, 7), (8, 1), (3, 2), (6, 4)]

# 計算旅行路径的總長度
def calculate_distance(points):
    distance = 0
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        distance += ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance

# 交换操作
def swap(points, i, j):
    points[i], points[j] = points[j], points[i]

# 爬山算法主程序
def hill_climbing_algorithm(points):
    current_route = points[:]
    current_distance = calculate_distance(current_route)
    while True:
        neighbors = []
        for i in range(len(current_route)-1):
            for j in range(i+1, len(current_route)):
                neighbor = current_route[:]
                swap(neighbor, i, j)
                neighbors.append(neighbor)
        if not neighbors:
            break
        neighbor_distances = [calculate_distance(neighbor) for neighbor in neighbors]
        best_neighbor_distance = min(neighbor_distances)
        if best_neighbor_distance >= current_distance:
            break
        best_neighbor_index = neighbor_distances.index(best_neighbor_distance)
        current_route = neighbors[best_neighbor_index]
        current_distance = best_neighbor_distance
    return current_route

# 测試程序
best_route = hill_climbing_algorithm(points)
print(best_route)
print(calculate_distance(best_route))