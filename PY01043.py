"""
Cho số nguyên dương N không quá 6 chữ số.
Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:
N là số thuận nghịch
Tất cả các chữ số của N đều chẵn
Số chữ số của N cũng là một số chẵn
VD 100
Output: 22 44 66 88
"""

def check(n):
    n1 = n
    m = 0
    dem = 0
    while n > 0:
        s = n % 10
        m = m*10 + n%10
        if s%2 != 0: return False
        else: dem += 1
        n //= 10
    if dem % 2 != 0: return False
    return m == n1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(22,n,2):
            if check(i): print(i,end=' ')
        print()



