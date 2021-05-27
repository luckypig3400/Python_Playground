import datetime
import requests
from bs4 import BeautifulSoup

startDate = datetime.datetime(2020, 1, 1)
# https://www.w3schools.com/python/python_datetime.asp

for i in range(365):
    print(startDate)
    startDate += datetime.timedelta(days=1)
    # https://stackoverflow.com/questions/3240458/how-to-increment-a-datetime-by-one-day

# html = requests.get("https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker=2021-05-20#")
# print(html.text)

# soup = BeautifulSoup(html.text, "html.parser")
