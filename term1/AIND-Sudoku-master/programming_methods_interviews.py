# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:57:37 2017

@author: sapereira
"""
import numpy as np
# Afunction to compute the number of ways to climb a flight of n steps
def climb(height):
    height1=1
    height2=2
    height3=4
    if height==1:
       # print ('There is %d way to climb the stairs.' % height)
        return height
    elif  height==2:
       # print ('There are %d ways to climb the stairs.' % height2)
        return  height2
    elif  height==3:
       # print ('There are %d ways to climb the stairs.' % height3)
        return height3
    else:
        for a in range(height-3):
            height_t= height1 + height2 + height3
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

def unique_list(l):    
    return sorted(list(frozenset(l)))

def sort_2(a,b):
    l=[a,b]
    if a>b:
        l[0]=b
        l[1]=a
    return l
            

def mergesort(l):
    if type(l)!=list:
           raise TypeError("Please, input a list.")
    else:
        sorted_list=[]
        sorted_l=[]
        sorted_r=[]
    if len(a,b)==2:
            l=[a,b]
            if a>b:
                l[0]=b
                l[1]=a
            return l
    else:
        whimerge
        if len(l)%2==0:
            centerpoint=len(l)/2
        else:
            centerpoint=len(l)/2+1
        sorted_r=mergesort(l[0:centerpoint:])
        sorted_r=mergesort(l[centerpoint+1::])
     #       mergesort(sorted_l)
      #      merge
    pass

def fibo(n):
    if type(n)!=int:
        raise TypeError("PLease input an integer")
    fibo1=1
    fibo2=1
    if n< 3:
        return fibo1
    else:
        for i in range(n-2):
            
            fibo=fibo1+fibo2
            fibo1=fibo2 
            fibo2=fibo
    return fibo

# write an algorithm for n-fibo numbers.
def F(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else: 
        return F(n-1)+F(n-2)
    
from math import sqrt
def F_alt(n):
   return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))            
    

# Exercises from Hackerrank
       
def comparethetriplets(a0, a1, a2, b0, b1, b2):
    # Complete this function
    alice=[a0,a1,a2]
    bob=[b0,b1,b2]
    alice_score=0
    bob_score=0
    for i in range(3):
        if bob[i]<alice[i]:
             bob_score+=1
        elif alice[i]< bob[i]:
            alice_score+=1
    return alice_score, bob_score      
    
def abs_diagonals(n,m):
    sum_diagonal1=0
    sum_diagonal2=0
    for i in range(n):
        sum_diagonal1+=m[i][i]
        sum_diagonal2+=m[n-i-1][n-i-1]
    return abs(sum_diagonal1 - sum_diagonal2)
    
    
column_1=[1,2,3] 
       
matrix= [[i for i in column_1] for i in range(3)]
def abs_diagonals_1(n,m):
    sum_diagonal1=0
    sum_diagonal2=0
    for row in m:
        for i in range(n):
            sum_diagonal1+=row[i]
            sum_diagonal2+=row[n-i-1]
    return abs(sum_diagonal1 - sum_diagonal2)
    


# Set the precision.




def plus_minus(n,arr):
    m_zeros=0
    m_pos=0
    for i in range(n):
        if arr[i]==0:
            m_zeros+=1
        elif arr[i]>0:
            m_pos+=1
    print("%.6f" % round(m_pos/n,6))
    print("%.6f" % round(1-(m_zeros+m_pos)/n,6))
    print("%.6f" % round(m_zeros/n,6))
    return 
               




      # Copy the arrays   
def minmax(arr):
    min_arr=min(arr)
    max_arr=max(arr)
    arr1=arr.copy()
    arr.remove(min_arr)
    arr1.remove(max_arr)

    return sum(arr1), sum(arr)

#def birthdayCakeCandles(n, ar):
#    # Complete this function
#    l=[i for i in ar if i==max(ar) if i<=n]
#    return len(l)
# USING LISTS TO FILTER BECOMES CUMBERSOME, RETURN TO SIMPLE COUNTERS
def birthdayCakeCandles(n, ar):
    # Complete this function
    max_ar=max(ar)
    c=0
    for i in ar:
        if i == max_ar:        
            c+=1
    return c

def timeConversion(s):
    # Complete this function
    hours=s[0:3]
    minutes=s[3:6]
    seconds=s[6:8]
    format_s=s[8:11]
    hours_num=int(hours[0:2])
    if format_s=='PM':
        if  int(hours_num) != 12:
            new_hours=str(hours_num+12)+ ':'
        else:
            new_hours='12:'
        new_time=new_hours + minutes + seconds
    else:
        if  int(hours_num) != 12:
            new_hours=hours
        else:
            new_hours='00:'
        new_time=new_hours + minutes + seconds
        
    return new_time


# Exercises Medium
    #   The Grid Search -implementation
    
def look_pattern1(G,R,C,P,r,c):
    '''G is the grid
    #P is the pattern to be searched for
    #r,R, c,C are as above'''
    for i in range(R-r+1):
        for j in range(C-c+1):
            sub_grid=[row[j:j+c] for row in G[i:i+r]]
            #print(sub_grid)
            if sub_grid==P:
                return 'YES'
    return 'NO'

    # Save time by breaking once it finds an element that is different from 
    #the array

     
def look_pattern(G,R,C,P,r,c):
    '''G is the grid
    #P is the pattern to be searched for
    #r,R, c,C are as above'''
     
    for i in range(R-r+1):
        for j in range(C-c+1):
            d=True
            for k in range(r):
                for l in range(c):
                    if G[i+k][j+l]!=P[k][l] :
                        d= False
                        break
                if d==False:
                    break
            if d:
                return 'YES'               
            elif i==R-r and j==C-c:
                    return 'NO'

def stringConstruction(s):
    # Complete this function
    s_l=len(s)
    c=s_l
    s_m=int(round(s_l/2,1)-1)
    for i in range(s_m,s_l):
        for j in range(0,s_l-1):
            subs=s[0:i]+s[0:i][j:s_l-i+1]
            #print(subs)
            if subs ==s and i<c:
                c=i
    return c

for i in range(3,4):
    print(i)

#for i in range(8):
#    for j in range(7):
#        if j>3:
#            break
#        print("didn't break")
#             
#        
#    print(i)

#Use of stacks is faster and more adequate
def is_matched(expression):
    dic_brackets={'{':'}','[':']','(':')'}
    matching_stack=[]
    for el in expression:
        if el in dic_brackets:
            
            matching_stack.append(el)
            #print(matching_stack)
        else:
            if not matching_stack:
                return False
            elif el==dic_brackets[matching_stack[-1]]:
                matching_stack=matching_stack[0:-1]
                #print(matching_stack)
            else:
                return False
    if len(matching_stack)>0:
        return False
    #print(matching_stack)
    return True