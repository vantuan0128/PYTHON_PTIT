"""
Sử dụng lớp Point đã có trong bài 1, khai báo lớp Triangle với thuộc tính là 3 điểm.
Viết các phương thức phù hợp để tính chu vi tam giác.
Nếu 3 điểm không thể tạo thành tam giác thì in ra INVALID
Nếu 3 điểm tạo thành 1 tam giác thì in ra chu vi của tam giác đó, làm tròn đến 3 chữ số phần thập phân.
Input:
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
Output:
INVALID
INVALID
17.071
"""
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def chuvi(self, a, b):
        AB = math.sqrt((self.x - a.x) * (self.x - a.x) + (self.y - a.y) * (self.y - a.y))
        AC = math.sqrt((self.x - b.x) * (self.x - b.x) + (self.y - b.y) * (self.y - b.y))
        BC = math.sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y))
        if (AB + AC) <= BC or (AB + BC) <= AC or (AC + BC) <= AB:
            print("INVALID")
        else:
            print("{:.3f}".format(AB + AC + BC))


a = []
t = int(input())
for x in range(t):
    a += [float(x) for x in input().split()]
i = 0
for j in range(t):
    p1 = Point(a[i], a[i + 1])
    p2 = Point(a[i + 2], a[i + 3])
    p3 = Point(a[i + 4], a[i + 5])
    p1.chuvi(p2, p3)
    i += 6