"""

"""

# Topic - Two Pointers, String

def Valid_Palindrome(s) -> bool:
    #s = ''.join(filter(str.isalnum, s)).lower()  #does the same
    s = ''.join([i for i in s if i.isalnum()]).lower()  
    left, right = 0, len(s)-1
    
    while left<right : 
        if s[left] != s[right] :
            return False
        left += 1
        right -= 1
    return True

str = "race e car"
print(f' The input string is : {str}')
print(f' The given string is a palindrome : {Valid_Palindrome(str)} ')