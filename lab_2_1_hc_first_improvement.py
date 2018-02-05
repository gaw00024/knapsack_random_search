from lab import Lab


def select_initial_solution(lab):
    solution = lab.random_solution()
    lab.evaluate(solution)
    return solution


def find_improved_solution(lab, solution):
    for index in range(100):
        solution = lab.flip_random(solution)
        lab.evaluate(solution)


def run_lab(filename):
    lab = Lab('2.1 First improvement (random mutation) Hill-climbing',
              filename)
    solution = select_initial_solution(lab)
    print lab.report()
    find_improved_solution(lab, solution)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
