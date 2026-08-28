import random

teachers = ['T1', 'T2', 'T3', 'T4', 'T5']
courses = ['C1', 'C2', 'C3', 'C4', 'C5']

slots_per_day = 5
days = 5
total_slots = slots_per_day * days 

population_size = 20
mutation_rate = 0.1
generations = 200


def create_chromosome():
    chromosome = []

    course_list = []
    for c in courses:
        course_list += [c] * 3

    while len(course_list) < total_slots:
        course_list.append(random.choice(courses))

    random.shuffle(course_list)

    for c in course_list:
        t = random.choice(teachers)
        chromosome.append((c, t))

    return chromosome


def fitness(chromosome):
    penalty = 0

    for day in range(days):
        start = day * slots_per_day
        end = start + slots_per_day
        day_slots = chromosome[start:end]

        teachers_in_slot = [t for (c, t) in day_slots]
        if len(teachers_in_slot) != len(set(teachers_in_slot)):
            penalty += 10  

    course_count = {}
    for c, t in chromosome:
        course_count[c] = course_count.get(c, 0) + 1

    for c in courses:
        penalty += abs(course_count.get(c, 0) - 3) * 5

    for t in teachers:
        count = 0
        for slot in chromosome:
            if slot[1] == t:
                count += 1
                if count > 3:
                    penalty += 5
            else:
                count = 0

    return penalty


def selection(population):
    population.sort(key=lambda x: fitness(x))
    return population[:len(population)//2]


def crossover(p1, p2):
    point = random.randint(1, total_slots - 2)
    return p1[:point] + p2[point:]


def mutate(chromosome):
    i, j = random.sample(range(total_slots), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome


def genetic_algorithm():
    population = [create_chromosome() for _ in range(population_size)]

    for gen in range(generations):
        fitness_scores = [fitness(ch) for ch in population]
        best = min(fitness_scores)

        print(f"Generation {gen+1}, Best Fitness: {best}")

        if best == 0:
            break

        parents = selection(population)

        new_population = []

        while len(new_population) < population_size:
            p1, p2 = random.sample(parents, 2)
            child = crossover(p1, p2)

            if random.random() < mutation_rate:
                child = mutate(child)

            new_population.append(child)

        population = new_population

    best_chromosome = min(population, key=fitness)
    return best_chromosome, fitness(best_chromosome)


best_solution, best_score = genetic_algorithm()

print("\nFinal Best Timetable:")
for i, slot in enumerate(best_solution):
    day = i // slots_per_day + 1
    time = i % slots_per_day + 1
    print(f"Day {day}, Slot {time}: {slot}")

print("\nFinal Fitness (Penalty):", best_score)