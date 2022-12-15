#https://www.codewars.com//kata/5b16bbd2c8c47ec58300016e
def productsum(n):
    nums = [2 * n] * (n + 1)
    def search(p, s, f, cur):
        k = p - s + f
        if k <= n:
            if p < nums[k]:
                nums[k] = p
            for i in range(cur, n // p * 2 + 1):
                search(p * i, s + i, f + 1, i)
    search(1, 1, 1, 2)
    return sum(set(nums[2:]))