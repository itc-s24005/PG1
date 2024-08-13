import datetime
t_delta = datetime.timedelta(days=1)
dt = datetime.datetime.strptime("24/08/13", "%d/%m/%y")
print(dt + t_delta)

