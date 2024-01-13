class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        result = 0 
        Roman_dict = {'I' : 1, 'V': 5 ,'X' :10 ,'L' : 50, 'C' :100 ,'D':500 ,'M' :1000 }
        for _ in s :
                if index < len(s)  - 1 and Roman_dict[s[index]] < Roman_dict[s[index+ 1]] :
                    result -= Roman_dict[s[index]] 
                    index += 1
                else : 
                    result += Roman_dict[s[index]]
                    index += 1 

 
        print( result )   
    

    romanToInt(1 ,"MCDXCIV")  1000 400 90 4