# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:03:45 2017

@author: A01439768
"""

import random

def print_header():
    print("\tWelcome to 'Guess My Number'!")
    print("\tI'm thinking of a number between 1 and 100.")
    print("\tTry to guess it in as few attempts as possible.\n")

def print_footer(the_number, tries):
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")
    print("\n\nPress the enter key to exit.")  
    
    
    
def main():
    # print the greeting banner
    print_header()
    
    # set the initial values
    the_number = random.randint(1, 100)

    

    
    # initialize the first upper and lower limit, firstGuess
    lowerLimit = 1
    upperLimit = 100
    guess = 50
    tries = 1
    
    
    while guess != the_number:
        if guess > the_number:
            print("Lower ...")
            lowerLimit = lowerLimit
            upperLimit = guess
            guess = (lowerLimit + guess)//2
            
            
        else:
            print("Higher...")
            lowerLimit = guess
            upperLimit = upperLimit
            guess = (upperLimit + guess)//2
            

        tries += 1
        
    print_footer(the_number, tries)

    
     
    
    
if __name__ == "__main__":
    main()