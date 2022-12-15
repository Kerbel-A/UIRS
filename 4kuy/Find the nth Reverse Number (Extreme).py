#https://www.codewars.com//kata/600c18ec9f033b0008d55eec
def find_reverse_number(n):
    if n < 11:
        return n - 1  
    s = str(n)
    if s[0:2] == '10':
        minus = 10 ** (len(s) - 2)
    else:
        minus = 10 ** (len(s) - 1)        
    new = n - minus
    rev = str(new)[::-1]        
    if int(s[0]) < 2 and not s[0:2] == '10':
        return new * minus + int(rev)
    else:
        return new * minus + int(rev[1:])