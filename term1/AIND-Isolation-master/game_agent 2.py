"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.disabled = True
#import math
class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass
import math

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    #raise NotImplementedError
    
    # 
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - 0.5*opp_moves)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(0.5*own_moves -opp_moves)
    
    


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    blank_spaces_n=len(game.get_blank_spaces())
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    
    #own_moves = len(game.get_legal_moves(player))
    #opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    #return float(0.5*own_moves -opp_moves)
    
    w_own_moves=own_moves/(opp_moves+ own_moves)
    if blank_spaces_n <= 30:
        return float(own_moves*w_own_moves - math.sqrt(30/blank_spaces_n)*(1- w_own_moves)*opp_moves)
    else:
        return float(own_moves*w_own_moves - ((1- w_own_moves)*opp_moves))
        
        
    
    
    
     



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return best_move
        best_move= legal_moves[0]
      

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move
    
    """ We implement the 3 helper methods terminal_test, max_val, and min_val
    in a similar way as in  the mini-project. We change syntax in order to make 
    them class methods.
    """
             
    
    
    def terminal_test(self,game):
        """ Return True if the game is over for the active player
        and False otherwise.
        
        Parameters
        
        ----------------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
                
        """
        #if self.time_left() < self.TIMER_THRESHOLD:
         #   raise SearchTimeout()   
            
        return not bool(game.get_legal_moves()) 

    def min_value(self,game,depth_level):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()   
            
        test_terminal=self.terminal_test(game)
        if test_terminal==True:
            #logging.info("Game is over while searching.")
            return 1
        #logging.info("Searching at level %d..." %game.move_count )
        v=float("inf")
        if game.move_count==depth_level-1:
         #   logging.info("minimizing over last depth..." )
            v, move = min([(self.score(game.forecast_move(m),self), m) 
                    for m in game.get_legal_moves()])
            return v
        else:
            v, move = min([(self.max_value(game.forecast_move(m),depth_level), m) 
                    for m in game.get_legal_moves()])
            return v         
    

    def max_value(self,game,depth_level):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
#        if self.time_left() < self.TIMER_THRESHOLD:
#            raise SearchTimeout()
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()   
            
        test_terminal=self.terminal_test(game)
        if test_terminal==True:
          #  logging.info("Game is over while searching.")
            return -1
        v=float("-inf")
        if game.move_count==depth_level-1:
           # logging.info("maximizing over last depth..." )
            v, move = max([(self.score(game.forecast_move(m),self), m) 
                    for m in game.get_legal_moves()])
            return v
        else:
            v, move = max([(self.min_value(game.forecast_move(m),depth_level), m) 
                    for m in game.get_legal_moves()])
            return v       
            
          
                  

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()         
        
        start_level=game.move_count
        #logging.info("Initial move_count is %d" %start_level)
        #legal_moves = game.get_legal_moves()
        #if not legal_moves:
         #   return (-1, -1)
        #best_move=legal_moves[0]
        if depth==1:
           _, move= max([(self.score(game.forecast_move(m),self), m) 
                    for m in game.get_legal_moves()])
           return move
        else:
            
                return max(game.get_legal_moves(),
            key=lambda m: self.min_value(game.forecast_move(m),depth+start_level))
                
          

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
        #raise NotImplementedError
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return best_move
        i=1
        

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            while self.time_left() >= self.TIMER_THRESHOLD:
                best_move=  self.alphabeta( game, i)
                i+=1

        except SearchTimeout:
            pass
            
      # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move   
            
        
        
        
        """ We implement the helper methods max_val, and min_val to take into 
        consideration the pruning.
        """
             
    
    
    def terminal_test(self,game):
        """ Return True if the game is over for the active player
        and False otherwise.
        
        Parameters
        
        ----------------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
                
        """
        #if self.time_left() < self.TIMER_THRESHOLD:
         #   raise SearchTimeout()   
            
        return not bool(game.get_legal_moves()) 
    
    def cutoff_test(self,game,d):
        """ Return True if the game is over for the active player
        and False otherwise.
        
        Parameters
        
        ----------------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
                
        """
        #if self.time_left() < self.TIMER_THRESHOLD:
         #   raise SearchTimeout()   
            
        return  game.move_count>d
    
    

    def min_value_alphabeta(self,game,depth_level,alpha,beta,depth_cut):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes, after pruning.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()   
        if depth_level >= depth_cut:
            return self.score(game,self)
        if  self.terminal_test(game):

            logging.info("Game is over while searching.")
            return 1
#            for move in game.get_legal_moves():
#                v = min(v,self.score(game.forecast_move(move),self))
#                if v<= alpha:
#                    return v
#                beta=min(beta,v)
#            return v
#               
#           
#        logging.info("Alpha-beta searching at level %d..." %game.move_count )
#        
        v=float("inf")
        for move in game.get_legal_moves():
               v= min(v,self.max_value_alphabeta(game.forecast_move(move),depth_level+1,alpha,beta,depth_cut))
               if v <= alpha:
               #In a minimizer node, if v is smaller than alpha, the minimizer
               # will always choose a value that is at most that value. Since
               #This value is smaller than alpha, the maximizer will not choose
               #that brunch. Thus it will be pruned.
                   return v
               #When there is no pruning, we try to look for children where
               #the value is minimized.
               beta=min(beta,v)
               
        return v   
                
    

    def max_value_alphabeta(self,game,depth_level, alpha,beta,depth_cut):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes, ater pruning.
        """

        #if self.time_left() < self.TIMER_THRESHOLD:
         #   raise SearchTimeout()   
        
        if depth_level >= depth_cut :
            return self.score(game,self)
        if self.terminal_test==True:
            logging.info("Game is over while searching.")
            return -1
        logging.info("Alpha-beta searching at level %d..." %game.move_count )    
            
            
       
        
#        if game.move_count==depth_level-1:
#            logging.info("maximizing over last depth..." )
#            for move in game.get_legal_moves():    
#                v= min(v,self.score(game.forecast_move(move),self))
#                if v >= beta: 
#           #In a maximizer node, if b is bigger than beta, the maximizer
#           # choose a value that is at least beta. Being bigger than beta,
#           #the minimizer will then never choose this brunch.
#                   return v
#           #When there is no pruning, we try to look for a child with better
#           #than our previous value.
#                alpha=max(alpha,v)
#            return v
#        else:
#            
        v=float("-inf")
        for move in game.get_legal_moves():
           v = max(v,self.min_value_alphabeta(game.forecast_move(move),depth_level+1,alpha,beta,depth_cut))
           if v >= beta:
           #In a maximizer node, if b is bigger than beta, the maximizer
           # choose a value that is at least beta. Being bigger than beta,
           #the minimizer will then never choose this brunch.
               return v
           #When there is no pruning, we try to look for a child with better
           #than our previous value.
           alpha=max(alpha,v)
              
           return v    
       
        
    def max_value1(self,game, alpha, beta, current_depth,depth_cutoff):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout() 
        if current_depth == depth_cutoff:
            #print(self.score(game,self))
         #   logging.info("Calculating Heuristic")
            #return self.score(game,self)
            return self.score(game,self)
             
        if self.terminal_test==True:
          #  logging.info("Game is over while searching.")
            return -1
        v = float("-inf")
        for move in game.get_legal_moves():
           # logging.info("maximizing for depth %d." %current_depth)
            v = max(v, self.min_value1(game.forecast_move(move), alpha, beta, current_depth+1, depth_cutoff))
            if v >= beta:
            #    logging.info("beta-prunning at %s" %(move,))
                return v
            alpha = max(alpha, v)
        return v

    def min_value1(self,game ,alpha, beta, current_depth, depth_cutoff):
        if self.time_left() < self.TIMER_THRESHOLD:
           raise SearchTimeout() 
        if current_depth == depth_cutoff:
            #logging.info("Calculating Heuristic")
            #return self.score(game,self)
            return self.score(game,self)
        if self.terminal_test==True:
            #logging.info("Game is over while searching.")
            return 1
        v = float("inf")
        for move in game.get_legal_moves():
            #logging.info("minimizing for depth %d." %(current_depth+1))
            #print(self.max_value1(game.forecast_move(move,alpha, beta, current_depth+1, depth_cutoff)))
            v = min(v, self.max_value1(game.forecast_move(move), alpha, beta, current_depth+1, depth_cutoff))
            if v <= alpha:
             #   logging.info("alpha-prunning at %s" %(move,))
                return v
            beta = min(beta, v)
        return v
   


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
            
       

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state
       # cutoff_test = (lambda game,depth_cut:  depth_cut > depth or self.terminal_test(game))
       # eval_fn = self.score or (lambda game, active_player: game.utility(game.active_player))    
        
#        start_level=game.move_count
#        
#        logging.info("Initial move_count is %d" %start_level)
#        if depth==1:
##           _, move= max([(self.score(game.forecast_move(m),self), m) 
##                    for m in game.get_legal_moves()])
##           
##           return move
#            logging.info("Depth is one")
#            best_move=None
#            best_score=float("-inf")
#            for m in game.get_legal_moves():
#                v = self.score(game.forecast_move(m),self)
#                if v > best_score:
#                    best_score = v
#                    best_move = m
#                if best_score >= beta:
#                        return best_move
#                alpha=max(alpha,v)
#            return best_move
#        else:
#        if depth==1:
#            logging.info("Depth is one")
#            best_move=None
#            best_score=float("-inf")
#            for m in game.get_legal_moves():
#                v = self.score(game.forecast_move(m),self)
#                if v > best_score:
#                    best_score = v
#                    best_move = m
#                if best_score >= beta:
#                        return best_move
#                alpha=max(alpha,v)
#            return best_move
#           
#        else:
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        best_move=legal_moves[0]
        best_score=alpha
        for m in legal_moves:
            v = self.min_value1(game.forecast_move(m),  best_score, beta, 1, depth)
            if v > best_score:
                best_score = v
                best_move = m
        return best_move
            
            
            
            
            
            
            
            
#            logging.info("Depth is bigger than one")
            #return max(game.get_legal_moves(),
             # key=lambda m: self.min_value1(game.forecast_move(m),alpha,beta,0,depth))
            
#            return max(game.get_legal_moves(),
 #           key=lambda m: self.min_value_alphabeta(game.forecast_move(m),0,alpha,beta,depth))
##            v=float("-inf")
       
#            v= max(v,self.min_value_alphabeta(game.forecast_move(move),depth + start_level,alpha,beta))
#            if v >= beta:
#               #In a maximizer node, if b is bigger than beta, the maximizer
#               # choose a value that is at least beta. Being bigger than beta,
#               #the minimizer will then never choose this brunch.
#                  return v
#               #When there is no pruning, we try to look for a child with better
#               #than our previous value.
#            alpha=max(alpha,v)
#              
#        return v  
#        best_move=None
#        best_score=float("-inf")
#        for m in game.get_legal_moves():
#            v = self.min_value1(game.forecast_move(m),alpha,beta,0,depth)
#            if v > best_score:
#                best_score = v
#                best_move = m
#            if best_score >= beta:
#           #In a maximizer node, if b is bigger than beta, the maximizer
#           # choose a value that is at least beta. Being bigger than beta,
#           #the minimizer will then never choose this brunch.
#               return best_move
#            alpha=max(alpha,v)   
#        return best_move
#    

              
        
        #legal_moves=game.get_legal_moves()
        #return legal_moves[0]
        # TODO: finish this function!
        #raise NotImplementedError
