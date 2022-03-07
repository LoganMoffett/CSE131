def leap_year_math(start_year, end_year):
    leap_years = 0
    year = end_year - start_year
    leap_years = leap_years + int(year / 400)
    leap_years = leap_years - int(year / 100)
    leap_years = leap_years + int(year / 4)
    return leap_years
    

def get_start_year(year = None):
    if year == None:
        year = input("What is the start year? ")
        year = int(year)
    return year
    
def is_leap_year(year):
    '''Find out if it is a leap year'''
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def num_days(month, year):
    '''Find out how many days are in the month'''
    days = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month != 2:
        return days[month]
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28

def get_dow(end_year, month):
    years = end_year - 1753
    dow = 1
    start_month = 1
    dow = (dow + int((365 * years) + leap_year_math(1753, end_year))) % 7
    while start_month != month:
        dow = (dow + int(num_days(start_month, end_year))) % 7
        start_month += 1 
    return dow

def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def main():
    leap_years = 0
    year = 1753
    end_year = get_start_year()
    month = int(input("What month "))
    dow = get_dow(end_year, month)
    display_table(dow, num_days(month, end_year))
    while year != end_year:
        leap_years = leap_years + is_leap_year(year)
        year = year + 1
while True:
    main()