from Population import Population


# A steady-state Genetic Algorithm with the following characteristics:
#   tournament selection of size 2
#   replace two worst individuals at each iteration
#   1-flip mutation
#   1-point crossover
#   population = 50
GENERATIONS = 1000

# Conclusions:
#   The vastly outperforms the iterated local search both in number of
#   iterations/generations required, and location of the optimum fitness.


def run_lab(filename):

    p = Population(50, filename)
    p.evaluate()

    for run in range(GENERATIONS):
        parent_a = p.tournament_selection()
        parent_b = p.tournament_selection()
        child_a = p.crossover(parent_a, parent_b)
        child_b = p.crossover(parent_a, parent_b)
        p.mutate(child_a)
        p.mutate(child_b)
        fitness_a = p.evaluate_solution(child_a)
        fitness_b = p.evaluate_solution(child_b)
        if fitness_a[0]:
            p.replace_worst(child_a)
        if fitness_b[0]:
            p.replace_worst(child_b)
        p.evaluate()

    return p.report()


if __name__ == '__main__':
    report = run_lab('knap20.txt')
    print report
    print
    report = run_lab('knap200.txt')
    print report
