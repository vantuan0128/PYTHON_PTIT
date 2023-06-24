"""
Khai báo lớp Point (điểm trong không gian hai chiều) với hai thuộc tính là tọa độ x và tọa độ y (số thực).
nhập vào hai điểm p1, p2 và tính khoảng cách hai điểm đó.
Bài tập này yêu cầu sử dụng hàm main cho sẵn như sau:
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
Input:
2
0 0 0 5
0 199 5 6
Output:
5.0000
193.0648
"""
import math
class Point:
    def __init__(self, x1, y1):
        self.x1=x1
        self.y1=y1
    def distance(self,Point):
        res=math.sqrt((self.x1-Point.x1)**2+(self.y1-Point.y1)**2)
        return "%.4f"%res

def Decimal(n):
    n=float(n)
    return n

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

