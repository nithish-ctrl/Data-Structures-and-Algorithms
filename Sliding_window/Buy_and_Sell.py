"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# Topic - Sliding window, Array 

def Buy_and_Sell(prices: list[int]) -> int:
    buy = prices[0]
    profit = 0 
    
    for i in range(1,len(prices)):
        if prices[i] < buy : 
            buy = prices[i]
        elif prices[i] - buy > profit :
            profit = prices[i] - buy

    return profit

prices = [7,1,5,3,6,4]
result = Buy_and_Sell(prices=prices)
print(f'The input list is : {prices}')
print(f'The maximum profit that can be made : {result}')    