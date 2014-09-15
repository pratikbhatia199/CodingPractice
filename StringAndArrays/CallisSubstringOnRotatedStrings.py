__author__ = 'pratik'

str_1 = "waterbottle"
str_2 = "tlewaterbot"

list_str_1 = list("waterbottle")
list_str_2 = list("tlewaterbot")


j=0
match_index = -1
while(j<len(list_str_1) and match_index==-1):
    if list_str_1[0]==list_str_2[j]:
        match_index=j
    else:
        j=j+1
i=0
while(j<len(str_1)):
    if list_str_1[i]==list_str_2[j]:
        i=i+1
        j=j+1
    else:
        break

if j!=len(str_1):
    print "There is no match"
else:
    print ''.join(list_str_1[i:len(list_str_1)])