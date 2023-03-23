"""
Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
Hãy sắp xếp dãy số theo tổng chữ số tăng dần.
Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.
Input:
1
8
143 43 22 99 7 9 1111 10000000
Output:
10000000 22 1111 7 43 143 9 99
"""

from functools import cmp_to_key

def tong(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

def cmp(a, b):
    if tong(a) != tong(b): return tong(a) - tong(b)
    else: return a - b

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(key = cmp_to_key(cmp))
        for i in a: print(i,end = ' ')
        print()