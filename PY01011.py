"""
Cho số nguyên dương N,
hãy liệt kê các số thuận nghịch nhỏ hơn N thỏa mãn điều kiện:
Chỉ có các chữ số 0,2,4,6,8
Số chữ số của N chia cho 2 dư 0
"""

def thuanNghich(n):
    m = n
    t = 0
    while m > 0:
        t = t*10 + m%10
        m //= 10
    return t == n

def check(n):
    m = 0
    while n>0:
        r = n % 10
        if r % 2 != 0: return False
        m += 1
        n //= 10
    return m % 2 == 0

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(22,n):
        if check(j) and thuanNghich(j): print(j, end=' ')
        else: continue
    print()

