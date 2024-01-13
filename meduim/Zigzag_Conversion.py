# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         Input: s = "PAYPALISHIRING", numRows = 4
#         Output: "PINALSIGYAHRPI"
#         Explanation:
#         P     I    N
#         A   L S  I G
#         Y A   H R
#         P     I
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         matrix = [[] for _ in range(numRows) ]
#         zigzage_string = []
#         liste = [ zigzage_string.append(char) for char in s ]
#         length = len(matrix) 
#         index = 0 
#         ReveseIndex = 1
        
#         print(zigzage_string , matrix) 
#         for char in zigzage_string : 
#             if length != 0 and index <= len(matrix) -1:
#                 if matrix[index] !== "":
#                 matrix[index].append(char) 
#                 length -= 1
#                 index += 1
#             elif length == 0  and index >= 0 : 
#                 if index - 2 > 0 : 
#                     matrix[index-2].append(char)
#                     index -= ReveseIndex
#                     matrix[index-2].append("")
#                 else :
#                     if index-2 == 0 : 
#                         matrix[index-2].append("")
#                         matrix[index-2].append(char)
#                         index -= 1
#                         length = len(matrix)
#                     # else :
#                     #     matrix[index-2].append(char)
#                     #     index+=1

         
#         print(zigzage_string , matrix) 
   
            
            

#     convert(2 , "PAYPALISHIRING" , 4)
    
    


class Solution(object):
    def convert(self, s, numRows):
        """
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        P     I    N
        A   L S   I G
        Y A   H R
        P     I
        :type s: str
        :type numRows: int
        :rtype: str
        """
        matrix = [[] for _ in range(numRows) ] 
        zigzage_string = []
        liste = [ zigzage_string.append(char) for char in s ]
        print(zigzage_string)
        meduim_lengthOfSting , length= len(zigzage_string) // 2 , len(matrix)
        pas_pattern = numRows // 2 
        i = 1
        j = meduim_lengthOfSting 
        
        for index in range(length) :
            matrix[index].append(zigzage_string[meduim_lengthOfSting - j])
            matrix[index].extend(" "*pas_pattern)
            if pas_pattern > -1 and index != 0 and index < length - 1: 
                pas_pattern += 1
                matrix[index].append(zigzage_string[meduim_lengthOfSting - i]) 
            if pas_pattern == 0 :
                pas_pattern = 1 
                matrix[index].extend(" "*pas_pattern)
            pas_pattern -=1 
            i +=1
            j -= 1  
            print(pas_pattern , i , j)
            
        i = -1
        j = meduim_lengthOfSting      
        for index in range(length) :
                pas_pattern = numRows // 2                                
                print("index" ,matrix , index , i , j)
                matrix[index].append(zigzage_string[meduim_lengthOfSting + i])
                matrix[index].extend(" "*pas_pattern)        
                matrix[index].append(zigzage_string[len(zigzage_string) - 1 + i ])
                pas_pattern -=1 
                i +=1
                j -= 1  

  



        print( zigzage_string ,matrix)        
            
    convert(2 , "PAYPALISHIRING" , 4)