__author__ = 'pratik'
import sys

TwoDArray = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
OneDArray = [1,3,4,6]
#OneDArray = [1,2,3,4]


def find_one_d_in_two_d(TwoDArray, OneDArray, i, j, index):
    if i>=len(TwoDArray) or j >=len(TwoDArray[0]) or i<0 or j<0:
        print "index exeeded", i, j
        return False

    if index == len(OneDArray):
        print "------Base case----"
        return True

    print "testing:", TwoDArray[i][j], OneDArray[index], index, i, j

    if TwoDArray[i][j] == OneDArray[index]:
        print "Test passed"
        if find_one_d_in_two_d(TwoDArray, OneDArray, i-1, j, index+1):
            return True
        if find_one_d_in_two_d(TwoDArray, OneDArray, i+1, j, index+1):
            return True

        if find_one_d_in_two_d(TwoDArray, OneDArray, i, j-1, index+1):
            return True

        if find_one_d_in_two_d(TwoDArray, OneDArray, i, j+1, index+1):
            return True
    return False


for i in range(0, len(TwoDArray)):
    for j in range(0, len(TwoDArray)):
        if find_one_d_in_two_d(TwoDArray, OneDArray, i, j, 0):
            print i,j, "True", '----------------------'
        else:
            print i, j, "False", '------------'
