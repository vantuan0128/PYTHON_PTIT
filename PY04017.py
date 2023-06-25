"""
Cuộc đua xe đạp bắt đầu từ 6h00 với độ dài quãng đường đua là 120 Km. Các cua-rơ sẽ được ghi nhận thành tích dựa trên thời điểm đến đích. Hãy xếp hạng theo thứ tự thành tích giảm dần.

Input

Dòng đầu ghi số cua-rơ tham gia cuộc đua.

Mỗi cua-rơ ghi trên 3 dòng:

Họ tên (xâu ký tự độ dài không quá 50)
Đơn vị (xâu ký tự độ dài không quá 20)
Thời điểm đến đích theo định dạng h:mm
Output

Ghi ra danh sách đã sắp xêp theo thành tích, tốt hơn xếp trước, kém hơn xếp sau.

Thông tin mỗi cua-rơ bao gồm:

Mã (là chữ cái đầu tiên của các từ trong tên đơn vị ghép với chữ cái đầu tiên các từ trong họ tên – xem ví dụ để hiểu rõ hơn)
Họ tên
Đơn vị
Vận tốc trung bình (đã làm tròn ra giá trị nguyên)
Input:
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
Output:
HBVNH Vu Ngoc Hoang Hoa Binh 51 Km/h
HNTVM Tran Vu Minh Ha Noi 48 Km/h
AGPDT Pham Dinh Tan An Giang 44 Km/h
"""
import datetime


class DX:
    def __init__(self, code, name, city, vantoc):
        self.code = code
        self.name = name
        self.city = city
        self.vantoc = vantoc


t = int(input())
a = []
for i in range(t):
    name = input().strip()
    city = input().strip()
    time = input().split(':')

    c = [i[0] for i in city.split()]
    b = [i[0] for i in name.split()]
    code = ''.join(c) + ''.join(b)

    vantoc = 120 / ((int(time[0]) * 60 + int(time[1]) - 60 * 6) / 60)

    a.append(DX(code, name, city, vantoc))

a = sorted(a, key=lambda x: -x.vantoc)
for i in range(len(a)):
    print(a[i].code, a[i].name, a[i].city, round(a[i].vantoc), end=' ')
    print('Km/h')