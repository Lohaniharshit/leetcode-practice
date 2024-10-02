from collections import defaultdict

def groupAnagrams1(strs): # passed

    anagram_map = defaultdict(list) # default value is an empty list. Can be integer, string ,etc
    result = []

    for s in strs:
        sorted_s = tuple(sorted(s)) # sorted returns a list so use tuple
        anagram_map[sorted_s].append(s)

    for value in anagram_map.values():
        result.append(value)
    return result





if __name__ == '__main__':
    groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"])
