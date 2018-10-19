def minute_to_hour(sec,minutes=70):
    hours = (minutes*60 + sec)/60
    return hours

print (minute_to_hour(60, 60))
