import numpy as np
import time
from general_func import generate_cube, generate_neighbor, calculate_deviation, evaluate, plot_deviation

def steepest_ascent_hill_climbing(max_iterations=1000):
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
        best_neighbor = None
        best_neighbor_deviation = current_deviation
        
        # loop untuk mendapat nilai tetangga yang lebih baik 
        for i in range(max_iterations):
            neighbor_cube = generate_neighbor(current_cube)
            neighbor_deviation = calculate_deviation(neighbor_cube)
            
            if neighbor_deviation < best_neighbor_deviation:
                best_neighbor = neighbor_cube
                best_neighbor_deviation = neighbor_deviation
        
        # kondisi jika telah mencapai local optimum
        if best_neighbor is None or best_neighbor_deviation >= current_deviation:
            print(f"Local optimum reached at iteration {iteration}")
            break
        
        # Pindah ke tetangga yang lebih baik
        current_cube = best_neighbor
        current_deviation = best_neighbor_deviation
        
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
# steepest_ascent_hill_climbing()
