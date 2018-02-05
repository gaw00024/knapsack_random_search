from itertools import product
from lab import Lab, QUIET

lab_name = '1.4 Exhaustive Search'


def run_lab(filename):
    lab = Lab(lab_name, filename)
    for solution in product([0, 1], repeat=20):
        lab.evaluate(solution, QUIET)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    exit(1)
    print
    run_lab('knap200.txt')
