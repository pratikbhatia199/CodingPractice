__author__ = 'pratik'


def return_num_of_set_bits(n):

    count = 0
    while(n>0):
        if (n)&1:
            count += 1
        n >>= 1
        print n
    return count


print return_num_of_set_bits(4)
