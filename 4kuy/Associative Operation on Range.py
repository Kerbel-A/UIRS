#https://www.codewars.com//kata/608cc9666513cc00192a67a9
def compute_ranges(arr, op, rs):
    n = len(arr)
    m = n.bit_length() + 1
    f = []
    for i in range(n):
        f.append([0] * m)
        f[i][0] = arr[i]   
    for k in range(1, m):
        for i in range(n):
            if i + (1 << k) - 1 < n:
                f[i][k] = op(f[i][k-1], f[i+(1<<(k-1))][k-1])
    res = []
    for l, r in rs:
        res.append(None)
        r -= 1
        d = r - l + 1
        k = d.bit_length() - 1
        i = l
        while i <= r:
            if d & (1 << k):
                if res[-1] is None:
                    res[-1] = f[i][k]
                else:
                    res[-1] = op(res[-1], f[i][k])
                i += (1 << k)           
            k -= 1
    return res