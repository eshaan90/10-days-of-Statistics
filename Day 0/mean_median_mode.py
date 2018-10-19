#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:34:32 2018

@author: MyReservoir
"""

from collections import Counter

def parse_input(X):
    l=[]
    p=''
    for string in X:
        if string!=' ':
            p+=string
        else:
            l.append(int(p))
            p=''
    l.append(int(p))
    return l 


def mean(X,l):
    mean=0
    for i in range(l):
        mean+=X[i]
    return round(mean/l,1)

def median(X,l):
    X.sort()
    median=0
    if l%2==0:
        median=(X[int(l/2)-1]+X[int(l/2)])/2
    else:
        median=X[int(l/2)]
    return median

def mode(X):
    count=Counter(X)
    max=1
    mode=[]
    for num,c in count.items():
        if c>max:
            mode.append(num)
            max=c
    if max==1:
        X.sort()
        mode=X[0]
        return mode
    else:
        mode.sort()
        return mode[0]

def main():
    
    l=int(input())
    X=input()
    X=parse_input(X)
    print(mean(X,l))
    print(median(X,l))
    print(mode(X))
    
    
if __name__=='__main__':
    main()
    