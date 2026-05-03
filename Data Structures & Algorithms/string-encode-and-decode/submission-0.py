class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs:

            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:

        result = []

        i = 0

        while i < len(s):

            # find the # sign

            j = i

            while s[j] != "#":

                j += 1

            # get the length

            length = int(s[i:j])

            # grab the word

            word = s[j+1 : j+1+length]

            result.append(word)

            # move forward

            i = j + 1 + length

        return result