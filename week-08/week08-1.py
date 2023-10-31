 # 題目給你數字n請回答return ture還是return false
        # 如果他是2的很多次方那就return ture ex. 1 2 4 8 16 32 64 128...
        # 不是的話false 例 N % 2 餘數不是0，就失敗了
        # 要把N慢慢變小
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n>1:
            if n % 2 !=0: #驚嘆號是判斷
                 return False
            else:
                n = n // 2 #要變小

        return True        
