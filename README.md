# Sudoku Project
MUIC ICCS205 Numerical Computation

# Sudoku

A popular number game/puzzle whose objective is to fill each of the empty cells in a grid with the correct number using the given initial clues.

https://user-images.githubusercontent.com/60769071/162630449-3963b3ec-a6d1-4903-9eda-d890c7629fe6.mp4

# Solving Sudoku using Linear Optimization
Unlike a normal linear optimization problem, the problem of sudoku puzzle does not have an objective function to be optimized because there is no better, or worse, solution. So, as long as the solution does not violate the constraints, the solution is valid. As for the decision variables, we utilize the 3-dimensional binary grid to represent all the combination of the value, row, and column, which in turn help us with the constraints where the constraints are as follows.
1. Each row must contain the numbers without repetitions
2. Each column must contain the numbers without repetitions
3. Each block must contain the numbers without repetitiions
4. Each cell must contain only one number
5. Each cell in the 3-dimensional grid must be either 0 or 1
6. Each initial clue must be fixed

<b> Note: </b> Please see sudoku.ipynb for more details.

# Repository Files
```
# python file for basic demo/showcase
- main.py
# python file for importing modules from jupyter notebook
- notebook_getter.py
# jupyter notebook: the main part of the project
- sudoku.ipynb
```

# Project Setup
```
Python 3.9.7 
   
Package Requirements
   -  streamlit
   -  cvxpy
   -  cvxopt
   -  numpy
```

# Run
Please run main.py to start a basic webapp for project demo.
```
streamlit run main.py
```
The main.py can also be run from the file itself (Recommended).

<b> Note: </b> The current working directory <b> must be </b> where the files are located.
