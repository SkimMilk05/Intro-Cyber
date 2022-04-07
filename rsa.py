# Sion Kim sk9uth
# Programming assignment #2

from random import sample
from math import sqrt

# checks if the number n is prime
# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def isprime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

# generates two random prime numbers, where p != q
# https://www.geeksforgeeks.org/python-random-sample-function/
def randomprimes():
    list = range(5,1000000)
    primes = []
    for i in list:
        if isprime(i): primes.append(i)
    chosen = sample(primes, 2)
    return chosen[0], chosen[1]

# returns e, n, d, p, q
def generatekey():    
    # 1. choose two random large prime p and q. compute n = p * q
    p, q = randomprimes()
    n = p * q
    # 2. choose e, 1 < e < n which is relatively prime to (p-1)(q-1)
    e = 65537
    # 3. find d => d*e mod(p-1)(q-1) = 1 or d*e = 1 mod (p-1)(q-1)
    # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    pq_1 = (p -1) * (q-1)
    d = pow(e, -1, pq_1)
    return e, n, d, p, q

# encrypts message m into ciphertext c with public key {e, n}
def encrypt(m, e, n):
    # c = m^e mod n
    return pow(m, e, n)

# decrypts ciphertext c into plaintext m with private key {d,n}
    # m = c^d mod n
def decrypt(c, d, n):
    return pow(c, d, n)


if __name__ == "__main__":
    print("Generating key...")
    e, n, d, p, q = generatekey()
    print("Finished generating key.")
    print("p =", p)
    print("q =", q)
    print("e =", e)
    print("d =", d)
    m = int(input("Enter message: ")) # inputs are integers
    # check if M > pq. If yes, re-generate key until M < pq.
    while (m > p*q):
        print("M > pq. Re-generating key.")
        e, n, d, p, q = generatekey()
        print("Finished generating key.")
        print("p =", p)
        print("q =", q)
        print("e =", e)
        print("d =", d)
    # encrypt and decrypt
    c = encrypt(m, e, n)
    print("Encrypted message =", c)
    print("Decrypted message =", decrypt(c, d, n))



