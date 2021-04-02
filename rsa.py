verbose = False

def get_p():
    print("Enter first prime (p): ")
    return int(input())


def get_q():
    print("Enter second prime (q):")
    return int(input())


def get_p_and_q():
   p = get_p()
   q = get_q()
   return (p, q)


def get_co_primes(p: int, q: int):
    return (p-1)*(q-1)


def GCD(i, n):
    """ Silliest method ever """
    if verbose:
        print(f"Co prime between {i} and {n}")
    for z in range (min(i,n), 0, -1):
        if ((i % z) == 0) and ((n % z) == 0):
            return z

    raise Exception(f"Not GCD found for {i} and {n}")


def coprime(i, n):
    if GCD(i, n) == 1:
        return True

    return False


def get_encryption_key(n, phi):
    # 1 < e < phi
    # e should be co-prime with n and phi

    for i in range (2, phi):
        if coprime(i, n) and coprime(i, phi):
            return i
    raise Exception("Not encryption key found")


def get_decryption_key(e: int, phi: int):
    """ e*d % n == 1"""
    for i in range(1, phi):
        if (e*i % phi) == 1:
            return i
    raise Exception("No decription key found")


def print_all(p: int, q: int, phi: int, e: int, d: int, n: int):
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


def generate_keys():
    print("Generating new keys")
    p, q = get_p_and_q()
    n = p*q
    phi = get_co_primes(p, q)
    e = get_encryption_key(n, phi)
    d = get_decryption_key(e, phi)
    print_all(p, q, phi, e, d, n)
    return e, d, n


def modexp(num, power, mod):
    return pow(num, power) % mod


def encrypted(msg, e, n):
    return modexp(msg, e, n)


def decrypt(msg, d, n):
    return modexp(msg, d, n)


if __name__ == "__main__":
    e, d, n = generate_keys()

    for plain in range(1, n):
        encrypted_message = encrypted(plain, e, n)
        dec = decrypt(encrypted_message, d, n)
        if dec != plain:
            raise Exception("Somthing went wrong..")
        print(f"{plain} - > {encrypted_message} -> {dec}")