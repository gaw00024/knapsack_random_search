from itertools import product
from lab import Lab, QUIET, COMMENT

lab_name = '1.4 Exhaustive Search'


def run_lab(filename, n):
    lab = Lab(lab_name, filename, COMMENT)
    for solution in product([0, 1], repeat=n):
        lab.evaluate(solution, QUIET)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt', 20)
    exit(1)
    print
    run_lab('knap200.txt', 200)
