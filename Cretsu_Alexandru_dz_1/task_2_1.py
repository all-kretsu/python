# lesson 1, task 2

# creating basic value list
value_list = []
for value in range(0, 1000):
    if value % 2 != 0:
        # value to the power of 3
        value_list.append(value ** 3)

# creating list of sum of each value which can be divided at 7
sum_list = []
for value in value_list:
    result = 0
    new_value = value
    while new_value != 0:
        value_rem = new_value % 10
        new_value //= 10
        result += value_rem
    if result % 7 == 0:
        sum_list.append(value)
# sum of sum_list values
result_int = 0
for sum_list_values in sum_list:
    result_int += sum_list_values

# creating list with values from sum_list plus 17 divided at 7
sum_list_2 = []
for value in sum_list:
    value += 17
    result = 0
    new_value = value
    while new_value != 0:
        value_rem = new_value % 10
        new_value //= 10
        result += value_rem
    if result % 7 == 0:
        sum_list_2.append(value)
# sum of sum_list values
result_int_2 = 0
for sum_list_values in sum_list_2:
    result_int_2 += sum_list_values

print(result_int)
print(result_int_2)
