import math


def get_factor_list(n):

    """
    Use trial division to identify the factors of n.
    1 is always a factor of any integer so is added at the start.
    We only need to check up to n/2, and then add n after the loop.
    """

    factors = [1]

    for t in range(2, (math.ceil((n / 2) + 1))):
        if n % t == 0:
            factors.append(t)

    factors.append(n)

    return factors


def factors(n):

    """
    Generator function leveraging the get_factor_list function.
    """

    return iter(get_factor_list(n))
