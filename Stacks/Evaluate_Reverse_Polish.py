from Stack import Stack

def evaluate_reverse_polish(arr):
    stack = Stack()
    for i in arr : 
        if i not in "-*/+" : 
            stack.Push(int(i))
        else : 
            a = stack.Pop()
            b = stack.Pop()
            if i == "+" : 
                stack.Push(a + b)
            elif i == "-" : 
                stack.Push(b-a)
            elif i == "*" : 
                stack.Push(a*b)
            elif i == "/" : 
                stack.Push(int(b/a))
    return stack.Pop()

numbers = ["4","13","5","/","+"]
result = evaluate_reverse_polish(numbers)
print(f'The input list is ; {numbers}')
print(f'The result of the evaluation of the reverse polish notattion is {result}')