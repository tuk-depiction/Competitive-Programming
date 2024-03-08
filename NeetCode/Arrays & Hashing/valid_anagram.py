from typing import List
from collections import defaultdict, Counter

def valid_anagram(s: str, t: str) -> bool:
    # 1st solution using Counter O(n)
    print(Counter(s), Counter(t))
    
    if Counter(s) == Counter(t):
        return True
    else:
        return False
    
    # 2st using sorted() O(nlogn)
    if sorted(s) == sorted(t):
        return True
    else:
        return False

if __name__ == "__main__":
    s, t = input("Enter 2 strings: ").split(" ")

    print(valid_anagram(s ,t))




