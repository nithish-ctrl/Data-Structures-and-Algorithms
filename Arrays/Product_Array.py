# Product of Array Except Self

def product_array(nums : list[int]) -> list[int]: 
    string_list = '*'.join(map(str,nums))
    Product_list = []
    for i in nums : 
        product = eval(string_list.replace(str(i), '1'))
        Product_list.append(product)
    return Product_list



nums = [1,2,3,4]
Product_list = product_array(nums=nums)
print(f'The input list is : {nums}')
print(f'The product of the array except itself is : {Product_list}')