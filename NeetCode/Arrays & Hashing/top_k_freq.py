from typing import List, Dict
from collections import defaultdict, Counter

def top_k_freq(nums: List[int], k: int) -> List[int]:

    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1

    res = dict(sorted(counter.items(), key=lambda x:x[1], reverse=True))

    return [k for k in res.keys()][0:k]

if __name__ == "__main__": 

    nums = [int(x) for x in input().split()]
    k = int(input())

    print(top_k_freq(nums, k))