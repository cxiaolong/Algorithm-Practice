from typing import List
import heapq
from collections import deque


# 方法1-暴力匹配（超时）
# time complexity: O((n−k+1)*k)=O(n*k), space complexity: O(n)
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            window = nums[i: i + k]
            res.append(max(window))
        return res


# 方法2：优先队列：大顶堆
# time complexity: O(n*logn), space complexity: O(n)
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]  # Python默认的heapq是小顶堆
        heapq.heapify(q)

        res = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res


# 方法3-单调队列: time complexity: O(n), space complexity: O(k)
# 首先利用容器deque实现单调队列
class MyQueue:
    """每次移动滑动窗口时，pop移除元素，push添加元素，front返回当前移动窗口的最大值"""
    def __init__(self):
        self.q = deque()

    def pop(self, val):
        """
        弹出元素时，比较当前要弹出的元素的数值是否等于队列出口元素的数值，如果相等则弹出
        保证队列是单调递减队列
        """
        if self.q and val == self.q[0]:
            self.q.popleft()

    def push(self, val):
        """如果push的数值大于队列入口元素数值，那么将队列入口元素弹出，直到push的数值小于等于队列的入口元素"""
        while self.q and self.q[-1] < val:
            self.q.pop()
        self.q.append(val)

    def front(self) -> int:
        """查询当前队列里的最大值，直接返回队列出口元素前端"""
        return self.q[0]


class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        for i in range(k):  # 先将k个元素放进去，形成初始的窗口
            que.push(nums[i])
        res = [que.front()]  # 放入第一个窗口的最大值

        for i in range(k, len(nums)):  # 移动窗口
            que.pop(nums[i - k])
            que.push(nums[i])
            res.append(que.front())
        return res


# 方法4-直接利用deque一步实现
class Solution4:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res = [q[0]]

        for i in range(k, len(nums)):
            if q and nums[i - k] == q[0]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])
        return res


if __name__ == '__main__':
    nums1, k1 = [1, 3, -1, -3, 5, 3, 6, 7], 3
    nums2, k2 = [1], 1
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    s4 = Solution4()
    print(s1.maxSlidingWindow(nums1, k1))
    print(s1.maxSlidingWindow(nums2, k2))
    print(s2.maxSlidingWindow(nums1, k1))
    print(s2.maxSlidingWindow(nums2, k2))
    print(s3.maxSlidingWindow(nums1, k1))
    print(s3.maxSlidingWindow(nums2, k2))
    print(s4.maxSlidingWindow(nums1, k1))
    print(s4.maxSlidingWindow(nums2, k2))