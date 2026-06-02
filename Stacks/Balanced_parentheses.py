from Stack import Stack

def balanced_parentheses(arr):
    s = Stack()
    for i in arr : 
        if i in "{[(" : 
            s.Push(i)
            print(s.display())
        else : 
            if s.isEmpty() : 
                return False
            top = s.Pop()
            print(s.display())
            if (i == "}" and top == "{") or (i == "]" and top == "[") or (i == ")" and top == "(") :
                continue
            else : return False
    return s.isEmpty()

'''
arr = "()[{}()]"
print(balanced_parentheses(arr))


arr = "[()"
print(balanced_parentheses(arr))

arr = "{[({[]})]}"
print(balanced_parentheses(arr))
'''

