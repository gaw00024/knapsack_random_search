from lab import Lab, COMMENT


def select_initial_solution(lab):
    solution = lab.random_solution()
    lab.evaluate(solution)
    return solution


def find_improved_solution(lab, solution):
    for index in range(lab.number_of_items):
        lab.flip_1_bit(index, solution)
        lab.evaluate(solution)
        lab.flip_1_bit(index, solution)


def run_lab(filename):
    lab = Lab('1.3 Neighbours', filename, COMMENT)
    solution = select_initial_solution(lab)
    print lab.report()
    find_improved_solution(lab, solution)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
