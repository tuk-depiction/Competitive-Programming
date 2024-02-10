from typing import List

def binary_search(lst: List[int], low: int, high: int, x: int) -> int:
    if (low >= high): return -1

    mid = (low + high) // 2

    if (lst[mid] == x): return mid
    elif (x < lst[mid]): return binary_search(lst, low, mid - 1, x)
    else: return binary_search(lst, mid+1, high, x)

def two_sum(lst: List[int], target: int) -> int: 
    for idx, num in enumerate(lst):
        diff = target-num
        found_idx = binary_search(lst, 0, len(lst)-1, diff)

        if found_idx != -1 and found_idx != idx: return sorted([idx, found_idx])

    return False

def two_sum_optz(lst: List[int], target: int) -> int:
    hash = {} # val -> index

    for idx, num in enumerate(lst):
        diff = target - num
        if diff in hash:
            return [hash[diff], idx]
        
        hash[num] = idx # index -> hash[val]
if __name__ == "__main__":
    # Multiple line input
    lst = [int(x) for x in input("Enter the list of numbers: ").split()]
    target = int(input("Enter a target: "))

    print(two_sum(lst, target))
    print(two_sum_optz(lst, target))