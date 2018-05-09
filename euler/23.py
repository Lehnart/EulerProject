from sympy.ntheory import divisors
from itertools import combinations_with_replacement


def is_abundant(n):
    if sum(divisors(n)[:-1]) > n:
        return True
    return False


# Find all abundants number below 28123
abundants = []
for n in range(28123):
    if is_abundant(n):
        abundants.append(n)

# Find all pair of abundant numbers
abundant_pairs = [pair for pair in combinations_with_replacement(abundants, 2)]
abundants_pair_sum = set([sum(pair) for pair in abundant_pairs])

# Find integer tha can t be written as the sum of 2 abundant numbers
solution = 0
for n in range(28123):
    if n not in abundants_pair_sum:
        solution += n
print("Solution : " + str(solution))
