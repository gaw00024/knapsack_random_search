# Single knapsack problem. Auxiliary code for implementing search heuristics
# by Gabriela Ochoa, October 2017

# Read the instance  data given a file name. Returns: n = no. items,
# c = capacity, items = 2 dimension array with values and weigths


def read_kfile(fname):
    with open(fname, 'rU') as kfile:
        lines = kfile.readlines()
    n = int(lines[0])
    c = int(lines[n + 1])
    items = [map(int, line.split()) for line in lines[1:n + 1]]
    return n, c, items


# Knapsack evaluation (fitness) function.
# Input: sol a vector of integers,
# items = 2 dimension array with values and weigths
# Returns: fitness = total value of the sack if valid solution or zero
# if invalid, weigth of the sack

def evaluate(sol, items, c):
    l = len(sol)
    weight = sum([sol[i] * items[i][2] for i in range(l)])
    if weight > c:
        fitness = 0
    else:
        fitness = sum([sol[i] * items[i][1] for i in range(l)])
    return fitness, weight

