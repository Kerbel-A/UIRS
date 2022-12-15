#https://www.codewars.com//kata/586e6b54c66d18ff6c0015cd
def splitlist(lst):
    can = {0: None}
    for i, c in enumerate(lst):
        next_can = {}
        for k in can:
            next_can[k + c] = c
        can |= {k: i for k in next_can if k not in can}
    s = sum(lst)
    best_diff, best_left = s, 0

    for k in can:
        diff = abs((s - k) - k)
        if diff < best_diff:
            best_diff = diff
            best_left = k
    left_ids = set()
    while best_left > 0:
        i = can[best_left]
        left_ids.add(i)
        best_left -= lst[i]

    return (
        [lst[i] for i in left_ids],
        [x for i, x in enumerate(lst) if i not in left_ids]
    )