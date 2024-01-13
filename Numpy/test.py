import numpy as np 

# matrix = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12]])

# # Find indices where the value is greater than 5
# indices = np.where(matrix > 5)
# print(indices)
# print(indices[0][3], indices[1])
# # Use these indices to extract the subarray
# result = matrix[[1, 1, 1, 2, 2, 2, 2], [1, 2, 3, 0, 1, 2, 3]]

# # Reshape the result to a 2D array and select columns 1 to 2
# # result = result[:, 1:3]

# print(result)

# Example 3: Reshape to a 2x2x2 3D array (total elements: 8)
# arr3 = np.arange(8)
# reshaped_arr3 = arr3.reshape((2, -1, 2))
# print(reshaped_arr3)


# import numpy as np

# # Creating two arrays
# A = np.ones((2, 2))
# B = np.zeros((2, 2))

# # Concatenating along axis 0 (vertical concatenation)
# result_vertical = np.concatenate((A, B) , axis = 0)
# print(f' {result_vertical} ' )


# matrix = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12]])

# # Extract the main diagonal (k=0)
# main_diagonal = matrix.diagonal()
# print("Main Diagonal:", main_diagonal)

# # Extract the diagonal above the main diagonal (k=1)
# above_main_diagonal = matrix.diagonal(offset=1)
# print("Diagonal Above Main Diagonal:", above_main_diagonal)

# # Extract the diagonal below the main diagonal (k=-1)
# below_main_diagonal = matrix.diagonal(offset=-3)
# print("Diagonal Below Main Diagonal:", below_main_diagonal)


# A = np.array([ [1, 2 ], [3, 4] ])
# B = np.array([ [2, 0], [1, 3]])

# result_matrix_product = np.dot(A, B)
# print(result_matrix_product)

# a = np.arange(4).reshape(2, 2) # [[0 , 1 ] , [2 , 3]] 
# v = np.array([-3, 2])

# result_dot_av = np.dot(a, v)
# result_dot_va = np.dot(v, a)
# print(v )
# print(a)
# print(result_dot_av , result_dot_va)

# Définir une matrice
# A = np.array([[4, -2],
#               [1,  1]])

# # Calculer les valeurs propres et les vecteurs propres
# valeurs_propres, vecteurs_propres = np.linalg.eig(A)

# # Afficher les résultats
# print("Matrice A:")
# print(A)

# print("nValeurs Propres:")
# print(valeurs_propres)

# print("nVecteurs Propres:")
# print(vecteurs_propres)
dim_1D = np.arange(10 , dtype = int)
dim_1D  = dim_1D[-1 : -10]
print(dim_1D)