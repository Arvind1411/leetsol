class Solution:
    save = [-1]*5001
    def __init__(self) -> None:
        if self.save[0]:
            self.save[0] = 0
            self.save[1] = 10
            # 4,6 d
            # 2,8 c
            # 1,3,7,9 b
            # 0 a
            a = b = c = d = 1
            mod = 10**9+7
            for i in range(2,5001):
                new_a = d<<1
                new_b = c+d
                new_c = b<<1
                new_d = a+(b<<1)
                a = new_a%mod
                b = new_b%mod
                c = new_c%mod
                d = new_d%mod
                self.save[i] = a+4*b+2*c+2*d
                
    def knightDialer(self, n: int) -> int:
        s = self.save[n]
        mod = 10**9+7
        while s >= mod:
            s -= mod
        return s