import unittest

from lab import Lab


class Tests(unittest.TestCase):
    def setUp(self):
        self.lab = Lab('Random Solution (20)', 'knap20.txt')

    def test_initial_state(self):
        self.assertEqual('Random Solution (20)', self.lab.name)
        self.assertEqual(20, self.lab.number_of_items)
        self.assertEqual(524, self.lab.capacity)
        self.assertListEqual([], self.lab.best_solution)
        self.assertTupleEqual((0, 0), self.lab.best_objective_value)

    def test_evaluate(self):
        solution = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0]
        self.assertTupleEqual((429, 431), self.lab.evaluate(solution))
        solution = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
        self.assertTupleEqual((531, 496), self.lab.evaluate(solution))
        solution = [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]
        self.assertTupleEqual((726, 519), self.lab.evaluate(solution))

    def test_best(self):
        solution = [0] * 20
        self.assertTupleEqual((0, 0), self.lab.evaluate(solution))
        solution[0] = 1
        self.assertTupleEqual((91, 29), self.lab.evaluate(solution))
        solution[0] = 0
        self.assertTupleEqual((0, 0), self.lab.evaluate(solution))
        self.assertTupleEqual((91, 29), self.lab.best_objective_value)
