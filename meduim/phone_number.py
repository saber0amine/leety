class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        phone_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        digits_legnth = len(digits)
        combination_list = []
        index , fixed  = 0 , 0
        if digits == '0' or digits == '' or digits_legnth > 4 :
            return []   
        elif digits_legnth ==  1 : 
            value = phone_dict[digits]
            for i in range(len(value)):
                combination_list.append(value[i])
            return combination_list
        
        
        
        else :
            dict_value = phone_dict[digits[fixed]]
            for _ in dict_value :                        
                element_fixed = dict_value[fixed]  
                for digit_element in digits[index +1 : ] :  
                    if fixed < len(dict_value) : 
                        element = element_fixed + phone_dict[digit_element][index]   
                        element_fixed = element                       
                        print(element)
                fixed +=1
                combination_list.append(element)

                        
            return combination_list  

s = Solution() 
print(s.letterCombinations("234"))