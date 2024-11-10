import numpy as np
import time
import random
from general_func import generate_cube, generate_neighbor, calculate_deviation, evaluate, plot_deviation

def stochastic_hill_climbing(max_iterations=1000):
    # Inisialisasi cube 
    current_cube = generate_cube()
    initial_cube = np.copy(current_cube)
    current_deviation = calculate_deviation(current_cube)
    
    # Untuk melakukan plot_deviation
    iterations = []
    deviations = []
    
    start_time = time.time() #catat waktu mulai
    
    # loop utama
    iteration = 0
    while iteration < max_iterations:
        iterations.append(iteration) 
        deviations.append(current_deviation)
        
        # Inisialisasi tetangga terbaik
        better_neighbors = []
        
        # loop untuk mendapat nilai tetangga yang lebih baik 
        for i in range(max_iterations):
            neighbor_cube = generate_neighbor(current_cube)
            neighbor_deviation = calculate_deviation(neighbor_cube)
            
            if neighbor_deviation < current_deviation:
                better_neighbors.append((neighbor_cube, neighbor_deviation))
        
        # kondisi jika telah mencapai local optimum
        if not better_neighbors:
            print(f"local optimum reached at iteration {iteration}")
            break
        
        # Memilih secara acak tetangga yang lebih baik
        chosen_neighbor, chosen_deviation = random.choice(better_neighbors)

        current_cube = chosen_neighbor
        current_deviation = chosen_deviation
        
        # Menampilkan progress setiap 10 iterasi
        if iteration % 10 == 0:
            print(f"Iteration {iteration}: Current deviation = {current_deviation}")
        
        # kondisi jika telah ditemukan solusi
        if current_deviation == 0:
            print("Perfect magic cube found!")
            break
            
        iteration += 1 # menambah iterasi
    
    duration = time.time() - start_time
    
    # menggunakan fungsi evaluate untuk menunjukkan cube awal, cube akhir, final obj function, dan durasi
    evaluate(initial_cube, current_cube, current_deviation, duration)
    
    # melakukan plot berdasarkan iterasi dan deviasi yang telah dikumpulnkan
    plot_deviation(iterations, deviations)
    
    return current_cube, current_deviation

# menjalankan algoritma 
# stochastic_hill_climbing()
