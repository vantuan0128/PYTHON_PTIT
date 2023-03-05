"""
Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố. Kết quả được in ra theo mẫu trong ví dụ, trong đó thêm số thừa số 1 (không phải nguyên tố) ở đầu kết quả phân tích.
Input:
3
28
100
1234
Output:
1 * 2^2 * 7^1
1 * 2^2 * 5^2
1 * 2^1 * 617^1
"""

def func():
    n = int(input())
    dem = 0
    while n % 2 == 0:
        n //= 2
        dem += 1
    print('1 ',end='')
    if dem > 0: print('* 2^'+str(dem),end=' ')
    i = 3
    while i <= n / 2 + 1:
        res = 0
        while n % i == 0:
            res += 1
            n //= i
        if res > 0: print('* '+str(i)+'^'+str(res),end=' ')
        i += 2
    if n > 1: print('* '+str(n)+'^1',end=' ')
    print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        func()