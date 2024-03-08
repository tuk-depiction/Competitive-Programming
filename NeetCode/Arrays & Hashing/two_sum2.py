from typing import List
from collections import defaultdict, Counter

def two_sum(nums: List[int], tar: int) -> List[int]:
    ht = defaultdict(int)

    for i, num in enumerate(nums):
        diff = tar - num

        if diff in ht:
            return [ht[diff] ,i]
        
        # due to the conflict of found the element itself first
        ht[num] = i
        
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter list of numbers: ").split()]
    target = int(input("Input target value: "))

    print(two_sum(nums, target))

