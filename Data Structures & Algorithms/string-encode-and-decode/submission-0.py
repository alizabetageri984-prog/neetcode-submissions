
class Solution:

    def encode(self, strs: list[str]) -> str:

        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> list[str]:

        result = []

        i = 0

        while i < len(s):

            j = i

            # Find the separator #
            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Extract the original string
            word = s[j + 1 : j + 1 + length]

            result.append(word)

            # Move to the next string
            i = j + 1 + length

        return result

