from typing import List


# 完全背包
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1, length+1):
            for word in wordDict:
                if i >= len(word):
                    dp[i] = dp[i] or (dp[i-len(word)] and s[i-len(word):i] == word)
        return dp[length]


if __name__ == '__main__':
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    s = Solution()
    print(s.wordBreak(s1, wordDict1))
    print(s.wordBreak(s2, wordDict2))
    print(s.wordBreak(s3, wordDict3))
