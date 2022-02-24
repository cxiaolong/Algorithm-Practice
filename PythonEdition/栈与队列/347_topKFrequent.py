import heapq
from collections import Counter, defaultdict
from typing import List


# 方法1-Python库函数
# time complexity: O(n*logn), space complexity: O(n)
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most = count.most_common(k)
        return [item[0] for item in most]


# 方法2-堆heap: 小顶堆
# time complexity: O(n*logk), space complexity: O(n)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计所有元素出现的频数
        count = defaultdict(int)
        for item in nums:
            count[item] += 1

        # 定义一个大小为k的小顶堆, 扫描所有元素对应出现的次数
        pri_que = []
        heapq.heapify(pri_que)
        for key, freq in count.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        res = [0] * k
        for i in range(k - 1, -1, -1):
            res[i] = heapq.heappop(pri_que)[1]
        return res


if __name__ == '__main__':
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    nums2, k2 = [1], 1
    s1 = Solution1()
    s2 = Solution2()
    print(s1.topKFrequent(nums1, k1))
    print(s1.topKFrequent(nums2, k2))
    print(s2.topKFrequent(nums1, k1))
    print(s2.topKFrequent(nums2, k2))
