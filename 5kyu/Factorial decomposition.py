#https://www.codewars.com//kata/5a045fee46d843effa000070
import math
def decomp(n):
    n = math.factorial(n)
    st = []
    for i in range(2,n):
        count = 0
        while n%i == 0:
            count+=1
            n = n // i
        if count>1 :
            st.append(f"{i}^{count}")
        elif count == 1:
            st.append(f"{i}")
        if n == 1:
            break
    return " * ".join(st)
