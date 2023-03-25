"""
Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
Hãy sắp xếp dãy số theo tích các chữ số tăng dần. Nếu tích các chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.
Input:
1
8
143 43 22 99 7 9 1111 10000000
Output:
10000000 1111 22 7 9 43 143 99
"""
from functools import cmp_to_key

def tich(n):
    ans = 1
    while n > 0:
        m = n % 10
        ans = ans*m
        n //= 10
    return ans

def cmp(a,b):
    if tich(a) != tich(b): return tich(a) - tich(b)
    else: return a - b

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        a = list(map(int,input().split()))
        # a.sort(key = cmp_to_key(cmp))
        # for x in a:
        #     print(x,end=' ')
        # print()
        a.sort(key=lambda x: (tich(x), int(x)))
        print(*a)
