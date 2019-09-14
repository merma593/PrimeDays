'''
COSC326 Etude 2

Finds and returns the truly prime days of the year from given input

@author Markham Meredith

'''

import math
import sys
from itertools import islice


months = [int(x) for x in sys.argv[1:]]        # Takes input arguments and puts into a list of the months
sumList = range(1,sum(months)+1)               # Makes a list of days of the year
splitList = iter(sumList)                      # Creates iterable object of days of year 
result = [list(islice(splitList, elem))        # Splits the days of the year into elements the size of the months  
          for elem in months]


def is_prime_num(x):
    if(x < 2):
        return False
    elif(x == 2):
        return True  
    for n in range(2, int(math.sqrt(x))+1):
        if(x % n==0):
            return False
    return True


def find_truly_prime(dateList):
    for count, elem in enumerate(dateList,1):                              # starts index at 1 instead of 0 to find prime indexes(months)    
        if(is_prime_num(count)):
            for con, a in enumerate(elem,1):                               # starts index at 1 insted of 0 to find prime indexes(days of month)
                if(is_prime_num(a) and is_prime_num(con)):                 # if the value of element(day of the year) and index of element(day of month) is prime
                    print(str(a) + ": " + str(count) + " " + str(con))


find_truly_prime(result)
