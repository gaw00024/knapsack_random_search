from lab import Lab, COMMENT


def run_lab(filename):
    lab = Lab('1.2 Random Search', filename, COMMENT)
    for index in range(100):
        solution = lab.random_solution()
        lab.evaluate(solution)
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
