"""
Trong toán học, một cặp số được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của 2 số đó là 1.
Cho số nguyên dương N, giả sử ta đếm được K số nguyên dương nhỏ hơn N có tính chất nguyên tố cùng nhau với N.
Hãy kiểm tra xem K có phải là số nguyên tố hay không.
"""
import math


def SNT(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if n % i == 0: return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    dem = 0
    for j in range(0,n):
        if math.gcd(j,n) ==  1: dem += 1
    if SNT(dem): print('YES')
    else: print('NO')