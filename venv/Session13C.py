import datetime

today = datetime.datetime.today()
print(today)

tomorrow = datetime.datetime(2019, 1, 1, 12, 12, 12)
print(tomorrow)

howMany = tomorrow - today
print(howMany)

