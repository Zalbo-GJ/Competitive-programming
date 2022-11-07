class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        words = {
            1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9: "Nine",
            10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen",
            20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety",
            100:"Hundred", 1000:"Thousand", 1000000:"Million", 1000000000:"Billion"
        }
        
        english = ""
        ans = self.wordy(num, english, words)
        return " ".join(ans.split())
        
    def wordy(self,num,english,word):
        if num == 0:
            return english
        elif num < 20:
            english += word[num]
            return english
        
        elif 20 <= num < 100:
            english += word[(num//10)*10] + " " + self.wordy(num%10, english, word)
            return english
        elif 100 <= num <1000:
            english += word[num//100] + " " + word[100] + " " + self.wordy(num%100, english, word)
            return english
        elif 1000 <= num < 1000000:
            english += self.wordy(num/1000, english, word) + " " + word[1000] + " " + self.wordy(num%1000, english, word)
            return english
        elif 1000000 <= num <1000000000:
            english += self.wordy(num/1000000, english, word) + " " + word[1000000] + " " + self.wordy(num%1000000, english, word)
            return english
        else:
            english += self.wordy(num//1000000000, english, word) + " " + word[1000000000] + " " + self.wordy(num%1000000000, english, word)
            return english