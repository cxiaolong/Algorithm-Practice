from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 使用defaultdict(list)方便append
        tickets_dict = defaultdict(list)
        for i, ticket in enumerate(tickets):
            tickets_dict[ticket[0]].append(ticket[1])
        path = ['JFK']

        def backtrack(start_point):
            if len(path) == len(tickets) + 1:
                return True
            tickets_dict[start_point].sort()
            for _ in tickets_dict[start_point]:
                # 必须及时删除，避免死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                if backtrack(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)
        backtrack(path[0])
        return path


if __name__ == '__main__':
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    s = Solution()
    print(s.findItinerary(tickets1))
    print(s.findItinerary(tickets2))
