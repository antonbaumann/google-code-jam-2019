def solve(path) -> str:
    return ''.join('S' if p == 'E' else 'E' for p in path)

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    path = input()
    print("Case #{}: {}".format(i, solve(path)))
