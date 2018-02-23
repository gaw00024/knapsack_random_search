import unittest

from Population import Population

POP_SIZE = 50


class Tests(unittest.TestCase):
    def setUp(self):
        self.population = Population(POP_SIZE, 'knap20.txt')

    def test_initial_state(self):
        self.assertEqual(POP_SIZE, self.population.size)
        self.assertEqual(POP_SIZE, len(self.population.p))
        self.assertEqual(20, len(self.population.p[0]))
        self.assertEqual(0, len(self.population.fitness))

    def test_evaluate_solution(self):
        s1 = [0] * 20
        self.assertTupleEqual((0, 0), self.population.evaluate_solution(s1))
        s1[0] = 1
        self.assertTupleEqual((91, 29), self.population.evaluate_solution(s1))

    def test_evaluate(self):
        self.population.evaluate()
        self.assertEqual(POP_SIZE, len(self.population.fitness))
        self.population.evaluate()
        self.assertEqual(POP_SIZE, len(self.population.fitness))

        self.population.p[0] = [0] * 20
        self.population.evaluate()
        self.assertTupleEqual((0, 0), self.population.fitness[0])

        self.population.p[POP_SIZE - 1] = [0] * 20
        self.population.evaluate()
        self.assertTupleEqual((0, 0), self.population.fitness[POP_SIZE - 1])

    def test_select_random_individual(self):
        solution = self.population.select_random_individual()
        self.assertIsInstance(solution, list)

    def test_tournament_selection(self):
        solution = self.population.tournament_selection()
        print solution
        self.assertIsInstance(solution, list)

    def test_crossover(self):
        s1 = [0] * 20
        s2 = [1] * 20
        s3 = self.population.crossover(s1, s2)
        self.assertIsInstance(s3, list)

    def test_mutate(self):
        s1 = [0] * 20
        s2 = s1[:]
        self.population.mutate(s2)
        self.assertFalse(s2 == s1)

    def test_replace_worst(self):
        self.population.evaluate()

        r1 = [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]
        r2 = [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]  # o
        self.population.fitness[POP_SIZE / 2] = (-1, -1)
        self.population.fitness[POP_SIZE - 1] = (-1, -1)
        self.population.replace_worst(r1, r2)
        self.assertListEqual(self.population.p[POP_SIZE / 2], r1)
        self.assertListEqual(self.population.p[POP_SIZE - 1], r2)

    def test_report(self):
        # print(self.population.fitness)
        self.population.evaluate()
        # print(self.population.fitness)
        # print self.population.report()
