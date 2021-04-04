verbose = False


def get_p() -> int:
    # return 23
    print("Example of prime numbers: 3 5 7 11 13 17 19 23 31 37 41 43 47 53 59 61 ...")
    print("Enter first prime (p) : ", end="")
    return int(input())


def get_q() -> int:
    # return 31
    print("Enter second prime (q) :", end="")
    return int(input())


def isprime(q: int) -> bool:
    """Sillest method to calculate if a number is prime"""
    for i in range(2, q):
        if q % i == 0:
            if verbose:
                print(f"{q} is not prime. It is divided by {i}")
            return False
    return True


def get_p_and_q() -> (int, int):
    p = get_p()
    q = get_q()
    if not isprime(p) or not isprime(q):
        raise Exception("Number not prime")
    if p == q:
        raise Exception("You need two different numbers")
    return p, q


def get_co_primes(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def GCD(i: int, n: int) -> int:
    """ Silliest method ever """
    if verbose:
        print(f"Co prime between {i} and {n}")
    for z in range(min(i, n), 0, -1):
        if ((i % z) == 0) and ((n % z) == 0):
            return z

    raise Exception(f"Not GCD found for {i} and {n}")


def coprime(i: int, n: int) -> int:
    if GCD(i, n) == 1:
        return True

    return False


def get_encryption_key(n: int, phi: int) -> int:
    # 1 < e < phi
    # e should be co-prime with n and phi

    for i in range(2, phi):
        if coprime(i, n) and coprime(i, phi):
            return i
    raise Exception("Not encryption key found")


def get_decryption_key(e: int, phi: int) -> int:
    """ e*d % n == 1"""
    for i in range(1, phi):
        if (e * i % phi) == 1:
            return i
    raise Exception("No decription key found")


def print_all(p: int, q: int, phi: int, e: int, d: int, n: int) -> None:
    if not verbose:
        return
    print(f"p    = {p}")
    print(f"q    = {q}")
    print(f"phi  = {phi}")
    print(f"=========")
    print(f"n    = {n}")
    print(f"e    = {e}")
    print(f"d    = {d}")
    pass


def generate_keys() -> (int, int, int):
    p, q = get_p_and_q()
    n = p * q
    phi = get_co_primes(p, q)
    e = get_encryption_key(n, phi)
    d = get_decryption_key(e, phi)
    print_all(p, q, phi, e, d, n)
    return e, d, n


def modexp(num: int, power: int, mod: int) -> int:
    return pow(num, power) % mod


def encrypted(msg: int, e: int, n: int) -> int:
    return modexp(msg, e, n)


def decrypt(msg: int, d: int, n: int) -> int:
    return modexp(msg, d, n)


def convert(char: str) -> int:
    """Convert character to int"""
    return ord(char)


if __name__ == "__main__":
    e, d, n = generate_keys()

    print("Message to encode: ", end="")
    msg = input()

    print("Plain Text : ", end="")
    for char in msg:
        print(f"{char.ljust(5)}", end="")
    print("\nIn ASCII   : ", end="")
    for char in msg:
        print(f"{str(convert(char)).ljust(5)}", end="")


    # Encode
    print("\nCiphered   : ", end="")
    ciphered_msg = []
    for char in msg:
        cipher = encrypted(convert(char), e, n)
        ciphered_msg.append(cipher)
        print(f"{str(cipher).ljust(5)}", end="")

    # Delete the encryption key
    del e

    # Decode
    print("\nDecrypted  : ", end="")
    deciphered_msg = []
    for cipher in ciphered_msg:
        decypted = decrypt(cipher, d, n)
        deciphered_msg.append(decypted)
        print(f"{str(decypted).ljust(5)}", end="")

    print("\nPlain Text : ", end="")
    for char in deciphered_msg:
        print(f"{chr(char).ljust(5)}", end="")
    print("")
    # for plain in range(1, n):
    #     encrypted_message = encrypted(plain, e, n)
    #     dec = decrypt(encrypted_message, d, n)
    #     if dec != plain:
    #         raise Exception("Something went wrong.. ")
    #     print(f"{plain} - > {encrypted_message} -> {dec}")
