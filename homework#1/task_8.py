m = int(input())
n = int(input())
k = int(input())
if m*n > k and k%n == 0 or k % m == 0:
    print('YES')
else:
    print('NO')