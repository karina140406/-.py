def is_anagram(str_1, str_2):   
    str_1 = str_1.lower()  
    str_2 = str_2.lower()   
    return sorted(str_1) == sorted(str_2)   
str_1 = input()
str_2 = input()
result = is_anagram(str_1, str_2)  
print(result)