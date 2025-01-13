import numpy as np
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(rows, cols):
    """Create a grid with random initial states (0 or 1)."""
    return np.random.choice([0, 1], size=(rows, cols))

def count_neighbors(grid, row, col):
    """Count the number of live neighbors for a cell."""
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]:
            count += grid[r, c]
    return count

def update_grid(grid):
    """Update the grid for the next generation."""
    new_grid = np.copy(grid)
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            live_neighbors = count_neighbors(grid, row, col)
            if grid[row, col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row, col] = 0  # Cell dies
            else:
                if live_neighbors == 3:
                    new_grid[row, col] = 1  # Cell becomes alive
    return new_grid

def main():
    rows, cols = 20, 40  # Size of the grid
    grid = create_grid(rows, cols)

    try:
        while True:
            clear_console()
            print("Game of Life")
            print("-" * cols)
            for row in grid:
                print("".join(["#" if cell else " " for cell in row]))
            print("-" * cols)

            print("Press 'n' for next step or 'q' to quit.")
            user_input = input().lower()
            if user_input == 'q':
                print("Simulation stopped.")
                break
            elif user_input == 'n':
                grid = update_grid(grid)
            else:
                print("Invalid input. Please press 'n' or 'q'.")
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()