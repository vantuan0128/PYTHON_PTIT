"""
Cho hai số nguyên N và X.

Bắt đầu từ số X, hãy liệt kê N +1 số liên tiếp sao cho
hoảng cách giữa số trước và số sau lần lượt là các số trong dãy N số nguyên tố đầu tiên.

Ví dụ N=5 và X=4. Vì 5 số nguyên tố đầu tiên là 2 3 5 7 11 nên ta có 6 số trong dãy cần liệt kê là: 4 6 9 14 21 32
Input:
5 4
Output:
4 6 9 14 21 32
"""

import math


def nto(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    n, x = map(int, input().split())
    if n == 1:
        print(x, x + 2)
    elif n == 2:
        print(x, x + 2, x + 2 + 3)
    else:
        print(x, x + 2, end=' ')
        m = x + 2
        for i in range(3, 1000000000, 2):
            if nto(i):
                m = m + i
                print(m, end=' ')
                n -= 1
            if n == 1: break
