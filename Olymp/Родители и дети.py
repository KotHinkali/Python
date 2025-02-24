from datetime import datetime

def years_between_dates(date1, date2):
    difference = abs(date1.year - date2.year)
    if date2.month < date1.month or (date2.month == date1.month and date2.day < date1.day):
        difference -= 1
    return difference


n = 3# int(input())
dates = ['12.02.1980', '15.03.1981', '01.03.2001', '29.02.2000', '17.05.2003']
"""for i in range(n + 2):
    dates.append(input())"""

dates = [datetime.strptime(d, '%d.%m.%Y') for d in dates]

now = datetime.now()

latest_date = None
latest_index = 0
for i in range(n + 2):
    if dates[i] < now:
        latest_date = dates[i]
        latest_index = i

parents_total_age = years_between_dates(latest_date, dates[0]) + years_between_dates(latest_date, dates[1])

child_total_age = 0
for i in range(2, n + 2):
    if i != latest_index:
        child_total_age += years_between_dates(latest_date, dates[i])

year_count = 0
while child_total_age < parents_total_age:
    parents_total_age += 2
    child_total_age += len(dates) - 2
    year_count += 1

print(year_count)




