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
unitlist = row_units + column_units + square_units
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
    values_m=values.copy()
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    #size_two_values = [box for box in values.keys() if len(values[box]) == 2]
    #for peer in peers[box]:
    #i=0
    for subunit in unitlist:
        #print(subunit)
        #i=+1
        subunit_dic=dict((s,values[s]) for s in subunit)
        #unit_values=[values[box] for box in subunit if len(values[box]) == 2]
        #unit_boxes= [box for box in subunit if len(values[box]) == 2]
        #unit_twins_values= [i for i in unit_values if unit_values.count == 2]
        #for i,item in enumerate(mylist):
    #D[item].append(i)
        #unit_twice = {k:v for k,v in subunit_values.items() if len(v)==2} 
        #unit_twice_vals= [v for v in unit_twice.values()]
        twins_dic={k:v for k,v in subunit_dic.items() if list(subunit_dic.values()).count(v)>1}
        #for key, value in D.items():
         #   if vals.count(value) > 1:
          #     unit_twins.append(key)
        #print(unit_twice)
       # print(unit_twice_vals)
       

        #print(twins_dic)
        #print('\n')
        
       # print(dict((s,int(values[s])) for s in subunit), unit_boxes, unit_twins_values)
        #print(subunit, unit_twins_values)
        #twins=dict((s, values[s]) for s in unit_boxes if values[s] in unit_twins_values )  
        if bool(twins_dic):
            #for box in [box for box in subunit if box not in list(twins_dic.keys())]:
             #for i in list(twins_dic.values())[0]:
                   #values[] = values[box].replace(i,'')
           to_del= list(twins_dic.values())[0]
           for box in [box for box in subunit if box not in list(twins_dic.keys())]:
             for i in to_del:
                   values_m[box] = values_m[box].replace(i,'')
#             
#             for box in list(twins_dic.keys()): 
#                for peer in peers[box]:
#                    for i in to_del:
#                        if len(values[peer])>1:
#                            #print(values[peer])
#                            values[peer] = values[peer].replace(i,'')
               #print("some change")
    return values_m
    
def cross(A, B):
    "Cross product of elements in A and elements in B."
    pass

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    pass

#    def display(values):
#        """
#        Display the values as a 2-D grid.
#        Args:
#            values(dict): The sudoku in dictionary form
#        """
#        pass

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
    pass

def only_choice(values):
    pass

def reduce_puzzle(values):
    pass

def search(values):
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
