# Write a Python program to generate the next 15 leap years starting from a given year.
# Populate the leap years into a list and display the list.

def find_leap_years(given_year):
    count = 0
    leap_years = []
    while count < 15:
        if given_year % 400 == 0  or (given_year % 4 == 0 and given_year % 100 != 0):
                leap_years.append(given_year)
                count += 1
                given_year+=4
        else:
           given_year +=1
    return leap_years
leap_years_list = find_leap_years(2001)
print(leap_years_list)
