from lab import Lab, QUIET, COMMENT

HC_ITERATIONS = 100
STARTS = 7


def select_initial_solution(lab):
    solution = lab.random_solution()
    lab.evaluate(solution, QUIET)
    return solution


def find_improved_solution(lab, solution):
    for index in range(HC_ITERATIONS):
        solution = lab.flip_random(solution)
        lab.evaluate(solution, QUIET)


def run_lab(filename):
    lab = Lab('2.2 Multi-start hill Climbing', filename, COMMENT)

    best_local_optimum = (0, 0)
    best_local_optimum_solution = []

    print "LOCAL OPTIMA.."
    for index in range(STARTS):
        lab.reset()
        starting_point = select_initial_solution(lab)

        find_improved_solution(lab, starting_point)
        local_optimum = lab.best_objective_value
        print lab.report()

        if local_optimum[0] > best_local_optimum[0]:
            best_local_optimum = local_optimum
            best_local_optimum_solution = lab.best_solution
    print
    print "BEST OF LOCAL OPTIMA:"
    lab.best_solution = best_local_optimum_solution
    lab.best_objective_value = best_local_optimum
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
