n = int(input())

for i in range(n):
    star = "".join(["*" for _ in range(i + 1)])
    print(star)
