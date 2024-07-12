from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = ""
    i = 0
    while (True):
        curr = ''
        for line in strs:
            if (len(line) == i):
                return prefix
            elif (curr == ''):
                curr = line[i]
            elif (line[i] != curr):
                return prefix
        prefix += curr
        i += 1
    return prefix