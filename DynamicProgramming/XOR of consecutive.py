import operator
"""
4
2
1
1
3
"""
total_numbers = input()
i=0
list_numbers = []
while (i<total_numbers):
    list_numbers.append(int(input()))
    i+=1


dict_max_count = {}

for i in range(0, len(list_numbers)):
    current_xor = list_numbers[0]
    if i in dict_max_count:
        count = dict_max_count[i]
        count = count + 1
        dict_max_count[i] = count
    else:
        dict_max_count[list_numbers[0]] = 1
    for j in range(i+1, len(list_numbers)):
        current_xor = current_xor ^ list_numbers[j]
        if current_xor in dict_max_count:
            count = dict_max_count[current_xor]
            count += 1
            dict_max_count[current_xor] = count
        else:
            dict_max_count[current_xor] = 1

min_key = float("inf")
max_val = 0

for key in dict_max_count:

    if dict_max_count[key] < max_val:

        continue

    if dict_max_count[key] > max_val:
        max_val = dict_max_count[key]
        min_key = key


    if dict_max_count[key]== max_val:
        if key < min_key:
            min_key = key


print min_key, max_val