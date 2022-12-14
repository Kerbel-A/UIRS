#https://www.codewars.com//kata/55aa92a66f9adfb2da00009a
def reversi_row(moves):
    stones = [set(), set()]
    for i, p in enumerate(moves):
        curr = stones[i%2]
        oppn = stones[(i+1)%2]
        curr.add(p)    
        l = p-1
        r = p+1
        while l in oppn:
            l-=1
        while r in oppn:
            r+=1
        flip = set(range(l+1 if l in curr else p+1, r if r in curr else p))    
        oppn -= flip
        curr |= flip
    return ''.join('*' if i in stones[0] else 'O' if i in stones[1] else '.' for i in range(8))
