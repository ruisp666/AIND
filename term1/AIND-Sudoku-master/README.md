# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  

A: To solve the naked twins problem we will enforce the constraint that no
box from a unit containing a pair of naked twins can contain any of the digits
of the common value of those twins.
We do this, by iterating following steps over the units:
1) We identify the boxes that have length 2, the "candidates".
2) We identify the values that are repeated twice and to which boxes they be
long. We then make a list L containing all such possible pairs.
3) For each pair P of boxes in L with the same value v, we  iterate over the remain
ing boxes, and eliminate from its value both digits of v.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem? 
 
A:The solution process can be obtained from those demonstrated in the classes,
by adding the two diagonals as two additional units to the set of units. 
This implies the relevant peers now contain the diagonals, and as such
 he functions eliminate, only_choice,  do not need 
 additional modifications. To the reduce_puzzle we add naked_twins as an additional
 constraint.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is c ode for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

