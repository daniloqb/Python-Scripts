import sys
import math_funcs as funcs


__author__ = 'daniloqb'


#input = "1/3 + 1/2 - 3/2"
while True:
    input_txt = raw_input("Enter the fraction: ")

    elements = input_txt.split(" ")

    index = 1
    numerators = []
    denominators = []
    operations = []

    for element in elements:
        if index % 2 != 0:
            l = element.split("/")
            numerators.append(l[0])
            denominators.append(l[1]) if len(l) > 1 else denominators.append(1)
        else:
            operations.append(element)
        index += 1

    numerators = map(lambda x: int(x), numerators)
    denominators = map(lambda x: int(x), denominators)

    mmc_v = funcs.mmc2(denominators)

    factors = map(lambda x, y: mmc_v / x * y, denominators, numerators)

    l_val = []

    for index in range(len(operations)):
        l_val.append(str(factors[index]))
        l_val.append((operations[index]))
    l_val.append(str(factors[len(factors) - 1]))

    numerator = "".join(l_val)
    numerator = eval(numerator)

    mdc_v = funcs.mdc2([abs(numerator), mmc_v])
    numerator = numerator / mdc_v
    denominator = mmc_v / mdc_v

    if denominator != 1:
        answer = "/".join([str(numerator), str(denominator)])
    else:
        answer = str(numerator)

    print input_txt, " = ", answer
