"""
class Solution(object):
    def maxProfit(self, prices):

        n = len(prices)
        if n == 0 or n == 1:
            return 0    
                
        if n == 2:
            if prices[0] > prices[1]:
                return 0 
            else:
                return prices[1] - prices[0]
            
            
        flag = 0
        profit = 0
        
        if prices[0] <= prices[1]:
            profit = profit - prices[0]
            flag = 1           
        
        for i in range(1, n-1):
            if prices[i] <= prices[i-1] and prices[i] <= prices[i+1] and flag == 0:
                profit = profit - prices[i]
                flag = 1
            elif (prices[i] >= prices[i-1] and prices[i] >= prices[i+1]) and flag == 1:
                profit =  profit + prices[i]
                flag = 0
                
        if flag == 1:
            profit =  profit + prices[n-1]
        
        return profit
"""

# too much side cases to consider
# draw pic of the price fluctuation to help with analysis
# a neat way of writing this: tracking the valley and peak alternatively, do the addition once a pair is found

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        
        i = 0
        valley = prices[0]
        peak = prices[0]
        profit = 0
        
        while i < len(prices) - 1:
            while i < len(prices) - 1 and valley >= prices[i+1]:
                i = i + 1
            valley = prices[i]
            while i < len(prices) - 1 and peak <= prices[i+1]:
                i = i + 1
            peak = prices[i]
            
            profit = profit + (peak - valley)
        
        return profit
        
                

# the last valley and peak are both prices[-1] which leads to a profit of zero
