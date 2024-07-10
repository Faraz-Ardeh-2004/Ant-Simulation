# Ant Colony Optimization using Genetic Algorithm

## Project Overview

This project implements an Ant Colony Optimization (ACO) algorithm using a Genetic Algorithm approach to solve the Santa Fe Trail problem. The goal is to evolve an optimal strategy for an ant to collect as much food as possible on a 2D grid within a limited number of time steps.

## Repository Structure

- `Main.py`: Main script to run the genetic algorithm and output results
- `Environment.py`: Defines the Environment class that manages the 2D grid
- `Ant.py`: Implements the Ant class with movement and sensing capabilities
- `Genetic_Algorithm.py`: Contains the GeneticAlgorithm class that evolves the ant's behavior
- `santafe.txt`: Input file describing the initial state of the environment

## How It Works

1. The environment is loaded from `santafe.txt`, defining a 32x32 grid where '1' represents food and '0' represents empty cells.
2. A population of ants with random genetic codes is initialized.
3. The genetic algorithm evolves the population over multiple generations:
   - Ants move through the environment based on their genetic code.
   - Fitness is determined by the amount of food collected.
   - Selection, crossover, and mutation operations are applied to create new generations.
4. The best performing ant's trail is saved to `muir_trail.txt`.

## Usage

Run the main script:

This will execute the genetic algorithm and print progress and final results to the console.

## Genetic Algorithm Parameters

Adjust these parameters in `Main.py`:

- `population_size`: Number of individuals in each generation (default: 100)
- `max_generations`: Maximum number of generations to evolve (default: 50)
- `crossover_rate`: Probability of crossover between two parents (default: 0.7)
- `mutation_rate`: Probability of mutation for each gene (default: 0.01)

## Output

The program outputs:
- Generation-by-generation progress
- Final results including best fitness, best genome, and generation statistics
- A file `muir_trail.txt` showing the path of the best-performing ant
<img width="428" alt="Screenshot 2024-07-10 at 10 10 49 AM" src="https://github.com/Faraz-Ardeh-2004/Ant-Simulation/assets/59162288/f4f2e29f-c1a4-4de4-9362-0af06c293ac5">



## Evaluation Criteria

The primary metric for evaluating performance is the amount of food collected by an ant in 200 time steps. Higher scores are better. The program also outputs average fitness, minimum fitness, and maximum fitness for each generation.

## Requirements

- Python 3.x

No additional libraries are required as the project uses only Python standard libraries.

## Future Improvements

- Implement different selection methods (e.g., roulette wheel selection)
- Add adaptive mutation rates
- Experiment with different crossover techniques
- Parallelize fitness evaluations for faster execution
- Visualize the best ant's path

## Contributing

Contributions to improve the algorithm or extend its functionality are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
