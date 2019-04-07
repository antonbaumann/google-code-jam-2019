def solve(n) -> (int, int):
    a, b = n, 0
    for i, d in enumerate(reversed(str(n))):
        if d == '4':
            sub = pow(10, i)
            a -= sub
            b += sub
    return a, b
    
t = int(input())
for i in range(1, t + 1):
    n = int(input())
    a, b = solve(n)
    print("Case #{}: {} {}".format(i, a, b))
