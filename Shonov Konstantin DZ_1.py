minutes = 60
hour = minutes * 60
day =  hour * 24
sec = [59, 60, 61, 3599, 3600, 3601, 86399, 86400]
for duration in sec:

    if duration < minutes:
        print(duration, 'sec')
    elif duration < hour:
        print(duration // minutes, 'min', duration % minutes, 'sec')
    elif duration < day:
        print(duration // hour, 'hour', duration // minutes, 'min', duration % minutes, 'sec')
    else:
        print(duration// day, 'day',duration // hour, 'hour', duration // minutes, 'min', duration % minutes, 'sec')