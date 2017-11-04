
"""
extract the genetic engine code from that specific to guessing the password so it can be reused for other projects.

"""

import random


class Chromosome:
    Genes = None
    Fitness = None

    """docstring for Chromosome:"""

    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    genes = ''.join(genes)
    fitness = get_fitness(genes)

    return Chromosome(genes, fitness)


def _mutate(parent, geneSet, get_fitness):
    index = random.randrange(0, len(parent))
    child_genes = list(parent)
    new_gene, alternate = random.sample(geneSet, 2)
    child_genes[index] = alternate \
        if new_gene == child_genes[index] \
        else new_gene
    genes = ''.join(child_genes)
    fitness = get_fitness(genes)

    return Chromosome(genes, fitness)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    best_parent = _generate_parent(targetLen, geneSet)
    best_fitness = get_fitness(best_parent)
    display(best_parent)
    if best_fitness >= optimalFitness:
        return best_parent

    while True:
        child = _mutate(best_parent, geneSet, get_fitness)
        child_fitness = get_fitness(child)

        if best_fitness >= child_fitness:
            continue
        display(child)
        if child_fitness >= optimalFitness:
            return child
        best_fitness = child_fitness
        best_parent = child
