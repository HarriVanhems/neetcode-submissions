class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_chars(s) == self.count_chars(t)
    
    def count_chars(self, text):
        counts = {}
        for ch in text:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
        return counts



                

