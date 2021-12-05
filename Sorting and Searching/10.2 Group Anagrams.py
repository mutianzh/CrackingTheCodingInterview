"""
10.2 Group Anagrams: Write a method to sort an array ot strings so that all tne anagrnms are next to
each other.
"""

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            groups[key].append(s)

        values = ''.join(groups.values())
        ans = []
        for group in values:
            ans += group

        return ans