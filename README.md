# Game of Life Noah_Assedou CDOF4

## Project Description
The **Game of Life** is a cellular automaton devised by mathematician John Horton Conway. This console-based implementation uses `#` to represent live cells and spaces to represent dead cells. Each generation evolves based on the states of its neighboring cells, following Conway's rules:

1. A live cell with fewer than two live neighbors dies (underpopulation).
2. A live cell with two or three live neighbors survives.
3. A live cell with more than three live neighbors dies (overpopulation).
4. A dead cell with exactly three live neighbors becomes a live cell (reproduction).

This project serves as an introduction to creating and contributing to open-source projects.

## How to Run the Project

### Prerequisites
- Python 3.7 or higher

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/game_of_life-noah-CDOF4.git
   cd game_of_life-noah-CDOF4
   ```
2. Run the program:
   ```bash
   python game_of_life.py
   ```

The simulation will start in the terminal, and you can exit by pressing `Ctrl + C`.

## License
This project is licensed under the [MIT License](LICENSE).
