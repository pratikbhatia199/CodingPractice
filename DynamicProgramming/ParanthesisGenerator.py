__author__ = 'pratik'
import copy

def paranthesis_generator(opening_remaining, closing_remaining, list_string):

    if opening_remaining ==0 and closing_remaining==0:
        print ''.join(list_string)

    if opening_remaining > 0:
        temp_list_string = copy.copy(list_string)
        temp_list_string.append('(')
        paranthesis_generator(opening_remaining-1, closing_remaining, temp_list_string)
        if closing_remaining<opening_remaining and closing_remaining>0:
            temp_list_string = copy.copy(list_string)
            temp_list_string.append(')')
            paranthesis_generator(opening_remaining, closing_remaining-1, temp_list_string)


    if closing_remaining > 0 and closing_remaining>opening_remaining:
        list_string.append(')')
        paranthesis_generator(opening_remaining,closing_remaining-1, list_string)



list_solutions = paranthesis_generator(3, 3, [] )
