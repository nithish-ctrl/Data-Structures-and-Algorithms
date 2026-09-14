'''
Problem: Given a string of brackets `()[]{}`, determine if it's valid (properly closed and nested).
'''

def Valid_Parantheses(s):
    stack = []
    mapp = {')' : '(', '}' : '{', ']' : '['}
    for char in s :
        if char in mapp.values():
            stack.append(char)
        elif char in mapp.keys():
            if mapp[char] == stack[-1] :
                stack.pop()
    return not stack

s = "()[]{}"
print(Valid_Parantheses(s))

s = "(]"
print(Valid_Parantheses(s))
