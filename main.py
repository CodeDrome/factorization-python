import factorization


def main():

    """
    Test the get_factor_list function and factors generator on a few numbers.
    """

    print("-----------------\n|")
    print("| codedrome.com |")
    print("| Factorization |")
    print("-----------------\n")

    numbers_to_factorize = [15,19,25,50,77,99]

    print("factorization.get_factor_list\n-----------------------------")

    for n in numbers_to_factorize:

        factors = factorization.get_factor_list(n)

        print("Factors of {}: {}".format(n, factors))

    print("\nfactorization.factors (generator)\n---------------------------------")

    for n in numbers_to_factorize:

        print("Factors of {}: ".format(n), end="")

        for f in factorization.factors(n):
            print("{} ".format(f), end="")

        print("")


main()
