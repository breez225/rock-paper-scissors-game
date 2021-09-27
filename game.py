#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 19:37:06 2021

@author: brilabanti
"""

# this is the "game.py" file...

# '''name = input ("Enter your Name: ")

# print("Welcome:" + name )'''

print("Rock, Paper, Scissors, Shoot!") 

import random 

import os 

from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")

print(x, "This is the one and only Rock, Paper, or Sciccors")

user_choice = input("rock, paper, or sciccors you choose: ")

print("What is your name:" +user_choice)

options = ["rock", "paper", "sciccors"]

computer_choice = random.choice(options)

print("The computer chose: " +computer_choice) 

if user_choice == computer_choice:
    print("Draw, you're lucky... or are you, try your luck again")
    
    print("Please play again")
        
elif user_choice == "rock" and computer_choice == "sciccors" :
            
            print("You win! Can you do it again though?") 
            
            print("please play again")
            
elif user_choice == "paper" and computer_choice == "sciccors" :
            
            print("haha, computer wins!")
            
            print("please play again")
            
elif user_choice == "paper" and computer_choice == "rock" :
            
            print("You win! Can you do it again though?")
            
            print("please play again")
            
elif user_choice == "sciccors" and computer_choice == "rock" :
            
            print("haha, computer wins!")
            
            print("please play again")
            
elif user_choice == "rock" and computer_choice == "paper" :
            
            print("You win! Can you do it again though?")
            
            print("please play again")
            
            print("You win! Can you do it again though?")
            
            print("please play again")