#https://www.codewars.com//kata/529adbf7533b761c560004e5
def fibonacci(n, cache = [0, 1]):
    if len(cache) <= n:
        cache.append(fibonacci(n - 1) + fibonacci(n - 2))
    return cache[n]
