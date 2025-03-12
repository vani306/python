from datetime import date

def days_between_dates(date1, date2):
    
    d1 = date(date1[2], date1[1], date1[0])
    d2 = date(date2[2], date2[1], date2[0])
    return abs((d2 - d1).days)

date1 = (10, 3, 2024)  
date2 = (25, 3, 2024)  

days_difference = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2}: {days_difference}")
