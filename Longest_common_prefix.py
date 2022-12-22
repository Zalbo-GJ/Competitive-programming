class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        minn = min(len(s)for s in strs)
        for i in range(minn):

            letter = strs[0][i]

            for j in strs:
                if j[i] != letter:
                    return ans
            ans+=letter
        return ans
