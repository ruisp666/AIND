# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:28:01 2017

@author: sapereira
"""
#from game_agent import MinimaxPlayer
from game_agent import  AlphaBetaPlayer
from isolation import Board
#import isolation
#import game_agent

player1=AlphaBetaPlayer()
player2=AlphaBetaPlayer()
game = Board(player1, player2)
game.apply_move((2, 3))
game.apply_move((0, 5))
print(game.to_string())
assert(player1 == game.active_player)
print(game.get_legal_moves())
player1.terminal_test(game)
game.move_count
game.play()

player1.alphabeta( game, 1)