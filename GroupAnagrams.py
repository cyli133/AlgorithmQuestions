from typing import List

"""
Source of question: https://leetcode.com/problems/group-anagrams/

Approach:
1. Count the frequency of appearance for each letter in each string in the list of strings given.
2. Observation: Strings with the same frequencies are considered anagrams
3. Store the frequency "table" of each string in a tuple of 26 elements
4. Create a hash table with these frequency tuples as the key and the corresponding strings as values (stored as a list 
of strings)
5. Loop through the hashtable and output the requested result as list of lists.

Reasons why the sorting approacch may outperforms my approach:
1. Complexity of my approach for each word is k(access character) + k(access frequency array) + 26(tuple to list) + ...
2. The 26 constant is too huge, in a sense that English words with over 26 in length rarely exist
3. Since the sorting of each word in the sorting approach takes mlogm where m is the length of the word, where m is 
usually MUCH less than 26, mlogm is much less than the constant term 26 in MOST cases.
"""
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = {}
    temparr = [0 for i in range(26)]
    for i in  strs:
        for value in i:
            temparr[ord(value) - 97] += 1
        if tuple(temparr) in hashmap:
            hashmap[tuple(temparr)].append(i)
        else:
            hashmap[tuple(temparr)] = [i]
        temparr = [0 for i in range(26)]
    result = []
    for i in hashmap:
        result.append(hashmap[i])
    return result

