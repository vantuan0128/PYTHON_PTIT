"""
Viết chương trình khai báo
lớp Thí Sinh gồm các thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3 và Tổng điểm.
Đọc thông tin 1 thí sinh từ bàn phím và in ra màn hình 3 thông tin: Họ tên, Ngày sinh, Tổng điểm.
Gồm 5 dòng lần lượt, mỗi dòng ghi 1 thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3.
Họ tên không quá 50 chữ cái,
Ngày sinh viết đúng chuẩn dd/mm/yyyy. Các giá trị điểm là số thực (float).
Ghi ra Họ tên, Ngày sinh và Tổng điểm.
Mỗi thông tin cách nhau một khoảng trống. Điểm được ghi ra với 1 số sau dấu phẩy.
Input:
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
Output:
Nguyen Hoang Ha 11/10/2001 20.0
"""
import datetime
class TS:
    def __init__(self,name, birth, x1, x2, x3):
        self.name = name
        self.birth = birth
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    def __str__(self):
        return "{} {} {}".format(self.name, self.birth,"{:.1f}".format(self.x1+self.x2+self.x3))

if __name__ == "__main__":
    name = input()
    birth = input()
    x1 = float(input())
    x2 = float(input())
    x3 = float(input())
    t = TS(name,birth,x1,x2,x3)
    print(t)