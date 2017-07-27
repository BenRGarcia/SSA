""" A module that returns full retirement age (MM/YYYY) based on user's DOB"""
# SSA Full Retirement Age (FRA) chart can be found at:
# https://www.ssa.gov/planners/retire/retirechart.html

import datetime

# Apologies--this function is verbose (Function modeled after US Federal Regulations)
def fra_chart(dob):

    """A function that returns the SSA full retirement age (FRA) as measured in months"""

    # If date of birth is 1/1/1938 or earlier, full retirement age (FRA) is 65
    if fra_dob < datetime.date(1938, 1, 2):
        months_to_fra = 780

    # If date of birth is between 1/2/1938 and 1/1/1939, full retirement age (FRA) is age 65 + 2 months
    elif fra_dob < datetime.date(1939, 1, 2):
        months_to_fra = 782

    # If date of birth is between 1/2/1939 and 1/1/1940, full retirement age (FRA) is age 65 + 4 months
    elif fra_dob < datetime.date(1940, 1, 2):
        months_to_fra = 784

    # If date of birth is between 1/2/1940 and 1/1/1941, then full retirement age (FRA) is age 65 + 6 months
    elif fra_dob < datetime.date(1941, 1, 2):
        months_to_fra = 786

    # If date of birth is between 1/2/1941 and 1/1/1942, then full retirement age (FRA) is age 65 + 8 months
    elif fra_dob < datetime.date(1942, 1, 2):
        months_to_fra = 788

    # If date of birth is between 1/2/1942 and 1/1/1943, then full retirement age (FRA) is age 65 + 10 months
    elif fra_dob < datetime.date(1943, 1, 2):
        months_to_fra = 790

    # If date of birth is between 1/2/1943 and 1/1/1955, then full retirement age (FRA) is age 66
    elif fra_dob < datetime.date(1955, 1, 2):
        months_to_fra = 792

    # If date of birth is between 1/2/1955 and 1/1/1956, then full retirement age (FRA) is age 66 + 2 months
    elif fra_dob < datetime.date(1956, 1, 2):
        months_to_fra = 794

    # If date of birth is between 1/2/1956 and 1/1/1957, then full retirement age (FRA) is age 66 + 4 months
    elif fra_dob < datetime.date(1957, 1, 2):
        months_to_fra = 796

    # If date of birth is between 1/2/1957 and 1/1/1958, then full retirement age (FRA) is age 66 + 6 months
    elif fra_dob < datetime.date(1958, 1, 2):
        months_to_fra = 798

    # If date of birth is between 1/2/1958 and 1/1/1959, then full retirement age (FRA) is age 66 + 8 months
    elif fra_dob < datetime.date(1959, 1, 2):
        months_to_fra = 800

    # If date of birth is between 1/2/1959 and 1/1/1960, then full retirement age (FRA) is age 66 + 10 months
    elif fra_dob < datetime.date(1960, 1, 2):
        months_to_fra = 802

    # If date of birth is 1/2/1960 or later, then your full retirement age (FRA) is age 67
    else:
        months_to_fra = 804

    return months_to_fra


def fra_month_calc(): # A function that makes certain month integer remains between 1 and 12, returns integer of calendar month of Full Retirement Age (FRA)
  remainder_months = fra_chart(fra_dob) % 12
  if fra_dob.month + remainder_months <= 12:
    return remainder_months
  else:
    remainder_months = fra_dob.months + remainder_months - 12
    return remainder_months


fra_month = fra_dob.month + fra_month_calc()                                        # Declares a variable to store value of Full Retirement Age (FRA) month
fra_year = fra_dob.year + (fra_chart(fra_dob) // 12)                                # Declares a variable to store value of Full Retirement Age (FRA) year
fra_month_day_year = str(fra_month) + "/" + str(fra_dob.day) + "/" + str(fra_year)  # Concatenate strings to later convert to date object
fra_date_object = datetime.datetime.strptime(fra_month_day_year, "%m/%d/%Y").date() # Convert string object to date object

print ("According to SSA, you will be Full Retirement Age (FRA) in " + fra_date_object.strftime('%B %Y') + " when you are " + str(fra_chart(fra_dob) // 12) + " years and " + str(fra_chart(fra_dob) % 12) + " months old.")
