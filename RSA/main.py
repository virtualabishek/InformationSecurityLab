import random

# just check if the num is prime ot not
def primeChecking(num):
    if num<2:
        return False
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
#function to just compute greatest gcd

def gcdChecker(a, b):
    while b!=0:
        a,b = b, a %b
    return a

# function to find the modular inverse using the extended Euclidean algorithm

def modularInverse(e, phi):
    def extendedGCD(a,b):
        if a ==0:
            return b, 0, 1
        gcd, x1, y1 = extendedGCD(b%a, a)
        x = y1 - (b // a)* x1
        y = x1
        return gcdChecker, x,y
    gcdChecker, x, _ = extendedGCD(e, phi)
    if gcdChecker != 1:
        return ValueError("No modular inverse exists for that")
    return x % phi

# function to generate RSA Public and private keys

def generateKeys(p,q):
    if not primeChecking(p) and primeChecking(q):
        raise ValueError("Both number should be prime");
    n = p*q
    phi = (p-1) * (q-1)
        # choosing random so that is compromise to  phi

    e = random.randrange(1, phi)
    while gcdChecker(e, phi) != 1:
        e = random.randrange(1, phi)

        # Compute d, the modular inverse of e modulo phi
    d = modularInverse(e, phi)
    return (e,n), (d,n)

# Function to encrypt a message

def encryptMessage(message, publicKey):
    e, n = publicKey
    if message >=n:
        raise ValueError("Messaes must be greater than n.")
    return pow(message, e,n)

# Function to decrypt a ciphertext

def decryptMessage(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

# example,using just simple number as greater will be complex mathematically
p = 17
q = 11
publicKey, privateKey = generateKeys(p,q)
message = 7


print(f"Public key (e, n): {publicKey}")
print(f"Private key (d, n): {privateKey}")
print(f"Original message: {message}")

ciphertext = encryptMessage(message, publicKey)
print(f"Ciphertext: {ciphertext}")

print(f"Decrypted message: {decryptMessage}")
decrypted_message = (ciphertext, privateKey)
print(f"Decrypted message: {decrypted_message}")