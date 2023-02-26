"""
Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau
nếu a và b có ước chung lớn nhất bằng 1.
Cho hai số nguyên dương N và K trong đó 10 < N < 10000; 1 < K < 6.
Hãy liệt kê các số có K chữ số thỏa mãn nguyên tố cùng nhau với N.
"""
import math

n,k = map(int,input().split())
ok = 0
for i in range (10**(k-1),10**k-1):
    if math.gcd(n,i) == 1:
        print(i,end = ' ')
        ok += 1
    if ok == 10:
        print()
        ok = 0