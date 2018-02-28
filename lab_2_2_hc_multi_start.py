from lab import Lab, QUIET, COMMENT

ITERATIONS = 100


def select_initial_solution(lab):
    solution = lab.random_solution()
    lab.evaluate(solution, QUIET)
    return solution


def find_improved_solution(lab, solution):
    for index in range(ITERATIONS):
        solution = lab.flip_random(solution)
        lab.evaluate(solution, QUIET)


def run_lab(filename):
    lab = Lab('2.2 Multi-start hill Climbing', filename, COMMENT)
    solution = select_initial_solution(lab)
    print lab.report()
    print ".."
    for index in range(7):
        find_improved_solution(lab, solution)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
