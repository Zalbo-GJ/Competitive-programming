class Solution:
    def generateParenthesis(self, n):
        def paren(left, right, curr, res):
            if left == 0 and right == 0:
                res.append(curr)
                return

            if left > 0:
                paren(left-1, right, curr + "(", res)

            if right > left:
                paren(left, right-1, curr + ")", res)
            return res
        res = paren(n, n, '', [])

        return res