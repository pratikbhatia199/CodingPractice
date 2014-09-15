__author__ = 'pratik'
import copy
input_string = "ABC"


list_input_string = list(input_string)
list_permutations = [""]
print "Doing something"

def get_permutations(list_permutations, index, list_input_string):
    print index, list_permutations, list_input_string
    if index == len(list_input_string):
        print index, 'Is equal',
        return list_permutations

    print "Entering"
    print list_permutations
    temp_list_permutations = []
    for permutation in list_permutations:
        print "current permutation: ", permutation
        print len(temp_list_permutations)
        for i in range(0, len(permutation)+1):
            temp_list_current = list(permutation)
            temp_list_current.insert(i, list_input_string[index])
            print temp_list_current
            temp_list_permutations.append(''.join(temp_list_current))

            print temp_list_permutations

    list_permutations.extend(temp_list_permutations)

    return get_permutations(temp_list_permutations, index+1, list_input_string)

list_permutations = get_permutations(['A'], 1, list_input_string)

print "final", list_permutations
