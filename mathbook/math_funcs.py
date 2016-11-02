# !/usr/bin/python

import math


def mmc(n, m):
    n_max = max(n, m)
    n_min = min(n, m)

    n_mmc = (n_max * n_min) / mdc(n_max, n_min)

    return n_mmc


def mdc(n, m):
    # Algoritimo de Euclides que diz se um numero 'a' eh a soma de dois outros numeros a = b+c
    # se um numero 'd' eh divisor de 'a' e 'b' entao necessariamente ele eh divisor de 'c'
    # entao eh utilizado o artificio n = am + r  === onde r eh o resto da divisao de m/a

    n_max = max(n, m)
    n_min = min(n, m)
    r = n_max % n_min
    if r == 0:
        return n_min
    else:
        return mdc(n_min, r)


def mmc2(list):
    mmc_primeFactors = []
    for number in list:
        numberFactors = []
        numberFactors = primeFactors(number)
        if not mmc_primeFactors:
            mmc_primeFactors = numberFactors
        else:
            for p in mmc_primeFactors:
                if p in numberFactors:
                    numberFactors.remove(p)
            mmc_primeFactors += numberFactors
    mmc = 1
    for number in mmc_primeFactors:
        mmc *= number
    return mmc


def mdc2(list):
    mdc_primeFactors = primeFactors(list[0])
    list.remove(list[0])

    for number in list:
        numberFactors = []
        temp = []
        numberFactors = primeFactors(number)
        for p in mdc_primeFactors:
            if p in numberFactors:
                temp.append(p)
                numberFactors.remove(p)
        mdc_primeFactors = temp

    mdc = 1
    for number in mdc_primeFactors:
        mdc *= number
    return mdc


def primeFactors(n):
    plist = listOfPrimes(int(math.floor(n / 2)))
    rlist = []
    index = 0
    i = 1
    if n in plist:
        return n
    while index < len(plist) and n > 1:
        prime = plist[index]
        if n % prime == 0:
            n /= prime
            rlist.append(prime)
        else:
            index += 1
        i += 1
    if rlist == []:
        rlist.append(n)

    return rlist





def listOfPrimes(M):

    max = int(math.sqrt(M))

    primes_l = [x for x in range(2, M + 1)]

    for i, v in enumerate(primes_l):
        if v > max:
            break
        for x, y in enumerate(primes_l):
            if (v != y and y % v == 0):
                primes_l.remove(y)

    return primes_l


def addFractions(f1, f2):
    f1 = f1.split('/')
    f2 = f2.split('/')

    num1 = 0
    den1 = 1
    num2 = 0
    den2 = 1

    if len(f1) == 1:
        num1 = int(f1[0])
    elif len(f1) == 2:
        num1 = int(f1[0])
        den1 = int(f1[1])

    if len(f2) == 1:
        num2 = int(f2[0])
    elif len(f2) == 2:
        num2 = int(f2[0])
        den2 = int(f2[1])

    if den1 == den2:
        frac = (num1 + num2, den1)
    else:
        frac = (num1 * den2 + num2 * den1, den1 * den2)

    d = mdc(frac[0], frac[1])

    return (frac[0] / d, frac[1] / d)



'''
Algoritimo antigo e cheio de falhas. Recebe uma string.
def listOfPrimes(M):

#Algoritimo para encontrar numeros primos chamado de Peneira de Eratostenes

    max = math.floor(math.sqrt(int(M)))
    list = [2]

    for i in range(2,int(M)+1):
        list.append(i)

    index = list[0]
    prime_l = []

    while index <= max:
        prime_l.append(index)
        list.remove(index)
        remove_l=[]
        for n in list:
            if n % index == 0:
                remove_l.append(n)

        for n in remove_l:
            list.remove(n)

        index = list[0]

    for n in list:
        prime_l.append(n)

    return prime_l

'''