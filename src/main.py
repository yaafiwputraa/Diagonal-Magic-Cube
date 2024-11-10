import sys
from genetic_algorithm import run_GA
from random_restart import random_restart_hill_climbing
from sideways import hill_climbing_with_sideways
from simulated_annealing import simulated_annealing
from steepest_ascent import steepest_ascent_hill_climbing
from stochastic import stochastic_hill_climbing

def main():
    print("Choose an algorithm to run:")
    print("1. Genetic Algorithm")
    print("2. Random Restart Hill Climbing")
    print("3. Sideways Hill Climbing")
    print("4. Simulated Annealing")
    print("5. Steepest Ascent Hill Climbing")
    print("6. Stochastic Hill Climbing")
    
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        run_GA()
    elif choice == '2':
        random_restart_hill_climbing()
    elif choice == '3':
        hill_climbing_with_sideways()
    elif choice == '4':
        simulated_annealing()
    elif choice == '5':
        steepest_ascent_hill_climbing()
    elif choice == '6':
        stochastic_hill_climbing()
    else:
        print("Invalid choice. Please restart and choose a valid option.")
        sys.exit()

if __name__ == "__main__":
    main()
