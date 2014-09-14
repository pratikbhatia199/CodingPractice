__author__ = 'pratik'

ways = [1,2,3]

def count_ways(steps):
    if steps<0:
        return 0

    if steps==0:
        return 1

    return count_ways(steps-1)+count_ways(steps-2)+count_ways(steps-5)

print count_ways(10)
