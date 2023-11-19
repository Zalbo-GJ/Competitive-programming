class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = map(str, digits)
        num = int("".join(num))

        return list(map(int, str(num + 1)))