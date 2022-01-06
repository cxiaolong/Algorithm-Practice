from typing import List


# 方法1-暴力法：模拟
class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            res = gas[i] - cost[i]
            index = (i + 1) % len(gas)
            while res >= 0 and i != index:
                res += gas[index] - cost[index]
                index = (index + 1) % len(gas)
            if res >= 0 and i == index:
                return i
        return -1


# 方法2-
class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0  # 当前油箱里油的数量
        min_gas = float('inf')  # 记录从起点开始出发，油箱里油的最小值
        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            cur_sum += rest
            min_gas = min(min_gas, cur_sum)
        if cur_sum < 0:
            return -1
        if min_gas >= 0:
            return 0
        for j in range(len(gas)-1, 0, -1):
            rest = gas[j] - cost[j]
            min_gas += rest
            if min_gas >= 0:
                return j
        return -1


# 方法3-贪心算法
class Solution3:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index = 0
        cur_sum = 0  # 当前剩余油量的和
        total_sum = 0  #
        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            cur_sum += rest
            total_sum += rest
            if cur_sum < 0:
                cur_sum = 0
                start_index = i + 1
        if total_sum < 0:
            return -1
        return start_index


if __name__ == '__main__':
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.canCompleteCircuit(gas1, cost1))
    print(s1.canCompleteCircuit(gas2, cost2))
    print(s2.canCompleteCircuit(gas1, cost1))
    print(s2.canCompleteCircuit(gas2, cost2))
    print(s3.canCompleteCircuit(gas1, cost1))
    print(s3.canCompleteCircuit(gas2, cost2))