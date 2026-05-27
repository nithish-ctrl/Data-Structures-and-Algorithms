
def generate_binary_string(n, curr, result):
    if len(curr) == n :
        result.append(curr)
        return
    
    generate_binary_string(n,curr + "0",result)

    if not curr or curr[-1] != "1" :
        generate_binary_string(n, curr + "1", result)

result = []
n = 4
curr = ""
generate_binary_string(n,curr,result)
print(result)
