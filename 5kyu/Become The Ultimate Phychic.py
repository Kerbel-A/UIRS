#https://www.codewars.com//kata/55b2d9bd2d3e974dfb000030
def Guess_it(n,m):
    result = []
    for x in range(0,n+1):
        b = 4 * n + x - m
        r = m - 3 * n - 2 * x
        g = x
        if all(y >= 0 for y in (b,r,g)):
            result.append([g,r,b])
    return result
