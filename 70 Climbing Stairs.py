class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dp(n, {})
        
    def dp(self, n, dic):
        if n == 0 or n == 1:
            dic[n] = 1
            return dic[n]
        if n not in dic:
            dic[n] = self.dp(n-1, dic) + self.dp(n-2, dic)
        return dic[n]

# record already take steps to avoid time limit exceed
