import random

# 旅行點的坐標
points = [(2, 5), (5, 1), (7, 2), (3, 6), (8, 3), (6, 5), (1, 8), (4, 9), (9, 7), (8, 1), (3, 2), (6, 4)]

# 生成初始種群
def generate_population(size):
    population = []
    for i in range(size):
        individual = random.sample(points, len(points))
        population.append(individual)
    return population

# 計算旅行路径的總長度
def calculate_distance(points):
    distance = 0
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        distance += ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance

# 計算種群中每個個體的適應度
def calculate_fitness(population):
    fitness = []
    for individual in population:
        distance = calculate_distance(individual)
        fitness.append(1/distance)
    return fitness

# 選擇個體
def select(population, fitness):
    total_fitness = sum(fitness)
    probabilities = [f/total_fitness for f in fitness]
    selected = random.choices(population, probabilities, k=2)
    return selected[0], selected[1]

# 交叉操作
def crossover(individual1, individual2):
    point1 = random.randint(0, len(individual1)-1)
    point2 = random.randint(point1, len(individual1)-1)
    child = individual1[:point1] + individual2[point1:point2] + individual1[point2:]
    return child

# 變異操作
def mutate(individual):
    point1 = random.randint(0, len(individual)-1)
    point2 = random.randint(0, len(individual)-1)
    individual[point1], individual[point2] = individual[point2], individual[point1]
    return individual

# 遗傳演算法主程序
def genetic_algorithm(population_size, generations):
    population = generate_population(population_size)
    for i in range(generations):
        fitness = calculate_fitness(population)
        new_population = []
        for j in range(population_size//2):
            parent1, parent2 = select(population, fitness)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
    best_individual = max(population, key=calculate_fitness)
    return best_individual

# 测試程序
best_route = genetic_algorithm(100, 1000)
print(best_route)
print(calculate_distance(best_route))