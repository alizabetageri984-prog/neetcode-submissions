class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            frequency[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            frequency[index] -= 1

        for count in frequency:
            if count != 0:
                return False
        return True

        