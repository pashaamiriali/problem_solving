normal_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
pd_in_1918 = '26.09.1918'
DAY_OF_PROGRAMMERS = 256


def calculate_day_of_programmers(year):
    if year == 1918:
        return pd_in_1918

    if is_leap_year(year):
        return calculate_for_leap_year(year)
    else:
        return calculate_for_normal_year(year)


def is_leap_year(year):
    if year < 1918:
        return check_for_julian(year)
    else:
        return check_for_gregorian(year)


def check_for_julian(year):
    return year % 4 == 0


def check_for_gregorian(year):
    return year % 400==0 or (year % 4 == 0 and not year % 100 == 0)


def calculate_for_leap_year(year):
    return calculate_day_in_year(DAY_OF_PROGRAMMERS, leap_months, year)


def calculate_for_normal_year(year):
    return calculate_day_in_year(DAY_OF_PROGRAMMERS, normal_months, year)


def calculate_day_in_year(day, months, year):
    _day = day
    month = 0
    for i in range(0, len(months)):
        if _day < months[i]:
            month = i+1
            break
        else:
            _day -= months[i]
    return str(_day)+'.0'+str(month)+'.'+str(year)




def main():
    year = int(input())
    print(calculate_day_of_programmers(year))

if __name__=='__main__':
    main()

