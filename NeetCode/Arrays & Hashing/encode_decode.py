from typing import List
from collections import Counter, defaultdict

class encode_decode:
    
    def __init__(self, st: List[str]):
        self.res = st

    def encode(self) -> List[str]:
        res = ""
        for s in self.res:
            res += str(len(s)) + "#" + s;
            
        return res

    def decode(self) -> List[str]:
        
        res = []
        s = self.encode()

        i = 0
        while (i < len(s)):

            print(s[i:i+1])
            length = int(s[i:i+1])

            if s[i+1:i+2] == "#":
                start = i+2
                end = start + length

                res.append(s[start:end])
                i += length + 2

        return res

if __name__ == "__main__":
    s = [str(x) for x in input().split()]

    enc_dec = encode_decode(s)
    #print(enc_dec.encode())
    print(enc_dec.decode())