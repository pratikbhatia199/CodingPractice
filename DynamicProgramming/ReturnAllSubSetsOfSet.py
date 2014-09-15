__author__ = 'pratik'
import copy
list_input = [1,3,5,7,8,9]

all_subsets = [[]]


for value in list_input:
    temp_all_subsets = []
    for list_value in all_subsets:
        temp_list_value = copy.copy(list_value)
        temp_list_value.append(value)
        temp_all_subsets.append(temp_list_value)

    for temp_list in temp_all_subsets:
        all_subsets.append(temp_list)


print len(all_subsets)

def get_all_subsets(list_value, i, all_subsets):

    if i == len(list_value):
        return all_subsets

    temp_all_subsets = []
    for list_subset in all_subsets:
        temp_list_subset = copy.copy(list_subset)
        temp_list_subset.append(list_value[i])
        temp_all_subsets.append(temp_list_subset)

    for list_temp_subset in temp_all_subsets:
        all_subsets.append(list_temp_subset)

    return get_all_subsets(list_value, i+1, all_subsets)

all_subsets = [[]]
all_subsets = get_all_subsets(list_input, 0, all_subsets)

print len(all_subsets)





