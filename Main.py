from Environment import Environment
from Genetic_Algorithm import GeneticAlgorithm
from Ant import Ant

def main():
    # Hyper_parameters
    population_size = 100
    max_generations = 50
    crossover_rate = 0.7
    mutation_rate = 0.01

    # Initialize environment
    muir_env = Environment("santafe.txt")

    # Run genetic algorithm
    ga = GeneticAlgorithm(population_size, max_generations, crossover_rate, mutation_rate)
    
    best_fitness = 0
    best_individual = None
    best_generation = 0

    print("Generation Progress:")
    for gen_num, population, fitnesses, current_best_individual, current_best_fitness in ga.evolve(muir_env):
        print(f"{gen_num},{current_best_fitness},{sum(fitnesses)/len(fitnesses):.2f},{min(fitnesses)},{max(fitnesses)}")
        
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_individual = current_best_individual
            best_generation = gen_num

    # Calculate final results and datas
    final_fitnesses = [ga.fitness(ind, muir_env) for ind in population]
    avg_fitness = sum(final_fitnesses) / len(final_fitnesses)
    min_fitness = min(final_fitnesses)
    max_fitness = max(final_fitnesses)

    # Print final results
    print("\nFinal results:")
    print(f"best fitness: {best_fitness}")
    print(f"best genome: {best_individual}")
    print(f"Best generation: {best_generation}")
    print(f"Average fitness: {avg_fitness:.2f}")
    print(f"Lowest fitness: {min_fitness}")
    print(f"highest fitness: {max_fitness}")

    # Save trail of best individual in new file
    muir_env.reset()
    ant = Ant(best_individual)
    for _ in range(200):
        food_ahead = ant.sense(muir_env)
        ant.update_state(food_ahead)
        ant.move(muir_env)
    
    with open("muir_trail.txt", "w") as f:
        for row in muir_env.grid:
            f.write("".join(row) + "\n")

if __name__ == "__main__":
    main()
