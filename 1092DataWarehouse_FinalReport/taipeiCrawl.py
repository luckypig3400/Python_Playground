import datetime

startDate = datetime.datetime(2020, 1, 1)
# https://www.w3schools.com/python/python_datetime.asp

for i in range(365):
    print(startDate)
    startDate += datetime.timedelta(days=1)
    # https://stackoverflow.com/questions/3240458/how-to-increment-a-datetime-by-one-day

