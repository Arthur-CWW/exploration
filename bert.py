def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sqrt(n: int):
    return int(n**0.5) + 1


def factorise(n: int):
    factors = []
    i = 2
    while n > 1:
        for i in range(2, sqrt(n)):
            if n % i == 0:
                factors.append(i)
                n = n // i
                print(n, i)
                break

        if is_prime(n):
            factors.append(n)
            break
    return factors


if __name__ == "__main__":
    """
    This doc is trying to find out why 768 is used and important in nlp transformers
    """

    print(f := factorise(768))  # [2, 3, 2, 2, 2, 2]
    cum = 1
    [cum := cum * i for i in f]

    print(f"{' * '.join(map(str, f))} = {cum}")
