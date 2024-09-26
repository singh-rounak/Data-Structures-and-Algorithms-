class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        res = ''
        for i in range(len(s)):
            if s[i].isalpha():
                res += s[i].lower()

            elif s[i].isalnum():
                res += s[i]

        if res[::-1] == res:
            return True
        return False

        '''
        Time: O(n)
        Space: O(n)

        '''