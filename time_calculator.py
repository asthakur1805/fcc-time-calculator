def add_time(start,duration,day=''):
    
    # Bi-directional mapping of days of the week for lookup purposes
    # day variable -> input, days variable -> for computation of difference, start day-> numerical code for starting day
    days_code = {'SUNDAY':0,'MONDAY':1,'TUESDAY':2,'WEDNESDAY':3,'THURSDAY':4,'FRIDAY':5,'SATURDAY':6}
    days_decode = dict((days_code[key],key.capitalize()) for key in days_code)
    
    # Getting the values of the start times and duration times  
    start_time = start.split()

    period = start_time[1]  # AM/PM

    start_time = start_time[0]
    start_HH=int(start_time[:start_time.find(':')]) #start hours
    start_MM=int(start_time[start_time.find(':')+1:]) #start mins

    if period == 'PM':
        start_HH = start_HH % 12 + 12 #converting to 24 hrs clock

    days = 0 if day == '' else days_code[day.upper()]
    start_day = days # Keeping track of this value to calculate the days difference required in output

    duration_time = duration.split(':')

    duration_HH=int(duration_time[0]) 
    duration_MM=int(duration_time[1])

    result_MM = start_MM + duration_MM # adding mins and checking for day switch
    if result_MM>=60:
        result_MM%=60
        start_HH+=1
        if start_HH==24:
            start_HH=0
            days+=1

    result_HH = start_HH + duration_HH # adding hours and checking for the day switch(es)
    if result_HH>=24:
        days += result_HH // 24
        result_HH%=24

    result_period = ' PM' if 12<=result_HH<24 else ' AM' 

    result_HH%=12
    if result_HH==0:
        result_HH=12 # Reconverting to 12 hour clock

    result_HH = f'{result_HH}'
    result_MM = f'{result_MM:02}'

    if day != '':
        result_day = f', {days_decode[days%7]}' # If day is passed as a third input, decode the day from the map days_decode
    else:
        result_day=''

    result_diff = days - start_day # Computing days difference
    if result_diff == 0:
        result_diff = ''
    elif result_diff == 1:
        result_diff = f' (next day)'
    else:
        result_diff = f' ({result_diff} days later)'

    new_time = ''.join([result_HH,':',result_MM,result_period,result_day,result_diff]) # Final result
    return new_time