from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        print(f"Initial array: {ans}")
        for i in range(1, n + 1):
            prev = i >> 1
            bit = i & 1
            ans[i] = ans[prev] + bit
            print(f"i = {i} (binary: {bin(i)[2:]}), ans[{i}] = ans[{prev}] ({ans[prev]}) + {bit} = {ans[i]}")
        print(f"Final array: {ans}")
        return ans

# Test
sol = Solution()
print(sol.countBits(5))