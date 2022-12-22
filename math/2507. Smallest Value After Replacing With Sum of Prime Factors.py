class Solution:
    def smallestValue(self, n: int) -> int:
        factors = self.get_primes(n)
        while len(factors) != 1:
            if n == sum(factors):
                return n
            factors = self.get_primes(sum(factors))
        return factors[0]

    def get_primes(self, n):
        res = []
        while n % 2 == 0:
            n //= 2
            res.append(2)
            # if n == 1:
            #     return res
        for factor in range(3, n + 1, 2):
            while n % factor == 0:
                n //= factor
                res.append(factor)
        if n > 2:
            res.append(n)
        return res