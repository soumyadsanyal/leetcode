#!/bin/python3

import sys

def thecomposer(f,g):
    return lambda x: f(g(x))

def theiterator(f,n):
    if n<1:
        return lambda x: x
    elif n==1:
        return f
    else:
        return thecomposer(f,(theiterator(f,n-1)))

def spring(x):
    return 2*x

def summer(x):
    return x+1
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    temp=theiterator(thecomposer(summer, spring),max(n//2,0))(1)
    if n%2==1:
        temp=spring(temp)
    print(temp)
    #print(theiterator(thecomposer(summer, spring),max(n//2,1))(1))
