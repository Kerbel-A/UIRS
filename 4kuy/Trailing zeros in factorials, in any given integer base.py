#https://www.codewars.com//kata/544483c6435206617a00012c
def trailing_zeros(num, base):
    c, z, k = [], float('inf'), 1
    while k * k <= base:
        k += 1
        if base % k == 0:
            d = 0
            while base % k == 0:
                d, base = d + 1, base//k
            c += [(k, d)]
    for p, q in c if base <= 1 else c + [(base, 1)]:
        d, k = 0, p
        while k <= num:
            d, k = d + num // k, k * p
        z = min(z, d // q)
    return z