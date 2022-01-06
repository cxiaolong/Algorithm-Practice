from typing import List


# 方法1-
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged



if __name__ == '__main__':
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals2 = [[1, 4], [4, 5]]
    s1 = Solution1()
    print(s1.merge(intervals1))
    print(s1.merge(intervals2))