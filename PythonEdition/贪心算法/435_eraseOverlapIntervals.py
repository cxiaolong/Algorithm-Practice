from typing import List


# 方法1-
class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                res += 1
                intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])
        return res


if __name__ == '__main__':
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    intervals3 = [[1, 2], [2, 3]]
    s1 = Solution1()
    print(s1.eraseOverlapIntervals(intervals1))
    print(s1.eraseOverlapIntervals(intervals2))
    print(s1.eraseOverlapIntervals(intervals3))
