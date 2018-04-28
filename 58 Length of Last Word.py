class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '':
            return 0
        
        return len(s.split(' ')[-1])
