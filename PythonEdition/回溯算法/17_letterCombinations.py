from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def back_track(index, combination):
            if len(digits) == index:
                combinations.append("".join(combination.copy()))
                return
            digit = digits[index]
            for letter in letter_dict[digit]:
                combination.append(letter)
                back_track(index + 1, combination)
                combination.pop()

        letter_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        combinations = []
        if digits:
            back_track(0, [])
        return combinations


if __name__ == '__main__':
    digits1 = "23"
    digits2 = ""
    digits3 = "2"
    s = Solution()
    print(s.letterCombinations(digits1))
    print(s.letterCombinations(digits2))
    print(s.letterCombinations(digits3))
