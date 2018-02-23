from Population import Population


p = Population(50, 'knap20.txt')
p.evaluate()

print p.fitness
print

for run in range(10):
    parent_a = p.tournament_selection()
    parent_b = p.tournament_selection()
    child_a = p.crossover(parent_a, parent_b)
    child_b = p.crossover(parent_a, parent_b)
    p.mutate(child_a)
    p.mutate(child_b)
    fitness_a = p.evaluate_solution(child_a)  # ?
    fitness_b = p.evaluate_solution(child_b)  # ?
    print fitness_a, fitness_b
    p.replace_worst(child_a, child_b)
    print p.fitness

print p.report()

# tournament selection of size 2
# replace two worst individuals at each iteration
# 1-flip mutation
# 1-point crossover
# population = 50

