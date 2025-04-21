import numpy as np
import os

def clear_console():
    """
    Clears the console screen.
    Works for both Windows (cls) and Unix-based systems (clear).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(rows, cols, predefined_grid=None):
    """
    Creates a grid with the specified number of rows and columns.
    Each cell is randomly assigned a value of 0 (dead) or 1 (alive).

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.

    Returns:
        np.ndarray: A 2D NumPy array representing the grid.
    """
    if predefined_grid is not None:
        grid = np.array(predefined_grid)
        assert grid.shape == (rows, cols), "Predefined grid shape mismatch!"
        return grid
    else:
        return np.random.choice([0, 1], size=(rows, cols))

def count_neighbors(grid, row, col):
    """
    Counts the number of live (1) neighbors for a cell at a given position.

    Args:
        grid (np.ndarray): The grid representing the current state of the game.
        row (int): Row index of the cell.
        col (int): Column index of the cell.

    Returns:
        int: The number of live neighbors.
    """
    # Define relative positions of the 8 possible neighbors
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),     # Top-left, Top, Top-right
        (0, -1),          (0, 1),       # Left,       Right
        (1, -1), (1, 0), (1, 1)         # Bottom-left, Bottom, Bottom-right
    ]
    count = 0
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        # Check if the neighbor is within bounds and count it if alive
        if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]:
            count += grid[r, c]
    return count

def update_grid(grid):
    """
    Updates the grid to the next generation based on Conway's Game of Life rules.

    Rules:
        1. Any live cell with fewer than 2 live neighbors dies (underpopulation).
        2. Any live cell with 2 or 3 live neighbors survives.
        3. Any live cell with more than 3 live neighbors dies (overpopulation).
        4. Any dead cell with exactly 3 live neighbors becomes alive (reproduction).

    Args:
        grid (np.ndarray): The current state of the grid.

    Returns:
        np.ndarray: The updated grid for the next generation.
    """
    new_grid = np.copy(grid)                                        # Create a copy of the current grid to update
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            live_neighbors = count_neighbors(grid, row, col)
            if grid[row, col] == 1:                             # Cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row, col] = 0                          # Cell dies
            else:                                               # Cell is dead
                if live_neighbors == 3:
                    new_grid[row, col] = 1                          # Cell becomes alive
    return new_grid

def main():
    """
    Main function to run the Game of Life simulation.
    Initializes the grid and updates it based on user input.
    """
    rows, cols = 5, 5  # petit exemple pour clarté

    # Exemple de grille prédéfinie (glider pattern)
    predefined_grid = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    # Initialiser avec grille prédéfinie ou aléatoire selon choix utilisateur
    choice = input("Use predefined grid? (y/n): ").lower()
    if choice == 'y':
        grid = create_grid(rows, cols, predefined_grid)
    else:
        grid = create_grid(rows, cols)    # Create the initial grid

    try:
        while True:                     # Infinite loop to keep the simulation running
            clear_console()             # Clear the console for a clean display
            print("Game of Life")       # Print the title
            print("-" * cols)           # Print a horizontal separator

            # Print the grid, using '#' for live cells and ' ' for dead cells
            for row in grid:
                print("".join(["#" if cell else " " for cell in row]))
            
            print("-" * cols)           # Print another horizontal separator

            print("Press 'n' for next step or 'q' to quit.")
            user_input = input().lower()    # Get user input
            if user_input == 'q':
                print("Simulation stopped.")
                break                       # Exit the loop and end the program
            elif user_input == 'n':
                grid = update_grid(grid)    # Update the grid to the next generation
            else:
                print("Invalid input. Please press 'n' or 'q'.")
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
