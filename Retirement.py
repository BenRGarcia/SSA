""" A program that prints a matrix of benefit amounts based on filing month """
# Run this program in BASH with $ python3 Retirement.py welcome.txt
import FullRetirementAge
import datetime
#import decimal
from sys import argv
script, file_1 = argv


def introduction(x):
    """A function that introduces the program"""

    # Clear the user's terminal screen
    print("\033c")

    # Open .txt file, print to terminal, close .txt file
    open_x = open(x)
    print(open_x.read())
    open_x.close()

    # Prompt user to continue
    input("\n\nPress the ENTER key to continue\n>>>")


def date_of_birth():
    """A function that takes user date of birth input, converts to date object"""

    # Clear the user's terminal screen
    print("\033c")

    # User inputs date of birth (dob), store as variable "dob"
    actual_dob = input("What is your date of birth? (MM/DD/YYYY)\n>>>")

    # Test user input for valid date format
    try:
        valid_dob = datetime.datetime.strptime(actual_dob, "%m/%d/%Y")
    except ValueError:
        print("\nSorry, that's not a valid date. You must use the MM/DD/YYYY format.")
        input("\nPress the ENTER key to try again.\n>>>")
        date_of_birth()

    # If no exception, convert user input to date object
    else:

        # Convert user input "dob" string into date object "birthdate"
        birthdate = datetime.datetime.strptime(actual_dob, "%m/%d/%Y").date()

        # Subtract 1 day from the actual date of birth b/c of SSA legislative/actuarial rules
        fra_dob = birthdate - datetime.timedelta(days=1)

        return fra_dob


def full_retirement_age(y):
    """A function that returns the full retirement age (MM/YYYY) according to SSA"""

    print(FullRetirementAge.fra_chart(y))



# Step 3 - Ascertain the user's "Primary Insurance Amount" according to SSA
#def ssa_pia():
    #"""A function that takes user input of SSA's PIA and converts to decimal object"""
    # Must use "decimal" module when working with money!!!


# Step 4 - Take date of birth date object and return full retirement age


# Step 4 - Perform Calculations
#def calculations():
    """A function that calculates SSA Retirement benefit matrix"""
    # Integrate use of "fraction" module
    # Account for SSA's rounding
    # Send results to .txt file?


# Step 5 - Present the benefit estimate in a comprehensible format
#def benefit_matrix():
    """A function that presents the SSA Retirement benefit matrix"""


# Call functions below
introduction(file_1)          # Print introduction .txt to terminal
fra_dob = date_of_birth()     # Call function to get user's date of birth, create global fra_dob
months_to_fra = full_retirement_age(fra_dob)  # Call function to return user's full retirement age
