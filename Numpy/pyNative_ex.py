import numpy as np
import matplotlib.pyplot as pl

"""https://pynative.com/python-numpy-exercise/"""


"""Exercise 1: Create a 4X2 integer array and Prints its attributes
Note: The element must be a type of unsigned int16. And print the following Attributes: –

The shape of an array.
Array dimensions.
The Length of each element of the array in bytes.
Expected Output:

Printing Array

[[64392 31655]
 [32579     0]
 [49248   462]
 [    0     0]]

Printing NumPy array Attributes

Array Shape is:  (4, 2)
Array dimensions are  2
Length of each element of array in bytes is  2"""

# array_42 = np.empty((4,4) , dtype = np.uint16)
# print(array_42)
# print(f"Array Shape is :  {array_42.shape}")
# print(f"Array dimension are  : {array_42.ndim}")
# print(f"Length of each element of array in bytes is :  {array_42.itemsize}")

"""
Exercise 2: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
Expected Output:

Creating 5X2 array using numpy.arange
[[100 110]
 [120 130]
 [140 150]
 [160 170]
 [180 190]]"""
 

# array  = np.arange(100, 192,10)
# array_52 = array.reshape(5 , 2)

# print(array_52)


"""Exercise 3: Following is the provided numPy array. Return array of items by taking the third column from all rows
sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
Expected Output:

Printing Input Array
[[11 22 33]
 [44 55 66]
 [77 88 99]]

Printing array of items in the third column from all rows
[33 66 99]"""

# import timeit
# first = """
# import numpy as np
# sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
# third_column_array = [x[len(sampleArray)-1] for  x in sampleArray]
# print(third_column_array)"""





# second = """
# import numpy as np
# sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
# newArray = sampleArray[...,2]
# print(newArray)"""

# firs1= timeit.timeit(first , number =10)
# second2= timeit.timeit(second , number =10)

# print(firs1 , second2) # 0.0008921129920054227 ||||||||||||| 0.0026368929975433275


"""Exercise 4: Return array of odd rows and even columns from below numpy array
sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
Expected Output:

Printing Input Array
[[ 3  6  9 12]
 [15 18 21 24]
 [27 30 33 36]
 [39 42 45 48]
 [51 54 57 60]]

Printing array of odd rows and even columns
[[ 6 12]
 [30 36]
 [54 60]]"""
 
# sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

# oddColoumn_evenRows = sampleArray.all([ sampleArray[: , ...] // 2 != 0 and  sampleArray[... , :] // 2 == 0 ])
# print(oddColoumn_evenRows)



# sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]]) 
# print("Printing Input Array")
# print(sampleArray)

# print("\n Printing array of odd rows and even columns")
# newArray = sampleArray[::2, 1::2]
# print(newArray)


# arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
# arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

# sum_arrays = arrayOne + arrayTwo 
# print(sum_arrays)

# square_arrays  = sum_arrays**2

# print(square_arrays)
# for x , y in np.nditer([arrayOne , arrayTwo ] , op_flags=['readwrite']):
#     x[...] = x+y
# print("addition of two arrays is \n")
# print(arrayOne)

# for num in np.nditer(arrayOne, op_flags = ['readwrite']):
#    num[...] = num*num
# print("\nResult array after calculating the square root of all elements\n")
# print(arrayOne)




"""
Exercise 9: Delete the second column from a given array and insert the following new column in its place.
"""

sampleArray = np.array([ [[34,43,73],[82,22,12],[53,94,66]]  , np.arange(9).reshape(3,3) ]) 
newColumn = np.array([[10,10,10]]) 

# Array_new = np.delete( sampleArray ,1 , axis = 1 ) 
# Cz we cant insert the entire column or even stack it horizontaly 
# for index , element in enumerate(newColumn[0]) :
#     sampleArray[index,1] = element

print(sampleArray)

#Another Scenario if 
# newColumn = np.array([ [10] , [ 10 ] , [ 10]]) 

# Array_new = np.delete( sampleArray ,1 , axis = 1 ) 
# Array_new = np.hstack( (Array_new , newColumn ) )
# print(Array_new)


x , y = sampleArray[0]  , sampleArray[1]
pl.figure("Exercice 10")
pl.plot(x,y)
pl.show()
pl.close()
