import random
import sympy
import time
from sympy import mod_inverse


def generare_p(n):
    return sympy.randprime(2 ** (n - 1) + 1, 2 ** n - 1)


def initializare(m):
    value = 0
    for i in m:
        value = value + ord(i)

    return 2**value


def vec(n, p):
    v = []
    while n != 0:
        v.append(n % p)
        n = n // p

    return v


def horner(y, x, p):
    rez = 0
    nr = len(y)

    for i in reversed(y):
        rez = rez + pow(x, nr) * i
        nr = nr - 1
    return rez % p


def codificare(vector, n, p):
    y = []
    i = 1
    while i <= n:
        y.append(horner(vector, i, p))
        i = i + 1

    return y


def multiply(p1, p2):  # de ad %p
    n = len(p1)
    m = len(p2)
    prod = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            prod[i + j] = (prod[i + j] + p1[i] * p2[j]) % p
    return prod


def add(p1, p2):
    n = len(p1)
    m = len(p2)
    suma = [0] * max(n, m)
    for i in range(n):
        suma[i] = p1[i]
    for i in range(m):
        suma[i] = (suma[i] + p2[i]) % p
    return suma


def worst_inversari(A, z):
    fc = 0
    for i in A:
        produs = 1
        for j in A:
            if j != i:
                produs *= (j * mod_inverse((j - i) % p, p))
        fc += (z[i - 1] * produs) % p
    return fc % p


def k_inversari(A, z):
    fc = 0
    for i in A:
        produs1 = 1
        produs2 = 1
        for j in A:
            if j != i:
                produs1 *= j
                produs2 *= ((j - i) % p)
        fc += (z[i - 1] * produs1 * mod_inverse(produs2, p)) % p
    return fc % p


def Reconstructie(A, z):
    pol = [0]
    for i in A:
        prod1 = [1]
        prod2 = 1
        for j in A:
            if j != i:
                prod1 = multiply(prod1, [-j, 1])
                prod2 = ((prod2 * (i - j)) % p)
        pol = add(pol, [(x * z[i - 1] * mod_inverse(prod2, p)) % p for x in prod1])
    # pol.reverse()
    pol = pol[1:-1]
    return pol


def decodificare(z):
    fc = None
    A = None
    time1 = None
    time2 = None
    start_time = time.time()
    while fc != 0:

        A = random.sample(range(1, len(z) + 1), k + 1)

        fc = worst_inversari(A, z)
    time2 = time.time() - start_time
    start_time2 = time.time()
    while fc !=0:
        fc = k_inversari(A, z)
    time1 = time.time() - start_time2

    print("timpul pentru k(k-1)" ,time2)
    print("timpul pentru k", time1)
    print("A:", A)
    print("fc:", fc)

    print("Decodificare:", Reconstructie(A, z), "\n")


if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        content = f.read()
    p= generare_p(162)

    print("Un numar prim mare (peste 161 biti):", p)

    v=initializare(content)

    y= vec(v, p)
    k=len(y)+1
    print("vectorul initial=",y)
    print(k)
    s=1
    n=k+2*s
   # y = initializare(v)
   # y = initializare(v)
    z = codificare(y,n,p)
    #print(z)
    index=2
    z[2] = 0
    decodificare(z)

