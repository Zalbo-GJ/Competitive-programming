class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        for i in range(len(word)):
            if word[i] in 'aeiou':
                count += (len(word)-i)*(i+1)
        return count