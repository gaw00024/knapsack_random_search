from lab import Lab, QUIET, COMMENT

ITERATIONS = 100


def select_initial_solution(lab):
    solution = lab.random_solution()
    lab.evaluate(solution)
    return solution


def find_best_in_neighborhood(lab, solution):
    for index in range(lab.number_of_items):
        lab.flip_1_bit(index, solution)
        lab.evaluate(solution, QUIET)
        lab.flip_1_bit(index, solution)


def find_improved_solution(lab, solution):
    for index in range(ITERATIONS):
        solution = lab.flip_random(solution)
        find_best_in_neighborhood(lab, solution)


def run_lab(filename):
    lab = Lab('2.3 Best-improvement hill Climbing', filename, COMMENT)
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
