import random
import math
import matplotlib.pyplot as plt

# 定义旅行点的坐标
points = [(2, 5), (5, 1), (7, 2), (3, 6), (8, 3), (6, 5), (1, 8), (4, 9), (9, 7), (8, 1), (3, 2), (6, 4)]

# 计算旅行路径的总长度
def calculate_distance(points):
    distance = 0
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        distance += ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance

# 生成初始种群
def generate_initial_population(points, population_size):
    population = []
    for i in range(population_size):
        individual = points[:]
        random.shuffle(individual)
        population.append(individual)
    return population

# 计算种群中每个个体的适应度
def calculate_fitness(population):
    fitness_scores = []
    for individual in population:
        fitness_scores.append(1 / calculate_distance(individual))
    return fitness_scores

# 选择算子
def selection(population, fitness_scores):
    index1 = random.randint(0, len(population)-1)
    index2 = random.randint(0, len(population)-1)
    while index2 == index1:
        index2 = random.randint(0, len(population)-1)
    if fitness_scores[index1] > fitness_scores[index2]:
        return population[index1]
    else:
        return population[index2]

# 交叉算子
def crossover(parent1, parent2):
    index1 = random.randint(0, len(parent1)-1)
    index2 = random.randint(0, len(parent1)-1)
    while index2 == index1:
        index2 = random.randint(0, len(parent1)-1)
    if index1 > index2:
        index1, index2 = index2, index1
    child = [-1] * len(parent1)
    for i in range(index1, index2+1):
        child[i] = parent1[i]
    j = 0
    for i in range(len(parent2)):
        if parent2[i] not in child:
            while child[j] != -1:
                j += 1
            child[j] = parent2[i]
    return child

# 变异算子
def mutation(individual):
    index1 = random.randint(0, len(individual)-1)
    index2 = random.randint(0, len(individual)-1)
    individual[index1], individual[index2] = individual[index2], individual[index1]
    return individual

# 遗传算法主程序
def genetic_algorithm(points, population_size, num_generations):
    # 生成初始种群
    population = generate_initial_population(points, population_size)
    for generation in range(num_generations):
        # 计算种群中每个个体的适应度
        fitness_scores = calculate_fitness(population)
        # 选择下一代个体
        next_generation = []
        for i in range(population_size):
            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:
                child = mutation(child)
            next_generation.append(child)
        population = next_generation
    # 返回最优个体
    return max(population, key=lambda individual: 1 / calculate_distance(individual))

points = [(2, 5), (5, 1), (7, 2), (3, 6), (8, 3), (6, 5), (1, 8), (4, 9), (9, 7), (8, 1), (3, 2), (6, 4)]

population_size = 100
num_generations = 500

best_individual = genetic_algorithm(points, population_size, num_generations)

# 将最优个体的路径画出来
plt.figure(figsize=(8, 8))
x = [point[0] for point in best_individual]
y = [point[1] for point in best_individual]
plt.plot(x, y, marker='o')
plt.plot(x + [x[0]], y + [y[0]], linestyle='dashed')
plt.show()
