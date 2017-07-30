""" A program that prints a matrix of benefit amounts based on filing month """
# Run this program in BASH with $ python3 Retirement.py welcome.txt
import datetime
import time
#import decimal
from sys import argv
script, file_1 = argv


def introduction(x):
    """A function that introduces the program"""

    # Clear the user's terminal screen
    print("\033c")

    # Open welcome.txt, print to terminal
    open_x = open(x)
    print(open_x.read())
    open_x.close()

    # Prompt user to continue
    input("\n\nPress the ENTER key to continue\n>>>")


# Step 2 - Ascertain the user's date of birth, convert to date object
def date_of_birth():
    """A function that takes user date of birth input, converts to date object"""

    # Clear the user's terminal screen
    print("\033c")

    # User inputs date of birth (dob), store as variable "dob"
    dob = input("What is your date of birth? (MM/DD/YYYY)\n>>>")

    # Exception handling, test user input for valid date
    try:
        valid_dob = time.strptime(dob, "%m/%d/%Y")
    except ValueError:
        print("\nSorry, that's not a valid date.")
        print("\nYou must use the MM/DD/YYYY format.")
        input("\nPress the ENTER key to try again.\n>>>")
        date_of_birth()

    else:

        # Convert user input "dob" string into date object "birthdate"
        birthdate = datetime.datetime.strptime(dob, "%m/%d/%Y").date()

        # Subtract 1 day from the actual date of birth b/c of SSA legislative/actuarial rules
        fra_dob = birthdate - datetime.timedelta(days=1)

        return fra_dob



# Step 3 - Ascertain the user's "Primary Insurance Amount" according to SSA
#def ssa_pia():
    """A function that takes user input of SSA's PIA and converts to decimal object"""
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
introduction(file_1)
date_of_birth()
