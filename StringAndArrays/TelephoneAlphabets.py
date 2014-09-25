__author__ = 'pratik'
from copy import copy
dict_no_alphabet = {}
dict_no_alphabet[0]=[]
dict_no_alphabet[1]=['A','B','C']
dict_no_alphabet[2]=['D','E','F']
dict_no_alphabet[3]=['G','H','I']
dict_no_alphabet[4]=['J','K','L']
dict_no_alphabet[5]=['M','N','O']
dict_no_alphabet[6]=['P','Q','R']
dict_no_alphabet[7]=['S','T','U']
dict_no_alphabet[8]=['V','W','X']
dict_no_alphabet[9]=['Y','Z']

number = [7,5,6]

possible_strings = [[]]

#initialization
for i in range(0,len(number)):
    list_temp = []
    for value in dict_no_alphabet[number[i]]:
        for string in possible_strings:
            temp_string = copy(string)
            print value, temp_string
            temp_string.append(value)
            list_temp.append(temp_string)
    possible_strings = copy(list_temp)
    print "possible", possible_strings

print len(possible_strings)


def compute_strings(index_number, list_output):
    if index_number == len(number):
        print list_output
        return

    for alphabet in dict_no_alphabet[number[index_number]]:
        temp_copy = copy(list_output)
        temp_copy.append(alphabet)
        compute_strings(index_number+1, temp_copy)


compute_strings(0,[])
