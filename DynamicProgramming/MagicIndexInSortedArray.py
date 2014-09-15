__author__ = 'pratik'
array = [-40,-20,-1,1,2,3,5,6,8,12,13]



def binary_search_modified(start, end, array, found):
    if found:
        return found

    if start>end:
        return found

    mid=(start+end)/2
    if array[mid]==mid:
        print "found at position", mid
        return mid

    if array[mid]>mid:
        found =binary_search_modified(start,mid-1, array, found)

    if array[mid]<mid:.
        found=binary_search_modified(start+1, end, array, found)
    return found


answer = binary_search_modified(0,len(array)-1, array, None)
print answer
