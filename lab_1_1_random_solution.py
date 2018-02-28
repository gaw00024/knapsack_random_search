from lab import Lab, COMMENT


def run_lab(filename):
    lab = Lab('1.1 Random Solution', filename, COMMENT)
    lab.evaluate(lab.random_solution())
    print lab.report()


if __name__ == '__main__':
    run_lab('knap20.txt')
    print
    run_lab('knap200.txt')
