"""
Sử dụng lớp Point đã có trong bài 1, khai báo lớp Triangle với thuộc tính là 3 điểm. Viết các phương thức phù hợp để tính diện tích tam giác.
Công thức Heron tính diện tích tam giác khi biết độ dài 3 cạnh là a,b,c:
Nếu 3 điểm không thể tạo thành tam giác thì in ra INVALID
Nếu 3 điểm tạo thành 1 tam giác thì in ra diện tích của tam giác đó, làm tròn đến 2 chữ số phần thập phân.
Input:
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
Output:
INVALID
INVALID
12.50
"""
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def dien_tich(self,a,b):
        A = math.sqrt((self.x-a.x)*(self.x-a.x)+(self.y-a.y)*(self.y-a.y))
        B = math.sqrt((self.x-b.x)*(self.x-b.x)+(self.y-b.y)*(self.y-b.y))
        C = math.sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))
        if A+B<=C or A+C<=B or B+C<=A:
            print("INVALID")
        else:
            X = 0.25*math.sqrt((A+B+C)*(A+B-C)*(-A+B+C)*(A-B+C))
            print("{:.2f}".format(X))


if __name__ == "__main__":
    a = []
    t = int(input())
    for x in range(t):
        a += [float(x) for x in input().split()]
    j = 0
    for i in range(t):
        a = Point(a[j],a[j+1])
        b = Point(a[j+2],a[j+3])
        c = Point(a[j+4],a[j+5])
        a.dien_tich(b,c)
        j += 6