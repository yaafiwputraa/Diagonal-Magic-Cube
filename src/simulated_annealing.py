import numpy as np
import math
import time
from general_func import * 

MAGIC_SUM = 315
MAX_ITERATIONS = 70000
INITIAL_TEMPERATURE = 1000 #ini yg krusial buat diganti2
COOLING_RATE = 0.99995 #ini yg krusial buat diganti2


def simulated_annealing():
    initial_cube = generate_cube() #harus disimpen buat ditampilin di akhir
    current_cube = np.copy(initial_cube) 
    current_deviation = calculate_deviation(current_cube)
    best_cube = np.copy(current_cube)
    best_deviation = current_deviation

    temperature = INITIAL_TEMPERATURE
    start_time = time.time()

    #buat ngeplot
    deviations = []
    iterations = []
    entropies = []
    stuck_count = 0 
    

    for iteration in range(MAX_ITERATIONS):
        neighbor_cube = generate_neighbor(current_cube)
        neighbor_deviation = calculate_deviation(neighbor_cube)
        
        
        delta_e = current_deviation-neighbor_deviation
        
        
        entropy = math.exp(delta_e / temperature)
        entropies.append(entropy)

        if neighbor_deviation < current_deviation or random.random() < entropy:
            if neighbor_deviation >= current_deviation:
                stuck_count += 1 
            current_cube = neighbor_cube # ^ klo deviationnya worse masi ada kemungkinan untuk pindah ke neighbornya
            current_deviation = neighbor_deviation

            if current_deviation < best_deviation:
                best_cube = np.copy(current_cube)
                best_deviation = current_deviation
                
                
        #simpen
        deviations.append(current_deviation)
        iterations.append(iteration)

        # temperature dikurangin sesuai cooling rate
        temperature *= COOLING_RATE
        
        if best_deviation == 0:  #klo deviation uda 0 yang berarti perfect magic cube
            print("Perfect magic cube found!")
            break        

        # setiap 1000 iterasi print deviasi
        if iteration % 1000 == 0:
            print(f"Iteration {iteration}: Current deviation = {current_deviation}")
            

    # plot
    duration = time.time() - start_time
    evaluate(initial_cube,best_cube,best_deviation,duration)
    print(f"'stuck' in local optimum: {stuck_count}")
    plot_deviation(iterations, deviations, entropies)
    
# simulated_annealing()