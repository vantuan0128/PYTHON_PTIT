"""
Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số.
Các giá trị đều nguyên dương và không quá 18 chữ số.
nhập vào hai phân số p và q. Tính tổng p + q, rút gọn và in ra kết quả.
Input:
123 456 12 34
Output:
1609/2584
"""
import math

class PS:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self, PS):
        x = self.a * PS.b + self.b * PS.a
        y = self.b * PS.b
        temp = math.gcd(x, y)
        self.a = x / temp
        self.b = y / temp
        return "{}/{}".format(int(self.a), int(self.b))


if __name__ == '__main__':
    a, b, n, m = map(int, input().split())
    ps = PS(a, b)
    ps1 = PS(n, m)
    print(ps.sum(ps1))