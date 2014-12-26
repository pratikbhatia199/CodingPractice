__author__ = 'pratik'

list_array = [-2,1,-3, 4,-1, 2, 1,-5, 4]



def partition(low, high):
    mid = (low+high)/2
    list_array[high], list_array[mid] = list_array[mid], list_array[high]
    j = -1
    for i in range(low, high):
        if list_array[i]<list_array[mid]:
            j+=1
            list_array[j], list_array[i] = list_array[i], list_array[j]

    list_array[j+1], list_array[high] = list_array[high], list_array[j+1]
    return j+1

def quicksort(low, high):
    if low < high:
        part = partition(low, high)
        quicksort(low, part-1)
        quicksort(part+1, high)

quicksort(0, len(list_array)-1)
print list_array




max_sum = -1000
max_end = -1
current_sum = 0
for i, value in enumerate(list_array):
    print i, value
    current_sum += value
    if current_sum > max_sum:
        max_sum = current_sum
        max_end = i

    if current_sum<0:
        current_sum = 0

print "Max sum is:", max_sum
print "Max end is:", max_end





"""

max_value = 0
max_index = ""
sum=0
start_index=0
start_index=[]
for i in range(0, len(list_array)):
    print sum, i, max_value, start_index
    if sum+list_array[i]>0:
        if sum>0:
            start_index.insert(i,start_index[i-1])
        else:
            start_index.insert(i,i)
        sum=sum+list_array[i]
    else:
        start_index.insert(i,i)
        sum=0
        continue

    if (sum>max_value):
        max_index = i
        max_value = sum



print max_value
print max_index
print list_array[3:7]
"""""