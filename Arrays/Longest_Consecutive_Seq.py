# Find the length of the longest consecutive sequence in a unsorted array of integers. 
def Longest_Consecutive_Seq(nums : list[int]) -> int:
    if not nums : return 0

    num_set = set(nums)
    longest_streak = 0  # Final result to return

    for num in num_set : 
        if num - 1 not in num_set : 
            longest = 1
            while num+longest in num_set : # Loop till every consecutive number is found in the sequence. 
                longest += 1
        longest_streak = max(longest_streak, longest)
    return longest_streak

number_list = [100,33,45,65,12,13,14,15]
Longest = Longest_Consecutive_Seq(nums = number_list)
print(f'The input list is : {number_list}')
print(f'The length of the longest consecutive sequence is : {Longest}')
