#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:22:54 2017

@author: Rui
"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import pygame
#This is so that we can exit pygame
#from sys import exit
#while True:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                exit()

import itertools
import numpy as np
assignments = []
#from collections import Counter
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units= [[a+b for a,b in list(zip(rows,cols))]] + [[ a+b for a,b in list(zip(rows[::-1],cols))]]
unitlist = row_units + column_units + square_units +diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
     #Find all instances of naked twins
     #Eliminate the naked twins as possibilities for their peers

    for subunit in unitlist:
       # Obtain the sub-dictionary containing pairs (box,values[box])
       # where  values[box] has size 2
        subunit_dic=dict((s,values[s]) for s in subunit if len(values[s]) == 2)
        # Obtain the dictionary containing filtered by twins
        twins_list=[k for k,v in subunit_dic.items() if list(subunit_dic.values()).count(v)>=2]
        #Identify all the boxes that share values of lenght 2
        #twins_set = [list(atwin) for atwin in itertools.combinations(twins_list, 2)]
        #try this which is faster:
        combs=[[[k,v] for k in twins_list] for v in twins_list ]
        combs2=[v for sublist in combs for v in sublist]
        a=np.array(combs2)
        twins_set=np.vstack({tuple(row) for row in a})
        #twins_set=list(frozenset(a))
        for atwin in twins_set:
            if values[atwin[0]]== values[atwin[1]]:
                #Eliminate from the remaining boxes of the unit, the value shared
                #by the twins
                for box in [box for box in subunit if box not in atwin]:
                    for i in values[atwin[0]]:
                        if len(values[box])>1:
                            values = assign_value(values,box, values[box].replace(i,''))
             
             
    return values


    
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value,
            then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))
    



def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value,
    eliminate this value from the values of all its peers. 
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values = assign_value(values,peer, values[peer].replace(digit,''))

    return values

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that
    only fits in one box, assign the value to this box.  (e.g you have a box
    on a certain unit '567' and the digit '7' only appears on this box. Then,
    this box ggets the '7'. )
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values,dplaces[0],digit)
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box 
    with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same,
    return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    logger.info('Running reduce_puzzle')
    #solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        #we now iterate over eliminate, only_choice, and finish with the new function
        #naked_twins
        values = eliminate(values)
        values = only_choice(values)
        values=naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    logger.info('Running search')
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    

   
    #Let us start with a box with minimal length
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, where 
    #we iterate over the digits of the s
    for digit in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = digit
        new_sudoku = assign_value(new_sudoku,s,digit)
        attempt = search(new_sudoku)
        if attempt:
            return attempt

    

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values=grid_values(grid)
    values=search(values)
    if values is None:
        logger.error('Values is none=%s',)
        return values
    return values

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    #test_case= '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    #solve(test_case)
    
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
