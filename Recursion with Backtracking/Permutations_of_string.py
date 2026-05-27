
def permutations_of_string(string_file):
    permutations = []
    #result = []
    for i in string_file:
        result = "" 
        if i not in result : 
            result+=i  
        if len(result) == len(string_file) :
            permutations.append([result])
    return permutations

string_file = "123"
result = permutations_of_string(string_file)
print(result)

        