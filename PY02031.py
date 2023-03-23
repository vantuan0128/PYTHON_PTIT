"""
Cho ma trận A[] cỡ N*M chỉ bao gồm các số nguyên dương không quá 1000.
Hãy kiểm tra các số trong ma trận, nếu giá trị nào là số nguyên tố thì thay thế bằng số 1,
không phải thì thay thế bằng số 0.
Input:
3 3
1 2 3
4 5 6
7 8 9
Output:
0 1 1
0 1 0
1 0 0
"""
import math

def SNT(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1, 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if SNT(a[i][j]): a[i][j] = 1;
            else: a[i][j] = 0
    for i in range(n):
        for x in a[i]: print(x, end = ' ')
        print()