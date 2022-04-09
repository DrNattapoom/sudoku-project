from notebook_getter import NotebookFinder
import sys
import subprocess
import pkg_resources

required = { "streamlit", "cvxpy", "cvxopt", "numpy" }
installed = { pkg.key for pkg in pkg_resources.working_set }
missings = required - installed

if missings: subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missings], stdout = subprocess.DEVNULL)

sys.meta_path.append(NotebookFinder())

from sudoku import Sudoku
from streamlit import cli as stcli
import streamlit as st
import numpy as np

@st.cache(allow_output_mutation=True)
def get_sudoku(n):
    return Sudoku(n)

def get_sudoku_board_html(board):
    n = len(board)
    sqrt_n = (int) (np.sqrt(n))
    board_html = "<div align = 'center' style = 'margin: 30px'><table>"
    for i in range(n):
        if (i % sqrt_n == 0):
            board_html += "<tbody>"
        board_html += "<tr>"
        for j in range(n):
            board_html += "<td>" if (j % sqrt_n != 0) else "<td style = 'border-left: solid medium'>"
            if (board[i][j] != 0):
                board_html += str(board[i][j])
            else:
                id = f"'{i},{j}'"
                board_html += f"<input id = {id} type = 'text' style = 'width: 100%; text-align: center; color: white; background-color: transparent; border: none;'>"
            board_html += "</td>"
        board_html += "</tr>"
    board_html += "</table></div>"
    return board_html

def solve(sudoku):
    return sudoku.solve_linear_optimization()

def main():
    st.title("ICCS205 Numerical Computation: Sudoku Project")
    st.caption("Presented by Nattapoom Dumronglaohapun")
    if (st.button("New Puzzle")):
        st.legacy_caching.clear_cache()
    sudoku = get_sudoku(9)
    puzzle = sudoku.puzzle
    board_html = get_sudoku_board_html(puzzle)
    style = '''
        <style>
            table { width: 65%; }
            tbody { border: solid medium; }
            td { border: solid thin; height: 1.4em; width: 1.4em; text-align: center; padding: 0; }
        </style>
    '''
    st.markdown(style + board_html, unsafe_allow_html = True)
    if st.button("Solve"):
        solution = solve(sudoku)
        st.markdown(get_sudoku_board_html(solution), unsafe_allow_html = True)

if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
