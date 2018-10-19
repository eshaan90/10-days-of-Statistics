#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:02:45 2018

@author: MyReservoir
"""


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

def median(X,l):
    X.sort()
    median=0
    i=int(l/2)
    if l%2==0:
        median=(X[i-1]+X[i])/2
        first=X[:i]
        last=X[i:]
    else:       
        median=X[i]
        first=X[:i]
        last=X[i+1:]
    return (median,first,last)



def main():
    
    l=int(input())
    X=input()
    X=parse_input(X)
    
    (m,first,last)=median(X,l)
    print(int(median(first,len(first))[0]))
    print(int(m))
    print(int(median(last,len(last))[0]))
    
    
if __name__=='__main__':
    main()
    