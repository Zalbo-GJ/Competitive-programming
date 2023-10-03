class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = "".join(key.split(" "))
        cipher = {}
        letter = 0
        for idx in range(len(key)):
            
            if key[idx] not in cipher.keys():
                cipher[key[idx]] = chr(letter + ord('a'))
                letter += 1
            
            idx += 1

        ans = []
        for char in message:
            if char == " ":
                ans.append(char)
                continue
            ans.append(cipher[char ])
        
        return "".join(ans)
   