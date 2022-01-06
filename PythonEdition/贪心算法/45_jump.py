from typing import List


class Solution1:
    def jump(self, nums: List[int]) -> int:
        cur_distance = 0  # 当前可以跳跃的最远距离下标
        next_distance = 0  # 下一步可以跳跃的最远距离下标
        res = 0  # 总共需要跳跃的次数
        for i in range(len(nums)):
            next_distance = max(next_distance, i + nums[i])
            if i == cur_distance:  # 如果当前走到了最远距离的下标
                if cur_distance != len(nums) - 1:  # 如果当前没有走到头
                    res += 1  # 需要继续跳跃
                    cur_distance = next_distance
                    if next_distance >= len(nums) - 1:
                        break
        return res


class Solution2:
    # 考虑当前最远可以跳跃到终点的前一步，则再跳跃一步即可到达终点
    def jump(self, nums: List[int]) -> int:
        cur_distance = 0
        next_distance = 0
        res = 0
        for i in range(len(nums) - 1):
            next_distance = max(next_distance, nums[i] + i)
            if i == cur_distance:  # 如果遍历到了当前可以跳跃到的最远距离，则需要再跳跃一步
                cur_distance = next_distance
                res += 1
        return res


if __name__ == '__main__':
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [2, 3, 0, 1, 4]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.jump(nums1))
    print(s1.jump(nums2))
    print(s2.jump(nums1))
    print(s2.jump(nums2))
