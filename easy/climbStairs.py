class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        else:
            prev_2 = 1
            prev_1 = 2
            curr = 0
            for i in range(2, n):
                curr = prev_1 + prev_2
                prev_2 = prev_1
                prev_1 = curr
            return curr