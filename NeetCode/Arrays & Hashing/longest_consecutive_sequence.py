from typing import List, Dict
from collections import Counter, defaultdict

class LongestConsecutive:
    def search(self, nums: List[int], target: int) -> bool:
        return any(target == num for num in nums)
    
    def longestConsecutve(self, nums: List[int]) -> int:

        maxCon = 0

        for num in nums:

            currCon = 1
            isFound = True
            i = 0

            while isFound:
                i += 1

                if self.search(nums, num+i):
                    currCon += 1
                    maxCon = max(maxCon, currCon)
                else:
                    isFound = False

        return maxCon
    
    def optimized(self, nums: List[int]) -> int:

        maxCon = 0
        ht = set(nums)


        for num in nums:

            currCon = 1
            isFound = True
            i = 0

            while isFound:
                i += 1

                if num+i in ht:
                    currCon += 1
                    maxCon = max(maxCon, currCon)

                else:
                    isFound = False

        return maxCon
    

if __name__ == "__main__":
    lst = [int(x) for x in input("Enter a list: ").split()]
    solution = LongestConsecutive()

    print(solution.longestConsecutve(lst))
    print(solution.optimized(lst))