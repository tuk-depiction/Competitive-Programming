from typing import List

def contains_duplicate(lst: List[int]) -> bool:
    
    dist_elems = set()

    for x in lst:
        if x in dist_elems:
            return True
        
        dist_elems.add(x)
        
    return False

if __name__ == "__main__":

    lst = [int(x) for x in input("Enter your list here: ").split()]

    print(contains_duplicate(lst))