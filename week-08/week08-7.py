class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False

        d = {} #空字典
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        #print(d)

        for c in t:
            if c not in d: # 不再統計的字典裡面
                return False # 失敗
            if d[c] <= 0: #不夠
                return False # 失敗
            else:
                d[c] = d[c] - 1

        return True