from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            # right justifying - SOOOOO helpful. It prefixes the number to make it 3 character string always.
            encoded += str(len(s)).rjust(3, '0')
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i = 0
        lensize = 3
        while i < len(s):
            wordlen = int(s[i:i + lensize])
            i += lensize
            ans.append(s[i:i + wordlen])
            i += wordlen
        return ans