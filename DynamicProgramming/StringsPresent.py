__author__ = 'pratik'

list_strings = ["ABC","AB","D"]
input_string = "ABCD"

def isSplittable(string):
    print "Input: ",string
    if (string) ==0:
        return True

    if string in list_strings:
        print "Matched", string
        return True

    for i in range(1,len(string)):
        print "Inside loop"
        print string[i:]
        print string[:i]
        print "calling"
        if isSplittable(string[i:]) & isSplittable(string[:i]):
            print "returning true", string[i:], string[:i]
            return True
    return False

x = isSplittable(input_string)
print x