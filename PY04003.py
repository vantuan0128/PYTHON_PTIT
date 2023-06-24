"""
Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số.
Các giá trị đều nguyên dương và không quá 18 chữ số.
Nhập vào một phân số và in ra phân số đó ở dạng tối giản.
Input:
123 456
Output:
41/152
"""
import math


class pso:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def rutgon(self):
        temp = math.gcd(self.n, self.m)
        self.n = int(self.n / temp)
        self.m = int(self.m / temp)

    def __str__(self):
        return "{}/{}".format(int(self.n), int(self.m))


if __name__ == '__main__':
    n, m = map(int, input().split())
    ps = pso(n, m)
    ps.rutgon()
    print(ps)


