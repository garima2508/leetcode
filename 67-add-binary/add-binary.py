class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a=int(a,2)
        dec_b=int(b,2)
        sum=dec_a+dec_b
        res=bin(sum)[2:]
        return res