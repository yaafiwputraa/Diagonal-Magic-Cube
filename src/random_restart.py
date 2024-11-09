import numpy as np
import time
from general_func import generate_cube, generate_neighbor, calculate_deviation, evaluate, plot_deviation

def random_restart_hill_climbing(max_iterations=1000, max_restart=5):
    best_cube = None
    best_deviation = float('inf')
    
    # Untuk melakukan plot_deviation
    iterations = []
    deviations = []
    
    # Melakukan tracking terhadap iterasi tiap restart
    attempt_iterations = []
    
    start_time = time.time()
    restart_count = 0
    total_iterations = 0

    # Loop untuk restart
    while restart_count <= max_restart:  
        if restart_count == 0:
            print("\nInitial attempt")
        else:
            print(f"\nRestart {restart_count}")
        
        # Inisialisasi cube baru untuk setiap percobaan
        current_cube = generate_cube()
        if restart_count == 0:
            initial_cube = np.copy(current_cube)
            
        current_deviation = calculate_deviation(current_cube)
        local_iterations = 0
        
        # loop utama untuk setiap percobaan
        while local_iterations < max_iterations:
            iterations.append(total_iterations)
            deviations.append(current_deviation)
            
            # Inisialisasi tetangga terbaik
            best_neighbor = None
            best_neighbor_deviation = current_deviation
            
            # loop untuk mendapat nilai tetangga yang lebih baik 
            for _ in range(max_iterations):
                neighbor_cube = generate_neighbor(current_cube)
                neighbor_deviation = calculate_deviation(neighbor_cube)
                
                if neighbor_deviation < best_neighbor_deviation:
                    best_neighbor = neighbor_cube
                    best_neighbor_deviation = neighbor_deviation
            
            # kondisi jika telah mencapai local optimum
            if best_neighbor is None or best_neighbor_deviation >= current_deviation:
                if restart_count == 0:
                    print(f"Local optimum reached at iteration {local_iterations} (initial attempt)")
                else:
                    print(f"Local optimum reached at iteration {local_iterations} (restart {restart_count})")
                break
            
            # Pindah ke tetangga yang lebih baik
            current_cube = best_neighbor
            current_deviation = best_neighbor_deviation
            
            # Mengubah nilai terbaik jika ditemukan deviasi lebih rendah
            if current_deviation < best_deviation:
                best_cube = np.copy(current_cube)
                best_deviation = current_deviation
            
            # Menampilkan progress setiap 10 iterasi
            if local_iterations % 10 == 0:
                print(f"Iteration {local_iterations}: Current deviation = {current_deviation}")
            
            # kondisi jika telah ditemukan solusi
            if current_deviation == 0:
                print("Perfect magic cube found!")
                attempt_iterations.append(local_iterations + 1)
                duration = time.time() - start_time
                
                # Memberikan output dari search yang telah dilakukan
                print("\nSearch Summary:")
                print(f"Number of restarts: {restart_count}")  # Not counting first attempt
                print("Initial attempt:", attempt_iterations[0], "iterations")
                if len(attempt_iterations) > 1:
                    print("Iterations per restart:", attempt_iterations[1:])
                    print(f"Average iterations per restart: {sum(attempt_iterations[1:]) / len(attempt_iterations[1:]):.2f}")
                
                # menggunakan fungsi evaluate untuk menunjukkan cube awal, cube akhir, final obj function, dan durasi
                evaluate(initial_cube, best_cube, best_deviation, duration)
                
                # melakukan plot berdasarkan iterasi dan deviasi yang telah dikumpulnkan
                plot_deviation(iterations, deviations)
                
                return best_cube, best_deviation
                
            local_iterations += 1
            total_iterations += 1
            
        # Record iterations for this attempt
        attempt_iterations.append(local_iterations)
        restart_count += 1
        
    duration = time.time() - start_time
    
    # Memberikan output dari search yang telah dilakukan
    print("\nSearch Summary:")
    print(f"Number of restarts: {restart_count - 1}")  
    print("Initial attempt:", attempt_iterations[0], "iterations")
    print("Iterations per restart:", attempt_iterations[1:])
    if len(attempt_iterations) > 1:
        print(f"Average iterations per restart: {sum(attempt_iterations[1:]) / len(attempt_iterations[1:]):.2f}")
    
    # menggunakan fungsi evaluate untuk menunjukkan cube awal, cube akhir, final obj function, dan durasi
    evaluate(initial_cube, best_cube, best_deviation, duration)
    
    # melakukan plot berdasarkan iterasi dan deviasi yang telah dikumpulnkan
    plot_deviation(iterations, deviations)
    
    return best_cube, best_deviation

# menjalankan algoritma 
random_restart_hill_climbing()