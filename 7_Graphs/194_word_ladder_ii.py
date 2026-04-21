"""
194. Word Ladder II

Time Complexity: O(V + E + Paths)
Space Complexity: O(V + E + Paths)
"""
from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
            
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    return layer[w]
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i] + c + w[i+1:]
                        if neww in wordSet:
                            newlayer[neww] += [j + [neww] for j in layer[w]]
                            
            wordSet -= set(newlayer.keys())
            layer = newlayer
            
        return []
