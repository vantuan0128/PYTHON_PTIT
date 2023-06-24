"""
Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa (‘A’ đến ‘Z’).
Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b.
Trong đó N không quá 100.000, 2 ≤ b ≤ 36.
Input:
3
10 2
2021 2
31 16
Output:
1010
11111100101
1F
"""

def func(n, b):
    s = ''
    while n > 0:
        du = n % b

        if du >= 10:
            s += str(chr(du + 55))
        else:
            s += str(du)
        n = int(n / b)
    print(s[::-1])

if __name__ == "__main__":
    n = int(input())
    while n > 0:
        m, b = map(int, input().split())
        func(m, b)
        n -= 1