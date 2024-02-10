import typing
from collections import Counter

def valid_anagram(txt1: str, txt2: str) -> bool:

    length = 256 # which is long strings

    if len(txt1) > length or len(txt2) > length:
        # For checking if the length of any strings is large
        return Counter(txt1) == Counter(txt2)

    # Efficient for only small sized strings
    else: return sorted(txt1) == sorted(txt2)

if __name__ == "__main__":
    txt1, txt2 = input("Enter strings: ").split(" ")

    print(valid_anagram(txt1, txt2))
