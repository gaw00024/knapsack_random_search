from lab import Lab, QUIET, COMMENT


def select_initial_solution(lab):
    solution = lab.random_solution()
    lab.evaluate(solution, QUIET)
    return solution


def find_improved_solution(lab, solution):
    for index in range(100):
        solution = lab.flip_2_bit(solution)
        lab.evaluate(solution, QUIET)
    return solution


def run_lab(filename):
    lab = Lab('2.4 Iterated Local Search', filename, COMMENT)
    solution = select_initial_solution(lab)
    print lab.report()
    print ".."
    find_improved_solution(lab, solution)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
