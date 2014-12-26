__author__ = 'pratik'

dict_num_words = {'1':['1','#','?'],
                  '2':['2','A','B', 'C']}




def list_possibilities(input_str, current_number, dict_num_words, list_possibilities_value):
    if(current_number == len(input_str)):
        return list_possibilities_value
    else:
        list_current_possibilities = dict_num_words[input_str[current_number]]
        temp_possibilities = []
        for possibility in list_possibilities_value:
            for current_possibility in list_current_possibilities:
                temp_possibilities.append(str(possibility)+str(current_possibility))
        return list_possibilities(input_str, current_number+1, dict_num_words, temp_possibilities)


ans = list_possibilities("12", 0, dict_num_words, [''])
print ans
