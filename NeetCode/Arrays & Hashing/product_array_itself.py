from typing import List, Dict
from functools import reduce
from collections import defaultdict, Counter

def product_array_itself(nums: List[int]) -> List[int]:

    res = []
    for idx, num in enumerate(nums):
       
        lst = nums[:idx] + nums[idx+1:]

        multipln = reduce((lambda x, y: x*y), lst)

        res.append(multipln)

    return res

if __name__ == "__main__": 

    nums = [int(x) for x in input().split()]

    print(product_array_itself(nums))