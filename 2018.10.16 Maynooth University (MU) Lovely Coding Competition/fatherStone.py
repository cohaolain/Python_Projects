n, x, k = input().split()
n, x, k = int(n), int(x), int(k)

c = 0
if x == 0 and n == 1:
    print(0)
else:
    while True:
        if (n == 1):
            if (k % 3 == 0):
                print(-1)
                break

        c = c + 1
        if (n % 2):
            n = (3 * n) + 1
        else:
            n = n / 2

        x = x + 1

        if (x == k):
            x = 0
            if (n == 1):
                print(c)
                break
