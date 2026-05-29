# The issue is the sorting makes the pair match wrong - have to put a single tuple into a list and then 
# descending sort acc to value only , this retains the value-weight pair
def Knacksack_problem(values, weights, capacity):
    paired_list = [(value,weight) for value,weight in zip(values,weights)]
    #paired_list.sort(reverse=True)
    iter = 0
    iter=0
    total_weight = 0
    total_value = 0
    while iter<len(paired_list) :
        if (capacity - total_weight) < paired_list[iter][1]:
            required_fraction = (capacity - total_weight)/paired_list[iter][1]
            total_value += paired_list[iter][0] * required_fraction
            break
        else : 
            total_weight += paired_list[iter][1]
            total_value += paired_list[iter][0]
            iter+=1
    return total_value

'''
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
print(Knacksack_problem(val,wt,capacity))

val = [60, 100]
wt = [10, 20]
capacity = 50  
print(Knacksack_problem(val,wt,capacity))
'''
