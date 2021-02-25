from deap import base
from deap import creator
from deap import cma
import numpy as np


class OptimizerCmaEs:

    def __init__(self, individual_size: int, population_size):
        self.individual_size = individual_size

        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, typecode='b', fitness=creator.FitnessMax)

        strategy = cma.Strategy(centroid=[0.0] * individual_size, sigma=1.0, lambda_=population_size)

        self.toolbox = base.Toolbox()
        self.toolbox.register("generate", strategy.generate, creator.Individual)
        self.toolbox.register("update", strategy.update)

        self.population = None

    def ask(self):
        # Generate a new population
        self.population = self.toolbox.generate()
        genomes = []
        for individual in self.population:
            genomes.append(np.array(individual))

        return genomes

    def tell(self, rewards):
        # Update the strategy with the evaluated individuals
        self.toolbox.update(self.population)
        for ind, fit in zip(self.population, rewards):
            ind.fitness.values = (fit,)
