from datetime import date as dt, timedelta
start_date = dt(2014, 4, 1)
end_date = dt(2015, 4, 1)

days = (end_date - start_date).days

for i in range(days+1):
    print start_date
    start_date = start_date + timedelta(days=1)
