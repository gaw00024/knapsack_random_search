# binary.py -- Implements a genetic representation as a list of integers (0, 1)
# A set of simple variation operators: mutation, 1ptXover and perturbation
#
# Gabriela ochoa

from random import randint


# Initialise a random solution
def initialise(size):
    return [randint(0, 1) for i in range(size)]


# 1pt- crossover. Input: 2 solutions. Returns a single offsprung

def xover_1pt(sol1, sol2):
    xp = randint(0, len(sol1) - 1)
    return [sol1[:xp] + sol2[xp:]]


# 1-flip mutation. Input: a solution. Returns: a mutated solution
def mutation(sol):
    pos = randint(0, len(sol) - 1)
    sol[pos] = 0 if sol[pos] else 1
    return sol


# This is a stronger mutation operator to be used in the Iterated Local Search Algorithm
# This implememtation simply conducts two applications of the single mutation operation

def perturbation(sol):
    l = len(sol)
    pos1 = pos2 = randint(0, l - 1)
    while (pos1 == pos2):
        pos2 = randint(0, l - 1)
    sol[pos1] = 0 if sol[pos1] else 1
    sol[pos2] = 0 if sol[pos2] else 1
    return sol


