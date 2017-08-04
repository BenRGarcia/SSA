""" A program that prints a matrix of benefit amounts based on filing month """
# Run this program in BASH with: $ python3 Retirement.py welcome.txt

import datetime
from sys import argv
script, file_1 = argv
import ReductionFactorDict


def introduction(a):
    """A function that introduces the program"""

    # Clear the user's terminal screen
    print("\033c")

    # Open .txt file, print to terminal, close .txt file
    open_a = open(a)
    print(open_a.read())
    open_a.close()

    # Prompt user to continue
    input("\n\nPress the ENTER key to continue\n>>>")


def dob_input():
    """A function that takes user date of birth input"""

    # Clear the user's terminal screen
    print("\033c")

    # Get user's date of birth
    dob = input("What is your date of birth? (MM/DD/YYYY)\n>>>")

    # Call function that tests for valid dob
    test_dob_input(dob)


def test_dob_input(b):
    """A function that checks the validity of user 'date of birth' input"""

    # Test for validity of user's 'date of birth' input, re-call dob_input() if invalid
    try:
        valid_dob = datetime.datetime.strptime(b, "%m/%d/%Y").date()
        convert_to_fra_dob(valid_dob)
    except:
        print("\nSorry, that's not a valid date. You must use the MM/DD/YYYY format.")
        input("\nPress the ENTER key to try again.\n>>>")
        dob_input()


def convert_to_fra_dob(c):
    """A function that declares global 'date of birth' variables"""

    global actual_dob
    actual_dob = c

    global string_actual_dob
    string_actual_dob = str(actual_dob)

    global fra_dob
    fra_dob = c - datetime.timedelta(days=1)

    global string_fra_dob
    string_fra_dob = str(fra_dob)


def fra_months(z): # Apologies, this function is verbose--function modeled after SSA regulations
    """A function that returns the number of months from date of birth to FRA based on SSA chart"""

    # Declare global variable
    global months_to_fra

    # If date of birth is 1/1/1938 or earlier, full retirement age (FRA) is 65
    if z < datetime.date(1938, 1, 2):
        months_to_fra = 780

    # If date of birth is between 1/2/1938 and 1/1/1939, then (FRA) is age 65 + 2 months
    elif z < datetime.date(1939, 1, 2):
        months_to_fra = 782

    # If date of birth is between 1/2/1939 and 1/1/1940, then (FRA) is age 65 + 4 months
    elif z < datetime.date(1940, 1, 2):
        months_to_fra = 784

    # If date of birth is between 1/2/1940 and 1/1/1941, then (FRA) is age 65 + 6 months
    elif z < datetime.date(1941, 1, 2):
        months_to_fra = 786

    # If date of birth is between 1/2/1941 and 1/1/1942, then (FRA) is age 65 + 8 months
    elif z < datetime.date(1942, 1, 2):
        months_to_fra = 788

    # If date of birth is between 1/2/1942 and 1/1/1943, then (FRA) is age 65 + 10 months
    elif z < datetime.date(1943, 1, 2):
        months_to_fra = 790

    # If date of birth is between 1/2/1943 and 1/1/1955, then (FRA) is age 66
    elif z < datetime.date(1955, 1, 2):
        months_to_fra = 792

    # If date of birth is between 1/2/1955 and 1/1/1956, then (FRA) is age 66 + 2 months
    elif z < datetime.date(1956, 1, 2):
        months_to_fra = 794

    # If date of birth is between 1/2/1956 and 1/1/1957, then (FRA) is age 66 + 4 months
    elif z < datetime.date(1957, 1, 2):
        months_to_fra = 796

    # If date of birth is between 1/2/1957 and 1/1/1958, then (FRA) is age 66 + 6 months
    elif z < datetime.date(1958, 1, 2):
        months_to_fra = 798

    # If date of birth is between 1/2/1958 and 1/1/1959, then (FRA) is age 66 + 8 months
    elif z < datetime.date(1959, 1, 2):
        months_to_fra = 800

    # If date of birth is between 1/2/1959 and 1/1/1960, then (FRA) is age 66 + 10 months
    elif z < datetime.date(1960, 1, 2):
        months_to_fra = 802

    # If date of birth is 1/2/1960 or later, then (FRA) is age 67
    else:
        months_to_fra = 804

    return months_to_fra


def fra_month_year(e):
    """A function that returns MM/YYYY of user's full retirement age (FRA)"""

    # Declare global variables
    global age_fra_year
    global fra_mmYYYY
    global remainder_months

    # Calculate year of full retirement age (FRA)
    fra_year = fra_dob.year + (months_to_fra // 12)
    remainder_months = months_to_fra % 12
    age_fra_year = months_to_fra // 12

    # Make sure month of FRA is between 1 and 12 (a valid calendar month)
    if (fra_dob.month + (e % 12)) <= 12:

        # Calculate month of FRA
        fra_month = fra_dob.month + (e % 12)

        # Concatenate string to convert to date object
        string_fra_mmYYYY = str(fra_month) + "/" + str(fra_year)

        # Convert date string to date object
        fra_mmYYYY = datetime.datetime.strptime(string_fra_mmYYYY, "%m/%Y").date()

        return fra_mmYYYY

    # Make sure month of FRA is between 1 and 12 (a valid calendar month)
    else:

        # Calculate month of FRA
        fra_month = fra_dob.month + (e % 12) - 12

        # Concatenate string to convert to date object
        string_fra_mmYYYY = str(fra_month) + "/" + str(fra_year)

        # Convert date string to date object
        fra_mmYYYY = datetime.datetime.strptime(string_fra_mmYYYY, "%m/%Y").date()

        return fra_mmYYYY


def dob_engine():
    """A function that forces valid date of birth input from user"""

    while True:
        dob_input()
        if fra_dob != None:
            break


def pia_input():
    """A function that takes user input of SSA's PIA and converts to decimal object"""

    # Clear the user's terminal screen
    print("\033c")

    # Get user input of Primary Insurance Amount (PIA)
    print("According to SSA, what is the estimated benefit amount you would receive \nat your full retirement age?")
    pia = input("Note: you must use the format: $XXXX\n>>> $")

    # Call function that tests for valid PIA
    test_pia_input(pia)


def test_pia_input(f):
    """"A function that tests for the validity of user 'PIA amount' input"""

    # Test user input for valid PIA input
    try:
        convert_to_int(f)
    except:
        print("\nSorry, that's not a valid amount. You must use the $XXXX format.")
        input("\nPress the ENTER key to try again.\n>>>")
        pia_input()


def convert_to_int(g):
    """A function that converts PIA to a Decimal type"""

    global ssa_pia
    ssa_pia = int(g)

    global string_ssa_pia
    string_ssa_pia = str('{:,.0f}'.format(ssa_pia))


def pia_engine():
    """A function that forces valid PIA input from user"""

    while True:
        pia_input()
        if ssa_pia != None:
            break


# Step 4 - Perform Calculations
def mba_calc():
    """A function that calculates the SSA Retirement benefit matrix"""

    # Clear the user's terminal screen
    print("\033c")

    print("According to SSA, based on your date of birth of:", actual_dob.strftime("%B %d, %Y"))
    print("Your full retirement age is:", fra_mmYYYY.strftime('%B %Y'))

    input("\nPress the ENTER key to continue\n>>>")
    # Clear the user's terminal screen
    print("\033c")

    print("\nIf you file for SSA RIB effective with", fra_mmYYYY.strftime('%B %Y'))
    print("Your full retirement age benefit would be:$" + string_ssa_pia)

    input("\nPress the ENTER key to see all possible months and their corresponding benefit amounts\n>>>")
    # Clear the user's terminal screen
    print("\033c")
    
    print("If you file 1 month early, your MBA would be about ${:.2f}".format(ssa_pia * ReductionFactorDict.reduction_factors[0][1] // 1))

    # increment print statement
    rf = 2

    # Account for SSA's throughout the month rule
    if fra_dob.day >= 2:
        # distance (in months) of age 62 to FRA
        early_to_fra_count = months_to_fra - 745
        early_to_fra_count_list = ReductionFactorDict.reduction_factors[1:early_to_fra_count]

        for orf in early_to_fra_count_list:
            print("If you file", rf, "months early, your MBA would be about ${:.2f}".format(ssa_pia * orf[1] // 1))
            rf += 1
            early_to_fra_count -= 1

    else:
        # distance (in months) of age 62 to FRA
        early_to_fra_count = months_to_fra - 744
        early_to_fra_count_list = ReductionFactorDict.reduction_factors[1:early_to_fra_count]

        for orf in early_to_fra_count_list:
            print("If you file", rf, "months early, your MBA would be about ${:.2f}".format(ssa_pia * orf[1] // 1))
            rf += 1
            early_to_fra_count -= 1


def program_engine():
    """A function that runs the show for this program"""

    # Print introduction .txt to terminal
    introduction(file_1)

    # Call function that asks user for valid date of birth value until one is given
    dob_engine()

    # Call function that calculates how many months until full retirement age (FRA)
    fra_months(fra_dob)

    # Call function that adds month to (FRA) to the SSA date of birth (fra_dob)
    fra_month_year(months_to_fra)

    pia_engine()

    mba_calc()


# Call function that runs the program
program_engine()
