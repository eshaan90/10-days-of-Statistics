#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:49:36 2018

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


def mean(X,W,l):
    mean=0
    weight_sum=0
    for i in range(l):
        mean+=X[i]*W[i]
        weight_sum+=W[i]
    return round(mean/weight_sum,1)

def main():
    
    l=int(input())
    X=input()
    W=input()
    X=parse_input(X)
    W=parse_input(W)
    print(mean(X,W,l))
    
    
if __name__=='__main__':
    main()
    