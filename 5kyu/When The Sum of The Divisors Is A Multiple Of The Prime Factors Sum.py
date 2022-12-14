#https://www.codewars.com//kata/562c04fc8546d8147b000039
def ds_multof_pfs(nMin, nMax):
    def prime(n):
        if type(n)!=int:
            return False
        if n == 2:
            return True
        if n%2==0 or n<2:
            return False
        for i in range(3,int(n**0.5)+1):
            if n%i==0:
                return False
        return True    
    def factors(n):
        l = []
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                l.extend([i,n//i])
        return sorted(set(l))    
    def pfactors(n):
        l = []
        for i in factors(n):
            if prime(i):
                while n%i==0:
                    l.append(i)
                    n /= i
        return l    
    return [x for x in range(nMin,nMax+1) if sum(factors(x))%sum(pfactors(x))==0]
