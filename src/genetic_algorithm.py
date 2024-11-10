import numpy as np
import matplotlib.pyplot as plt
import time
from general_func import calculate_deviation
from general_func import generate_cube


MAGIC_SUM = 315

def crossover(parent1, parent2):
    point = np.random.randint(1, 5)
    child = np.copy(parent1)
    child[:, :, point:] = parent2[:, :, point:]
    return child

def mutate(cube):
    i, j, k, i2, j2, k2 = np.random.randint(0, 5, 6)
    cube[i, j, k], cube[i2, j2, k2] = cube[i2, j2, k2], cube[i, j, k]
    return cube

def genetic_algorithm(population_size, max_iterations):
    cube_initial = generate_cube() 
    current_deviation = calculate_deviation(cube_initial)

    def generate_initial_population(population_size):
        population = []
        for _ in range(population_size):
            cube = generate_cube()
            population.append(cube)
        return population

    population = generate_initial_population(population_size)
    best_scores = []
    avg_scores = []

    start_time = time.time()

    for iteration in range(max_iterations):
        population_scores = [calculate_deviation(cube) for cube in population]
        best_scores.append(min(population_scores))
        avg_scores.append(np.mean(population_scores))
        
        if (iteration + 1) % 50 == 0:
            print(f"Iteration {iteration + 1}: Current Objective Function Value = {best_scores[-1]}")

        selected = [population[i] for i in np.argsort(population_scores)[:population_size // 2]]

        new_population = []
        for _ in range(population_size // 2):
            idx1, idx2 = np.random.choice(len(selected), 2, replace=False)
            parent1, parent2 = selected[idx1], selected[idx2]
            child = crossover(parent1, parent2)
            if np.random.rand() < 0.2:  
                child = mutate(child)
            new_population.append(child)
        
        population = selected + new_population

    end_time = time.time()

    final_population_scores = [calculate_deviation(cube) for cube in population]
    cube_final = population[np.argmin(final_population_scores)]
    print(cube_final)

    print(f"Initial Objective Function Value: {current_deviation}")
    print(f"Final Objective Function Value: {min(final_population_scores)}")
    print(f"Duration: {end_time - start_time} seconds")
    return cube_final, best_scores, avg_scores, end_time - start_time


def run_GA():
    population_sizes = []
    iteration_counts = []
    for i in range(3):
        pop_size = int(input(f"Enter population size {i + 1}: "))
        population_sizes.append(pop_size)
    for i in range(3):
        iter_count = int(input(f"Enter iteration count {i + 1}: "))
        iteration_counts.append(iter_count)

    for pop_size in population_sizes:
        for run in range(3):
            print(f"Run {run + 1} with population size: {pop_size}")
            cube, best_scores, avg_scores, duration = genetic_algorithm(pop_size, 1000)
            plt.plot(best_scores, label=f'Best - Pop {pop_size} (Run {run + 1})')
            plt.plot(avg_scores, label=f'Average - Pop {pop_size} (Run {run + 1})')
            plt.xlabel('Iterations')
            plt.ylabel('Objective Function Value')
            plt.title(f'Performance with Population Size {pop_size}')
            plt.grid(True)
            plt.legend()
            plt.show()

    for iteration_count in iteration_counts:
        for run in range(3):
            print(f"Run {run + 1} with iteration count: {iteration_count}")
            cube, best_scores, avg_scores, duration = genetic_algorithm(50, iteration_count)
            plt.plot(best_scores, label=f'Best - Iter {iteration_count} (Run {run + 1})')
            plt.plot(avg_scores, label=f'Average - Iter {iteration_count} (Run {run + 1})')
            plt.xlabel('Iterations')
            plt.ylabel('Objective Function Value')
            plt.title(f'Performance with Iteration Count {iteration_count}')
            plt.grid(True)
            plt.legend()
            plt.show()


