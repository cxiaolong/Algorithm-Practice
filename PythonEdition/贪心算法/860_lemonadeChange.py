from typing import List


# 方法1-
class Solution1:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_five = 0
        num_ten = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                num_five += 1
            elif bills[i] == 10:
                num_ten += 1
                num_five -= 1
                if num_five < 0:
                    return False
            else:
                if num_ten:
                    num_ten -= 1
                    num_five -= 1
                    if num_five < 0:
                        return False
                else:
                    num_five -= 3
                    if num_five < 0:
                        return False
        return True



if __name__ == '__main__':
    bills1 = [5, 5, 5, 10, 20]
    bills2 = [5, 5, 10, 10, 20]
    bills3 = [5, 5, 10]
    bills4 = [10, 10]
    s1 = Solution1()
    print(s1.lemonadeChange(bills1))
    print(s1.lemonadeChange(bills2))
    print(s1.lemonadeChange(bills3))
    print(s1.lemonadeChange(bills4))