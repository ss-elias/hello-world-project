# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 21:55:53 2021

@author: Sneha
"""



print("if u want to play, type 'yes'...To exit the game type 'no'.")
l=["stone","paper","scissors"]
import random
def sps(n):
    c_sc=0
    u_sc=0
    i=1
    while c_sc<n and u_sc<n:
        print("enter your ",i,"th","choice")
        u_ch=input("enter your choice: ")
        c_ch=random.choice(l)
        print("---------------------------")
        print("you chose: ",u_ch)
        print("computer chose: ",c_ch)
        i=i+1
        if c_ch=="paper" and u_ch=="stone" or c_ch=="stone" and u_ch=="scissors" or c_ch=="scissors" and u_ch=="paper":
            print("computer scores!")
            c_sc=c_sc+1
            print("your score: ",u_sc,"out of ",n)
            print("computer's score: ",c_sc,"out of ",n)
        if u_ch=="paper" and c_ch=="stone" or u_ch=="stone" and c_ch=="scissors" or u_ch=="scissors" and c_ch=="paper":
            print("you score!")
            u_sc=u_sc+1
            print("your score: ",u_sc,"out of ",n)
            print("computer's score: ",c_sc,"out of ",n)
        if u_ch==c_ch:
            print("its a draw!")
            print("your score: ",u_sc,"out of ",n)
            print("computer's score: ",c_sc,"out of ",n)
        if u_ch not in l or c_ch not in l:
            print("incorrect option is entered")
            continue
        if u_sc==n or c_sc==n:
            break
        if u_sc=="exit":
            break
    if u_sc==n:
        print("you won!")
        print("your final score: ",u_sc,"out of",n)
        print("computer's final score: ",c_sc,"out of",n)
    if c_sc==n:
        print("computer won!")
        print("your final score: ",u_sc,"out of",n)
        print("computer's final score: ",c_sc,"out of",n)
        print("BETTER LUCK NEXT TIME")
#main
dec=input("Do you want to play? ")
if dec=="yes" or dec=="YES" or dec=="Yes":
    max_score=int(input("enter the maximum score: "))
    if max_score<=0:
        print("ENTER A NUMBER GREATER THAN  0")
    else:
        sps(max_score)   
if dec=="no" or dec=="NO" or dec=="No":
    print("BYE!")
    



