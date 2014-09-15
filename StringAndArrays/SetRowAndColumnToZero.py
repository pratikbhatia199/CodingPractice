__author__ = 'pratik'

matrix=[[1,2,0],[3,0,5],[7,8,9]]

def set_to_zero(matrix):
    list_zero_columns = [0]*len(matrix)
    list_zero_rows = [0]*len(matrix[0])
    for i in range(0,len(matrix)):
        if list_zero_columns[i] == -1:
            continue
        for j in range(0, len(matrix)):
            if list_zero_rows[j] == -1:
                continue
            if matrix[i][j]==0:
                list_zero_rows[j]=-1
                list_zero_columns[i]=-1

    print list_zero_columns
    print list_zero_rows
set_to_zero(matrix)



