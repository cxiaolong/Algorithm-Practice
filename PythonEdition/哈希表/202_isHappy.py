# 方法1-用哈希表存储产生过的数字
class Solution1:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            sum_ = 0
            while num > 0:
                num, digit = divmod(num, 10)
                sum_ += digit ** 2
            return sum_

        visit = set()
        while n != 1 and n not in visit:
            visit.add(n)
            n = get_sum(n)

        return n == 1


# 方法2-快慢指针法：反复调用get_sum得到的是一个隐式的链表，因此可以用"弗洛伊德循环查找算法"
class Solution2:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            sum_ = 0
            while num > 0:
                num, digit = divmod(num, 10)
                sum_ += digit ** 2
            return sum_

        slow = n
        fast = get_sum(n)
        while fast != 1 and fast != slow:
            slow = get_sum(slow)
            fast = get_sum(get_sum(fast))

        return fast == 1


if __name__ == '__main__':
    n1 = 19
    n2 = 2
    s1 = Solution1()
    s2 = Solution2()
    print(s1.isHappy(n1))
    print(s1.isHappy(n2))
    print(s2.isHappy(n1))
    print(s2.isHappy(n2))