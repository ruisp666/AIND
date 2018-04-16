# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:57:37 2017

@author: sapereira
"""

# Afunction to compute the number of ways to climb a flight of n steps
def climb(height):
    height1=1
    height2=2
    height3=4
    if height==1:
        print ('There is %d way to climb the stairs.' % height)
        return
    elif  height==2:
        print ('There are %d ways to climb the stairs.' % height2)
        return 
    elif  height==3:
        print ('There are %d ways to climb the stairs.' % height3)
        return 
    else:
        for a in range(height-3):
            height_t= 4*height1 + 2*height2 + height3
            height1=height2
            height2=height3
            height3=height_t
            print(a)
    return height_t


def reverse(s):
       
    if type(s)!=str:
           raise TypeError("Please, input a string.")
    reverse_s=''
    len_s=len(s)
    for i in range(len_s):
            reverse_s+= s[len_s-i-1]            
    return reverse_s  

#useful methods
    #s.split(',') takes eliminates the character form the string and returns
    #string
    
    
       
            


    
