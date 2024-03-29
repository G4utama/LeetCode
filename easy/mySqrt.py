class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        else:
            l = 1
            r = x
            while l <= r:
                m = (l+r)//2
                temp = m*m
                if temp == x:
                    return m
                elif temp < x:
                    l = m+1
                else:
                    r = m-1
            return l-1