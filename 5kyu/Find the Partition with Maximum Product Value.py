#https://www.codewars.com//kata/5716a4c2794d305f4900156b
def find_part_max_prod(n):
    if n % 3 == 0:
        return [[3]*(n//3), 3**(n//3)]
    if n % 3 == 1:
        return [[4] + [3]*(n//3 - 1), [3]*(n//3 - 1) + [2, 2], 3**(n//3 - 1)*4]
    if n % 3 == 2:
        return [[3]*(n//3) + [2], 3**(n//3)*2]
