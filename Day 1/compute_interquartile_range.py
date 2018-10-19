#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:14:14 2018

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

def create_dataset(X,F,l):
    d={}
    for x,f in zip(X,F):
        d[x]=f
    S=[]
    for key,value in d.items():
       while value>0:
           S.append(key)
           value-=1
    return S

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
    F=input()
    X=parse_input(X)
    F=parse_input(F)
    
    S=create_dataset(X,F,l)
    (m,first,last)=median(S,len(S))
    q1=median(first,len(first))[0]
    q3=median(last,len(last))[0]
    print(float(q3-q1))
    
if __name__=='__main__':
    main()