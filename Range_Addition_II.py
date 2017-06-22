class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m*n
        return min(i[0] for i in ops)*min(i[1] for i in ops)

## find the min rectangle