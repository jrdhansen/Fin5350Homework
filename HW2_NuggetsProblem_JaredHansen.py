# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:31:22 2017

@author: A01439768
"""

# This function is where we've actually abstracted the work to.
# It checks to see if a candidate number is some linear combination
# of the different quantities that nuggets come in: 6,9,20.
# We do this by using nested for-loops

def isNuggetNumber (candidate, small=6, medium=9, large=20):
    for i in range(candidate//small +1 ):
        for j in range(candidate//medium + 1):
            for k in range(candidate//large + 1):
                if(small*i + medium*j + large*k == candidate):
                    return True
    return False



# In our main function we use a while loop. If a candidate number
# is some lin comb of 6,9,20 then we increment the count variable by 1
# and then go through the loop again.

def main():
    small = 6
    medium = 9
    large = 20
    
    #initialize the count to 0
    count = 0
    
    # start with the largest nugget number initialized to 5
    largest = small - 1
    
    # start with the first candidate as 6
    candidate = small
    
    while count != small:
        if(isNuggetNumber(candidate)):
            count += 1
        else:
            largest = candidate
            count = 0
        candidate += 1
        
    print("The largest number of nuggest you cannot buy is: {0}".format(largest))
    
    
main()