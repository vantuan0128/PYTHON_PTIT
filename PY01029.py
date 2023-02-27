"""
Trong toán học, cặp số (a,b) được gọi là nguyên tố cùng nhau nếu
ước số chung lớn nhất của a và b bằng 1.
Cho số nguyên dương N không quá 9 chữ số.
Hãy kiểm tra xem N và số đảo của N có phải là một cặp số nguyên tố cùng nhau hay không.
"""
import math


def nghichDao(n):
    m = 0
    while n > 0:
        m = m*10 + n%10
        n //= 10
    return m

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if math.gcd(n,nghichDao(n)) == 1: print('YES')
        else: print('NO')