""" A program that prints a matrix of benefit amounts based on filing month """
# Run this program in BASH with: $ python3 Retirement.py welcome.txt

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

    # Test user input for valid date of birth date format
    try:
        valid_dob = datetime.datetime.strptime(actual_dob, "%m/%d/%Y")
    except ValueError:
        print("\nSorry, that's not a valid date. You must use the MM/DD/YYYY format.")
        input("\nPress the ENTER key to try again.\n>>>")
        date_of_birth()

    # If no exception, convert user input to date object
    else:

        # Convert user input "dob" string into date object "birthdate"
        dob_date_obj = datetime.datetime.strptime(actual_dob, "%m/%d/%Y").date()

        # Subtract 1 day from the actual date of birth b/c of SSA legislative/actuarial rules
        fra_dob = dob_date_obj - datetime.timedelta(days=1)

        return fra_dob


def months_to_fra(z): # Apologies, this function is verbose--function modeled after SSA regulations
    """A function that returns the number of months to SSA full retirement age (FRA)"""

    # If date of birth is 1/1/1938 or earlier, full retirement age (FRA) is 65
    if z < datetime.date(1938, 1, 2):
        months_to_fra = 780

    # If date of birth is between 1/2/1938 and 1/1/1939, full retirement age (FRA) is age 65 + 2 months
    elif z < datetime.date(1939, 1, 2):
        months_to_fra = 782

    # If date of birth is between 1/2/1939 and 1/1/1940, full retirement age (FRA) is age 65 + 4 months
    elif z < datetime.date(1940, 1, 2):
        months_to_fra = 784

    # If date of birth is between 1/2/1940 and 1/1/1941, then full retirement age (FRA) is age 65 + 6 months
    elif z < datetime.date(1941, 1, 2):
        months_to_fra = 786

    # If date of birth is between 1/2/1941 and 1/1/1942, then full retirement age (FRA) is age 65 + 8 months
    elif z < datetime.date(1942, 1, 2):
        months_to_fra = 788

    # If date of birth is between 1/2/1942 and 1/1/1943, then full retirement age (FRA) is age 65 + 10 months
    elif z < datetime.date(1943, 1, 2):
        months_to_fra = 790

    # If date of birth is between 1/2/1943 and 1/1/1955, then full retirement age (FRA) is age 66
    elif z < datetime.date(1955, 1, 2):
        months_to_fra = 792

    # If date of birth is between 1/2/1955 and 1/1/1956, then full retirement age (FRA) is age 66 + 2 months
    elif z < datetime.date(1956, 1, 2):
        months_to_fra = 794

    # If date of birth is between 1/2/1956 and 1/1/1957, then full retirement age (FRA) is age 66 + 4 months
    elif z < datetime.date(1957, 1, 2):
        months_to_fra = 796

    # If date of birth is between 1/2/1957 and 1/1/1958, then full retirement age (FRA) is age 66 + 6 months
    elif z < datetime.date(1958, 1, 2):
        months_to_fra = 798

    # If date of birth is between 1/2/1958 and 1/1/1959, then full retirement age (FRA) is age 66 + 8 months
    elif z < datetime.date(1959, 1, 2):
        months_to_fra = 800

    # If date of birth is between 1/2/1959 and 1/1/1960, then full retirement age (FRA) is age 66 + 10 months
    elif z < datetime.date(1960, 1, 2):
        months_to_fra = 802

    # If date of birth is 1/2/1960 or later, then your full retirement age (FRA) is age 67
    else:
        months_to_fra = 804

    return months_to_fra


def fra_mm_yyyy(a):
    """A function that returns MM/YYYY of user's full retirement age (FRA)"""

    # Calculate year of full retirement age (FRA)
    fra_year = fra_dob.year + (months_to_fra // 12)

    # Calculate FRA month, make sure it's between 1 and 12 (a valid calendar month)
    if (fra_dob.month + (a % 12)) <= 12:
        fra_month = fra_dob.month + (a % 12)
        return fra_month, fra_year

    else:
        fra_month = fra_dob.month + (a % 12) - 12
        return fra_month, fra_year


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
introduction(file_1)                     # Print introduction .txt to terminal
fra_dob = date_of_birth()                # Call function to get user's date of birth, declare fra_dob
months_to_fra = months_to_fra(fra_dob)   # Call function to return user's # of month until FRA
fra_month, fra_year = fra_mm_yyyy(months_to_fra) # Call function to return user's FRA (MM/YYYY)
print("Yo! FRA month/year is:", fra_month, fra_year)



#fra_month_day_year = str(fra_month) + "/" + str(fra_dob.day) + "/" + str(fra_year)  # Concatenate strings to later convert to date object
#fra_date_object = datetime.datetime.strptime(fra_month_day_year, "%m/%d/%Y").date() # Convert string object to date object
