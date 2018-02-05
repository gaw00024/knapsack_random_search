from binary import initialise, mutation
from knapsack import evaluate, read_kfile

QUIET = True


class Lab:

    def __init__(self, name, filename):
        self.name = name
        number_of_items, capacity, items = read_kfile(filename)
        self.number_of_items = number_of_items
        self.capacity = capacity
        self.items = items
        self.best_objective_value = (0, 0)
        self.best_solution = []

        print "-- Lab: " + name + " (" + filename + "), #items: " + \
              str(number_of_items) + ", capacity: " + str(capacity)

    def random_solution(self):
        return initialise(self.number_of_items)

    @staticmethod
    def flip_bit(index, solution):
        solution[index] = 1 - solution[index]

    @staticmethod
    def flip_random(solution):
        return mutation(solution)

    def evaluate(self, solution, quiet=False):
        objective_value = evaluate(solution, self.items, self.capacity)
        if not quiet:
            print "Evaluating solution: " + str(solution) + \
                  ", Objective Value: " + str(objective_value)
        if objective_value[0] > self.best_objective_value[0] or \
                self.best_objective_value[0] == 0:
            self.best_solution = solution[:]
            self.best_objective_value = objective_value
        return objective_value

    def report(self):
        return "Best solution found: " + str(self.best_solution) + \
               "\nObjective Value (value, weight): " + \
               str(self.best_objective_value)
