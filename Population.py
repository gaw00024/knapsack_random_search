from random import randint

import sys

from binary import initialise, xover_1pt, mutation
from knapsack import read_kfile, evaluate


class Population:
    def __init__(self, size, filename):
        number_of_items, capacity, items = read_kfile(filename)
        self.number_of_items = number_of_items
        self.capacity = capacity
        self.items = items
        self.size = size
        self.p = [0] * size
        for i in range(size):
            self.p[i] = initialise(number_of_items)
        self.fitness = []

    def evaluate(self):
        self.fitness = []
        for solution in self.p:
            self.fitness.append(evaluate(solution, self.items, self.capacity))

    def evaluate_solution(self, solution):
        return evaluate(solution, self.items, self.capacity)

    def select_random_individual(self):
        return self.p[randint(0, self.size - 1)]

    def tournament_selection(self):
        s1 = self.select_random_individual()
        s2 = self.select_random_individual()
        if evaluate(s1, self.items, self.capacity)[0] > evaluate(s2, self.items, self.capacity)[0]:
            return s1
        else:
            return s2

    def crossover(self, solution1, solution2):
        return xover_1pt(solution1, solution2)

    def mutate(self, solution):
        mutation(solution)

    def replace_worst(self, r1, r2):
        worst_seen = sys.maxint
        worst_seen_index = -1
        for i in range(self.size):
            if self.fitness[i][0] < worst_seen:
                worst_seen = self.fitness[i][0]
                worst_seen_index = i

        # replace worst seen with r1
        self.p[worst_seen_index] = r1
        self.fitness[worst_seen_index] = self.evaluate_solution(r1)

        worst_seen = sys.maxint
        worst_seen_index = -1
        for i in range(self.size):
            if self.fitness[i][0] < worst_seen:
                worst_seen = self.fitness[i][0]
                worst_seen_index = i

        # replace worst seen with r2
        self.p[worst_seen_index] = r2
        self.fitness[worst_seen_index] = self.evaluate_solution(r2)

    def report(self):
        best_seen = -1
        best_seen_index = -1
        for i in range(self.size):
            if self.fitness[i][0] > best_seen:
                best_seen = self.fitness[i][0]
                best_seen_index = i

        return "Best solution found: " + str(self.p[best_seen_index]) + \
               "\nObjective Value (value, weight): " + \
               str(self.fitness[best_seen_index])
