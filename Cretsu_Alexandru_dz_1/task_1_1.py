# lesson 1, task 1

print('Hello, its a converter of seconds!')
# Input seconds
duration = int(input('Insert a number of seconds: \n'))
# seconds in 1 minute, 1 hour and 1 day
sec_in_min = 60
sec_in_hour = 3600
sec_in_day = 86400
# floored quotient
minutes = duration // sec_in_min
hours = duration // sec_in_hour
days = duration // sec_in_day

if duration < sec_in_min:
    print(f'{duration} сек.')
elif duration < sec_in_hour:
    seconds = duration % sec_in_min
    print(f'{minutes} мин {seconds} сек.')
elif duration < sec_in_day:
    seconds = duration % minutes
    minutes = (duration % sec_in_hour) // sec_in_min
    print(f'{hours} час. {minutes} мин. {seconds} сек.')
elif duration > sec_in_day:
    duration = duration % sec_in_day
    seconds = duration % minutes
    minutes = (duration % sec_in_hour) // sec_in_min
    hours = (duration % sec_in_day) // sec_in_hour
    print(f'{days} дн. {hours} час. {minutes} мин. {seconds} сек.')
