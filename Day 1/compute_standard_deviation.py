#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:31:15 2018

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


def compute_mean(X,l):
    mean=0
    for i in range(l):
        mean+=X[i]
    return round(mean/l,1)

def compute_std(X, l, mean):
    std=0
    for i in range(l):
        std+=(X[i]-mean)**2
    return round((std/l)**0.5,1)

def main():
    
    l=int(input())
    X=input()
    X=parse_input(X)
    
    mean=compute_mean(X, l)
    print(compute_std(X, l, mean))
    
    
if __name__=='__main__':
    main()
    
    