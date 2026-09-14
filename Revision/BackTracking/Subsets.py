
def Subsets(nums):
    res = []
    sett = []

    def backtrack(start):
        if start == len(nums):
            res.append(sett[:])
            return 
        sett.append(nums[start])
        backtrack(start+1)
        sett.pop()
        backtrack(start+1)
    backtrack(0)
    return res


nums = [1,2,3]
print(Subsets(nums))