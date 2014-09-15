__author__ = 'pratik'

array_1 = [9,10,15,20,0,5,7]
array_2 = [45,50,20,30,40]


def binary_search_modified(array, start, end, x):
    print array, start, end ,x
    if start>end:
        print "first terminal"
        return -1
    if end>len(array)-1 or start <0:
        print end, len(array)-1
        print "second terminal"
        return -1
    mid = (start+end)/2
    if x == array[mid]:
        print "found at: ", mid
        return mid
    else:
        result = -1
        print "Doing something"
        #which is sorted half
        if array[start] < array[mid]:
            if x < array[mid]:
                result = binary_search_modified(array,start,mid-1,x)
            else:
                result = binary_search_modified(array, mid+1, end,x)
        if result!=-1:
            return result
        if array[mid]<array[end]:
            if x < array[mid]:
                result = binary_search_modified(array,start,mid-1,x)
            else:
                result = binary_search_modified(array, mid+1, end,x)

        if result!=-1:
            return result

        else:
            result = binary_search_modified(array, mid+1, end,x)
            if result!=-1:
                return result

            else:
                result = binary_search_modified(array,start,mid-1,x)
                return result





print len(array_1)-1
print 6>len(array_1)-1

value = binary_search_modified(array_1, 0, len(array_1)-1, 5)

print value