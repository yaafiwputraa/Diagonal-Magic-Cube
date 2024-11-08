import numpy as np
import random
import matplotlib.pyplot as plt

MAGIC_SUM = 315


def generate_cube():
    numbers = list(range(1, 126))
    random.shuffle(numbers)
    return np.array(numbers).reshape((5, 5, 5))

def generate_neighbor(cube):
    new_cube = np.copy(cube)
    pos1 = tuple(random.randint(0, 4) for _ in range(3))
    pos2 = tuple(random.randint(0, 4) for _ in range(3))
    while pos1 == pos2:
        pos2 = tuple(random.randint(0, 4) for _ in range(3))
    new_cube[pos1], new_cube[pos2] = new_cube[pos2], new_cube[pos1]
    return new_cube

def calculate_deviation(cube):
    total_deviation = 0
    
    def line_deviation(line_sum):
        return abs(line_sum - MAGIC_SUM)
    
    for i in range(5):
        for j in range(5):
            total_deviation += line_deviation(np.sum(cube[i, j, :])) #baris
            total_deviation += line_deviation(np.sum(cube[i, :, j])) #kolom
            total_deviation += line_deviation(np.sum(cube[:, i, j])) #pilar
    
    for i in range(5):
        total_deviation += line_deviation(np.trace(cube[i, :, :])) #trace = buat itung diagonal 
        total_deviation += line_deviation(np.trace(np.fliplr(cube[i, :, :]))) #diflip left to right, buat ngitung diagonal yg 1 ny lg
        total_deviation += line_deviation(np.trace(cube[:, i, :]))
        total_deviation += line_deviation(np.trace(np.fliplr(cube[:, i, :])))
        total_deviation += line_deviation(np.trace(cube[:, :, i]))
        total_deviation += line_deviation(np.trace(np.fliplr(cube[:, :, i])))
    
    total_deviation += line_deviation(np.trace(cube.diagonal(axis1=0, axis2=1))) #diag 0,0,0 ke 5,5,5 
    total_deviation += line_deviation(np.trace(np.fliplr(cube).diagonal(axis1=0, axis2=1))) #diag 0,0,5 ke 5,5,0
    total_deviation += line_deviation(np.trace(cube.diagonal(axis1=0, axis2=2))) #diag 0,5,0 ke 5,0,5
    total_deviation += line_deviation(np.trace(np.flipud(cube).diagonal(axis1=0, axis2=2))) #diag 0,5,5 ke 5,0,0
    
    return total_deviation

def evaluate(cube_initial, cube_final, final_obj, duration):
    # Print evaluation results
    print("Initial State:")
    print(cube_initial)
    print("\nFinal State:")
    print(cube_final)
    print(f"\nFinal Obj Func: {final_obj}")
    print(f"Duration: {duration:.3f} s")

def plot_deviation(iterations, deviations):
    plt.figure(figsize=(10, 5))
    plt.plot(iterations, deviations, label='Current Deviation', color='blue')
    plt.xlabel('Iteration')
    plt.ylabel('Deviation')
    plt.title('Plot nilai objective function terhadap banyak iterasi yang telah dilewati')
    plt.legend()
    plt.grid()
    plt.show()