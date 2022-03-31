# lesson 1, task 3


input_percent = int(input('insert percent number: '))
# percents from 11 to 19 being written "процентов"
if input_percent >= 11 and input_percent <= 19:
    print(f'{input_percent} процентов.')

# count of percent remainder
remainder_percent = input_percent
remainder_percent %= 10

if input_percent < 11 or input_percent > 19:
    if remainder_percent == 1:
        print(f'{input_percent} процент.')
    elif remainder_percent >= 2 and remainder_percent < 5:
        print(f'{input_percent} процента.')
    else:
        print(f'{input_percent} процентов.')


        