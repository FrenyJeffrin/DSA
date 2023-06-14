import math
class Solution:
    def exactly3Divisors(self,N):
        count = 0
        for i in range(2, int(math.sqrt(N)) + 1):
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime and i * i <= N:
                count += 1
        return count