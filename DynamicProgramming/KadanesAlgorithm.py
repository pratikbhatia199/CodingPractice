__author__ = 'pratik'

list_array = [-2,1,-3, 4,-1, 2, 1,-5, 4]

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
