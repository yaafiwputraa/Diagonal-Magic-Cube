import numpy as np
import matplotlib.pyplot as plt
import time
from general_func import calculate_deviation
from general_func import generate_cube
from general_func import evaluate


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

def plot_hasil(iterations, best_scores, avg_scores, pop_size, iter_count, run):
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, best_scores, label='Best Score in Population')
    plt.plot(iterations, avg_scores, label='Average Population Score')
    plt.xlabel('Iterations')
    plt.ylabel('Objective Function')
    plt.title(f'Hasil Percobaan (Population: {pop_size}, Iterations: {iter_count}, Run: {run})')
    plt.grid(True)
    plt.legend()
    plt.show()

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
            
            for attempt in range(5):
                child = crossover(parent1, parent2)
                if not np.array_equal(child, parent1) and not np.array_equal(child, parent2): # agar child tidak sama dengan parent 1 atau 2
                    break
                else:
                    child = mutate(child)
            
            if np.random.rand() < 0.2:  
                child = mutate(child)
                # cek apakah child sam dengan kedua parent
            new_population.append(child)
        
        population = selected + new_population

    end_time = time.time()
    duration = end_time - start_time
    
    final_population_scores = [calculate_deviation(cube) for cube in population]
    best_idx = np.argmin(final_population_scores)
    cube_final = population[best_idx]
    final_score = final_population_scores[best_idx]

    print("\n" + "="*50)
    print("HASIL AKHIR")
    print("="*50)
    
    evaluate(cube_initial, cube_final, final_score, duration)
    
    return cube_initial, cube_final, best_scores, avg_scores, duration, final_score

def run_GA():
    print("=== Setup Percobaan ===")
    population_sizes = []
    iteration_counts = []
    for i in range(3):
        pop_size = int(input(f"Varian Populasi {i + 1}: "))
        population_sizes.append(pop_size)
    for i in range(3):
        iter_count = int(input(f"Varian Iterasi {i + 1}: "))
        iteration_counts.append(iter_count)

    CONTROL_ITERATIONS = 1000
    print("\n=== Experiment 1: Coba varian populasi ===")
    print(f"Iterasi yang di kontrol : {CONTROL_ITERATIONS}")
    print(f"varian populasi         : {population_sizes}")
    
    for pop_size in population_sizes:
        print(f"\nJumlah Populasi yang dites: {pop_size}")
        for run in range(3):
            print(f"\n{'-'*50}")
            print(f"Run {run + 1}/3 ukuran populasi: {pop_size}")
            print(f"{'-'*50}")
            
            cube_initial, cube_final, best_scores, avg_scores, duration, final_score = \
                genetic_algorithm(pop_size, CONTROL_ITERATIONS)
            
            iterations = list(range(CONTROL_ITERATIONS))
            plot_hasil(iterations, best_scores, avg_scores, pop_size, CONTROL_ITERATIONS, run + 1)

    CONTROL_POPULATION = 50
    print("\n=== Experiment 2: Coba varian iterasi ===")
    print(f"Populasi yang di kontrol: {CONTROL_POPULATION}")
    print(f"Varian Iterasi          : {iteration_counts}")
    
    for iteration_count in iteration_counts:
        print(f"\nJumlah Iterasi yang di test: {iteration_count}")
        for run in range(3):
            print(f"\n{'-'*50}")
            print(f"Run {run + 1}/3 with jumlah iterasi {iteration_count}")
            print(f"{'-'*50}")
            
            cube_initial, cube_final, best_scores, avg_scores, duration, final_score = \
                genetic_algorithm(CONTROL_POPULATION, iteration_count)
            
            iterations = list(range(iteration_count))
            plot_hasil(iterations, best_scores, avg_scores, CONTROL_POPULATION, iteration_count, run + 1)

run_GA()
