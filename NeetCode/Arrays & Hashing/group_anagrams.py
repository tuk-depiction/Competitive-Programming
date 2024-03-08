from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    ht = defaultdict(list)

    for str in strs:
        # hashmap index must be immutable data type (tuple, pair, integer?)
        immutable_dt = tuple(sorted(str))
        ht[immutable_dt].append(str) 
    
    # or 
    # result = []
    # for value in ht.values():
    #     result.append(value)

    return [value for value in reversed(ht.values())]


if __name__ == "__main__":
    strs = [str(x) for x in input("Enter the list of strings: ").split()]

    print(group_anagrams(strs))

