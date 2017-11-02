import datetime
import random
import genetic
import unittest


class GuessPasswordTests(unittest.TestCase):

    def test_hello_world(self):
        target = 'Hello World!'
        self.guess_password(target)

    def guess_password(self, target):
        gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
        start_time = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(genes):
            display(genes, target, start_time)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(
            target), optimalFitness, gene_set, fnDisplay)
        self.assertEqual(best, target)


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)


def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))


if __name__ == '__main__':
    unittest.main()
