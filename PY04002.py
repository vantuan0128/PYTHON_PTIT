"""
Khai báo lớp Rectangle với 3 thuộc tính:
Chiều dài: số nguyên
Chiều rộng: số nguyên
Màu sắc: xâu ký tự
Nhập vào giá trị độ dài hai cạnh của hình chữ nhật và màu sắc.
In ra thông tin về chu vi, diện tích và màu sắc
(đã đưa về dạng chuẩn trong đó ký tự đầu viết hoa, các ký tự sau viết thường) của hình chữ nhật đó.
Bài tập này yêu cầu sử dụng hàm main cho sẵn như sau:

Python 3
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

Input:
10 2 RED
Output:
24 20 Red
"""

class Rectangle:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color[0:1:].upper() + color[1::].lower()

    def check(self):
        if self.w <= 0 or self.h <= 0: return 0
        return 1

    def output(self):
        if self.check() == 1:
            print((self.w + self.h) * 2, self.w * self.h, self.color, sep=' ')
        else:
            print('INVALID')


a = input().split()
rec = Rectangle(int(a[0]), int(a[1]), (a[2]))
rec.output()
