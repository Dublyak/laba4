from datetime import datetime, timedelta

def predict_lucky_dates(start_date, n):
    start_date = datetime.strptime(start_date, "%Y/%m/%d")
    lucky_dates = []
    current_date = start_date
    while len(lucky_dates) < 3:
        current_date += timedelta(days=n)
        if current_date.day % 4 != 0 and current_date.weekday() != 0:
            lucky_dates.append(current_date.strftime("%d %B, %A"))
    return lucky_dates

start_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))
lucky_dates = predict_lucky_dates(start_date, n)
for date in lucky_dates:
    print(date)
