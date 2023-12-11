class Solution:
    def subtractProduction(self, n: int) -> int:
        s = 0
        mul = 1

        while n > 0:
            digit = n % 10
            s += digit
            mul *= digit

            n //= 10

        return mul - s


soln = Solution()

result = soln.subtractProduction(4421)

print(result)