
#First solution : 

# def rotate (matrix : list[list[int]]) :
#     length = len(matrix) - 1 
#     for i in range(length+1) : 
#         for index in range(length + 1 ) : 
#             if i < length - 1 and index <= length - 1: 
#                 tmp = matrix[i][index]
#                 matrix[i][index] = matrix[length-index][i]
#                 matrix[length-index][i] = matrix[length-index][length-i]
#                 matrix[length-index][length-i] = matrix[i][length]
#                 matrix[index][length] = tmp
#             else : 
#                 if i < length and index < length-1 :
#                     print ( i , index ) 
#                     tmp = matrix[i][index] 
#                     matrix[i][index] = matrix[i+1][index+1]
#                     matrix[i+1][index+1] = tmp 

# #Second Solution 
# def rotate (matrix : list[list[int]]) :
#     length = len(matrix) - 1
#     for i in range(length // 2 + 1): #because swapping matrix involvse the pair , so we should iterat just the first middle 
#         for index in range(i, length - i):
#             tmp = matrix[i][index]
#             matrix[i][index] = matrix[length - index][i]
#             matrix[length - index][i] = matrix[length - i][length - index]
#             matrix[length - i][length - index] = matrix[index][length - i]
#             matrix[index][length - i] = tmp

# third solution and the esiest one 
# def rotate(matrix: list[list[int]]):
#     length = len(matrix) - 1
#     for i in range(length // 2 + 1):
#         for index in range(i, length - i):
#             tmp1 = matrix[index][length]
#             matrix[index][length] = matrix[i][index]
#             tmp2 = matrix[length - index][length]
#             matrix[length - index][length] = tmp1
#             tmp1 = matrix[length][index]
#             matrix[length][index] = matrix[length - index][length - index]
#             matrix[length - index][length - index] = tmp2
#             matrix[i][index] = tmp1


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(matrix)
rotate(matrix)
print(matrix)