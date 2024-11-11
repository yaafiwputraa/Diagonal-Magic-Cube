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
    duration = end_time - start_time

    
    final_population_scores = [calculate_deviation(cube) for cube in population]
    best_idx = np.argmin(final_population_scores)
    cube_final = population[best_idx]
    final_score = final_population_scores[best_idx]

    
    print("\n" + "="*50)
    print("RESULTS")
    print("="*50)
    
    # Print initial state
    print("\nINITIAL STATE:")
    print("-"*20)
    for i in range(5):
        print(f"\nLayer {i+1}:")
        print(np.array2string(cube_initial[i], separator=' ', precision=2))
    print(f"\nInitial Objective Function Value: {current_deviation}")
    
    # Print final state
    print("\nFINAL STATE:")
    print("-"*20)
    for i in range(5):
        print(f"\nLayer {i+1}:")
        print(np.array2string(cube_final[i], separator=' ', precision=2))
    print(f"\nFinal Objective Function Value: {final_score}")
    
    print(f"\nDuration: {duration:.2f} seconds")
    print("="*50)
    
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

    
    CONTROL_ITERATIONS = 1000 # iterasi yg di control
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
            
            
            plt.figure(figsize=(10, 6))
            plt.plot(best_scores, label='Best Scores')
            plt.plot(avg_scores, label='Average Scores')
            plt.xlabel('Iterations')
            plt.ylabel('Objective Function Value')
            plt.title(f'Plot nilai objective function terhadap banyak iterasi yang telah dilewati (Populasi) {pop_size} (Run {run + 1})')
            plt.grid(True)
            plt.legend()
            plt.show()

    
    CONTROL_POPULATION = 50 # populasi yg di control
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
            
            
            plt.figure(figsize=(10, 6))
            plt.plot(best_scores, label='Best Scores')
            plt.plot(avg_scores, label='Average Scores')
            plt.xlabel('Iterations')
            plt.ylabel('Objective Function Value')
            plt.title(f'Plot nilai objective function terhadap banyak iterasi yang telah dilewati (Iterasi) {iteration_count} (Run {run + 1})')
            plt.grid(True)
            plt.legend()
            plt.show()
