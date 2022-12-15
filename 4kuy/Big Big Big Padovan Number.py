#https://www.codewars.com//kata/5819f1c3c6ab1b2b28000624
def padovan(n):
    x,y,z = 1,0,0
    for c in map(int,bin(n)[2:]):
        x,y,z = x*x+2*y*z,2*x*y+y*y+z*z, x*z+2*y*z+x*z+y*y
        if c:
            x,y,z = y,z,x+y
    return x+y+z
