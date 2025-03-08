

#!/usr/bin/env python3
 
 
'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: Dalip Singh
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''
 
 
import sys
 
 
def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]
 
 
 
 
def mon_max(month: int, year: int) -> int:
    """
    Returns the maximum number of days in a given month of a given year.
    
    Parameters:
        month (int): The month number (1-12).
        year (int): The year to determine if February has 28 or 29 days.

    Returns:
        int: The number of days in the given month.
    """
    # Determine if it's a leap year
    feb_max = 29 if leap_year(year) else 28

    # Dictionary of max days for each month
    days_in_month = {
        1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
        8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    return days_in_month.get(month, 0)  # Default to 0 if an invalid month is given


 
 
def after(date: str) -> str:
    """
    Returns the next day for a given date in YYYY-MM-DD format.
    """
    str_year, str_month, str_day = date.split('-')
    year, month, day = int(str_year), int(str_month), int(str_day)
    
    # Correctly call mon_max() with both arguments
    month_days = mon_max(month, year)

    day += 1  # Move to the next day
    
    if day > month_days:  # Check if day exceeds month's max
        day = 1
        month += 1
    
    if month > 12:  # If month exceeds December, reset to January next year
        month = 1
        year += 1
    
    return f"{year}-{month:02d}-{day:02d}"
 
 
 
 
def usage():
    """
    Prints usage instructions when the user makes an error.
    """
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

 
 
 
 
def leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.
    Returns True if leap year, otherwise False.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

 
 
def valid_date(date: str) -> bool:
    """
    Checks if the given date is valid in YYYY-MM-DD format.
    
    Parameters:
        date (str): The date as a string in 'YYYY-MM-DD' format.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        # Ensure the date is in correct format
        parts = date.split('-')
        if len(parts) != 3:
            return False

        # Convert string parts to integers
        year, month, day = map(int, parts)

        # Validate year range (reasonable limits)
        if year < 1000 or year > 9999:  
            return False

        # Validate month range
        if month < 1 or month > 12:
            return False

        # Validate day range using mon_max()
        max_days = mon_max(month, year)
        if day < 1 or day > max_days:
            return False

        return True  # If all checks pass, return True

    except (ValueError, TypeError):
        return False  # Catch non-numeric values or incorrect formats
 
 
def day_count(start_date: str, end_date: str) -> int:
    """
    Counts the number of Saturdays and Sundays between start_date and end_date (inclusive).
    
    Parameters:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        int: The number of weekend days in the given range.
    """
    count = 0
    current_date = min(start_date, end_date)  # Ensure correct order
    end_date = max(start_date, end_date)

    # Define possible weekend names
    weekend_names = {"Saturday", "Sunday", "sat", "sun"}
    weekend_numbers = {6, 7}  # If day_of_week() returns numbers

    while current_date <= end_date:
        year, month, day = map(int, current_date.split('-'))

        weekday = day_of_week(year, month, day)  # Get day of the week

        # Convert weekday to lowercase for comparison
        if isinstance(weekday, str) and weekday.lower() in weekend_names:
            count += 1
        elif isinstance(weekday, int) and weekday in weekend_numbers:
            count += 1

        current_date = after(current_date)  # Move to the next day

    return count
 
 
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    
    date1, date2 = sys.argv[1], sys.argv[2]

    if not valid_date(date1) or not valid_date(date2):
        usage()
    
    weekends = day_count(date1, date2)
    print(f"The period between {min(date1, date2)} and {max(date1, date2)} includes {weekends} weekend days.")

