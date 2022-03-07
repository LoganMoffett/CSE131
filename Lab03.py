# 1. Name:
#      Logan Moffett
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This will display a calander for a given month in a year after 1753
# 4. What was the hardest part? Be as specific as possible.
#      I messed up the input loop which caused some problems till I noticed it was the issue.
#      Other then that it was pretty easy.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

def get_month():
    '''Get the month from the user'''
    while True:
        try:
            month = int(input("Enter a month between 1 and 12 "))
            if month >= 1 and month <= 12:
                return month
            else:
                print("invalid month")
        except:
            print("Invalid response")

def get_year():
    ''' Get the year from the user'''
    while True:
        try:
            year = int(input("Enter year: "))
            if year >= 1753:
                return year
            else:
                print("invalid year")
        except:
            print("Invalid Response")

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

def get_dow(user_month, user_year):
    '''Find the dow or spacing to the first day in the month'''
    print(user_year)
    month = 1
    year = 1753
    dow = 1
    while user_year != year:
        dow = (dow + 365 + is_leap_year(year)) % 7
        year = year + 1
    
    while user_month != month:
        dow = (dow + num_days(month, user_year)) % 7
        month = month + 1

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

def main(month = None, year = None):
    if month == None:
        month = get_month()
    if year == None:
        year = get_year()
    dow = get_dow(month, year)
    display_table(dow, num_days(month, year))

main(2, 1753)
main(1, 1754)
main(2, 1756)
main(2, 1800)
main(2, 2000)

