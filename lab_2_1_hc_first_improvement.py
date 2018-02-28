from lab import Lab, QUIET, COMMENT

ITERATIONS = 100


def select_initial_solution(lab):
    solution = lab.random_solution()
    lab.evaluate(solution)
    return solution


def find_improved_solution(lab, solution):
    for index in range(ITERATIONS):
        solution = lab.flip_random(solution)
        lab.evaluate(solution, QUIET)


def run_lab(filename):
    lab = Lab('2.1 First improvement (random mutation) Hill-climbing',
              filename, COMMENT)
    solution = select_initial_solution(lab)
    print lab.report()
    print ".."
    find_improved_solution(lab, solution)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
