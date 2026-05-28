
def max_avg_subarray(arr,k):
    curr_sum = 0
    length = len(arr)
    for i in range(k):
        curr_sum+=arr[i]
    max_avg = curr_sum/k
    for i in range(k,length):
        curr_sum+= arr[i]
        curr_sum-=arr[i-k]
        curr_avg = curr_sum/k
        max_avg = max(curr_avg, max_avg)
        return max_avg
    
arr = [50, 50, 100, -50]
print(max_avg_subarray(arr,2))
    