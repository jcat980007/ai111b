import math
import random
import matplotlib.pyplot as plt

# 定义12个旅游点坐标
points = [(2, 5), (5, 1), (7, 2), (3, 6), (8, 3), (6, 5), (1, 8), (4, 9), (9, 7), (8, 1), (3, 2), (6, 4)]


def get_distance(point1, point2):
    """
    计算两个点之间的距离
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def get_path_length(path):
    """
    计算路径长度
    """
    length = 0
    for i in range(len(path) - 1):
        length += get_distance(path[i], path[i + 1])
    length += get_distance(path[-1], path[0])
    return length


def get_neighbors(path):
    """
    获取相邻路径
    """
    neighbors = []
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            neighbor = path.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors


def hill_climbing(points, max_iter=100):
    """
    爬山算法
    """
    # 随机生成一个解
    current_path = random.sample(points, len(points))
    # 记录当前最优解
    best_path = current_path
    # 记录每次迭代的当前解
    paths = [current_path]
    # 记录当前最优解的长度
    best_length = get_path_length(current_path)
    # 迭代
    for i in range(max_iter):
        # 获取相邻路径
        neighbors = get_neighbors(current_path)
        # 选择最优路径作为下一次迭代的当前解
        next_path = min(neighbors, key=lambda path: get_path_length(path))
        # 如果找到了更优的解，更新最优解
        if get_path_length(next_path) < best_length:
            best_path = next_path
            best_length = get_path_length(best_path)
        # 将当前解更新为下一个解
        current_path = next_path
        # 记录当前解
        paths.append(current_path)
    return best_path, best_length, paths


# 绘制搜索路径图
plt.figure(figsize=(8, 8))
for i in range(len(paths) - 1):
    x = [point[0] for point in paths[i]]
    y = [point[1] for point in paths[i]]
    plt.plot(x + [x[0]], y + [y[0]], linestyle='dashed')
x = [point[0] for point in best_path]
y = [point[1] for point in best_path]
plt.plot(x + [x[0]], y + [y[0]], color='red', linewidth=2)
plt.scatter(x, y, color='black', s=80)
plt.title(f'TSP - Hill Climbing Algorithm\nPath Length: {best_distance:.3f}')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

