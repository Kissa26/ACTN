#cand e mai  recomadat sa folosesc lehmer
# când numărul este de forma unui număr Mersenne.care au forma 2^p - 1

# Solovay-Strassen (Jacobi symbol)
import random
import time

def jacobi_symbol(a, n):
    jacobi = 1

    if a == 1 or a == 0:
        return a
    #
    # if a < 0:  # (-1/n) = (-1) ** [(n-1)/2]
    #     a = -a
    #     if n % 4 == 3:
    #         jacobi = -jacobi

    while a:
        if a < 0:
            a = -a
            if n % 4 == 3:
                jacobi = -jacobi

        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                jacobi = -jacobi

        if a < n:
            a, n = n, a

        if a % 4 == 3 and n % 4 == 3:  # reciprocitate
            jacobi = -jacobi
        a = a % n  # reducere

        if a > n // 2:
            a = a - n

    if n == 1:
        return jacobi
    return 0


def Solovay_Strassen(n):
    ok = 1
    for i in range(100):
        a = random.randint(2, n - 1)
        jacobian = ( jacobi_symbol(a, n)) % n

        if jacobian == 0 or pow(a, int((n - 1) / 2), n) != jacobian:
            ok = 0
    if ok == 1:
        print(f"{n}: prime")
    else:
        print(f"{n}: not prime")


# Lucas-Lehmer (Mersenne numbers)
def Mersenne(s, M):
    A1 = 0
    while s >= (M + 1):
        A1 += 1
        s -= (M + 1)

    A0 = s
    if A1 + A0 == M:
        return 0
    elif A1 + A0 < M:
        return A1 + A0
    else:
        return A1 + A0 - M


def Lucas_Lehmer(n):
    s = 4
    M = 2 ** n - 1

    for i in range(n - 2):
        s = Mersenne(s * s - 2, M)

    if s == 0:
        print(f"{M}: prime")
    else:
        print(f"{M}: not prime")


n1 = 8388617
n2 = 20
start_time = time.time()
Solovay_Strassen(n1)
end_time = time.time()
execution_time_ss = end_time - start_time

# Măsurarea timpului de execuție pentru Lucas-Lehmer
start_time = time.time()
Lucas_Lehmer(n2)
end_time = time.time()
execution_time_ll = end_time - start_time

print("Timpul de execuție Solovay-Strassen:", execution_time_ss)
print("Timpul de execuție Lucas-Lehmer:", execution_time_ll)