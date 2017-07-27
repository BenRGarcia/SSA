""" A program that prints a matrix of benefit amounts based on any filing month """

import datetime
import decimal

# Step 1 - Introduce the program
def introduction():

    """A function that introduces the program"""

    print ("Welcome to the SSA Retirement Benefit Matrix Program!")
    print ("This program will ask you for 2 things: and")
    print ("1) Your date of birth (MM/DD/YYYY)")
    print ("")
    print ('"Primary Insurance Amount" according to SSA.')
    print ("In return, the program with return a matrix contains")
    print ("all possible monthly benefit amounts depending on")
    print ("your chosen month of filing.")


# Step 2 - Ascertain the user's date of birth, convert to date object
def date_of_birth():

    """A function that takes user date of birth input, converts to date object"""

    # User inputs date of birth (dob), store as variable "dob"
    dob = input("What is your date of birth? (MM/DD/YYYY) ")

    # Convert user input "dob" string into date object "birthdate"
    birthdate = datetime.datetime.strptime(dob, "%m/%d/%Y").date()

    # Subtract 1 day from the actual date of birth b/c of SSA legislative/actuarial rules
    fra_dob = birthdate - datetime.timedelta(days=1)







# Step 3 - Ascertain the user's "Primary Insurance Amount" according to SSA
def ssa_pia():
    """A function that takes user input of SSA's PIA and converts to decimal object"""
    # Must use "decimal" module when working with money!!!



# Step 4 - Take date of birth date object and return full retirement age




# Step 4 - Perform Calculations
def calculations():
    """A function that calculates SSA Retirement benefit matrix"""
    # Integrate use of "fraction" module
    # Account for SSA's rounding
    # Send results to .txt file?






# Step 5 - Present the benefit estimate in a comprehensible format
def benefit_matrix():
    """A function that presents the SSA Retirement benefit matrix"""
