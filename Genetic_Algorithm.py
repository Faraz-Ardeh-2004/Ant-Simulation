import random
from Ant import Ant

class GeneticAlgorithm:
    def __init__(self, population_size, max_generations, crossover_rate, mutation_rate):
        self.population_size = population_size
        self.max_generations = max_generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def initialize_population(self):
        return [''.join(str(random.randint(0, 9)) for _ in range(30)) for _ in range(self.population_size)]

    def fitness(self, genes, environment):
        environment.reset()  # Reset environment before each evaluation
        ant = Ant(genes)
        for _ in range(200):  # 200 time steps
            food_ahead = ant.sense(environment)
            ant.update_state(food_ahead)
            ant.move(environment)
        return ant.food_eaten

    def select(self, population, fitnesses):
        tournament_size = 3
        selected = []
        for _ in range(len(population)):
            tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
            winner = max(tournament, key=lambda x: x[1])[0]
            selected.append(winner)
        return selected

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        return parent1, parent2

    def mutate(self, individual):
        return ''.join(gene if random.random() > self.mutation_rate else str(random.randint(0, 9)) for gene in individual)

    def evolve(self, environment):
        population = self.initialize_population()
        best_fitness = 0
        best_individual = None

        for generation in range(self.max_generations):
            fitnesses = [self.fitness(ind, environment) for ind in population]
            
            current_best = max(fitnesses)
            if current_best > best_fitness:
                best_fitness = current_best
                best_individual = population[fitnesses.index(best_fitness)]

            selected = self.select(population, fitnesses)
            
            next_generation = []
            for i in range(0, len(selected), 2):
                parent1, parent2 = selected[i], selected[i+1] if i+1 < len(selected) else selected[0]
                child1, child2 = self.crossover(parent1, parent2)
                next_generation.extend([self.mutate(child1), self.mutate(child2)])

            population = next_generation

            yield generation + 1, population, fitnesses, best_individual, best_fitness

        return best_individual, best_fitness
