"""
Khách sạn XYZ có đơn giá (theo ngày) được quy định khác nhau theo từng tầng. Khách hàng đến thuê phòng sẽ được tính tổng số tiền ở theo đơn giá cộng thêm chi phí dịch vụ phát sinh nếu có.
Tầng 1 -> 25
Tầng 2 -> 34
Tầng 3 -> 50
Tầng 4 -> 80
Hãy giúp khách sạn tính tiền phải trả cho từng khách hàng và sắp xếp theo thứ tự tổng tiền giảm dần.
Input

Dòng đầu ghi số khách hàng (không quá 20)

Mỗi khách hàng ghi trên 4 dòng gồm:

Tên khách hàng (xâu ký tự độ dài không quá 100)
Số phòng
Ngày nhận phòng (định dạng dd/mm/yyyy)
Ngày trả phòng (định dạng dd/mm/yyyy)
Tiền dịch vụ phát sinh (số nguyên dương nhỏ hơn 100)
Output

Ghi ra danh sách đã được sắp xếp theo tổng tiền giảm dần bao gồm lần lượt các thông tin:

Mã khách hàng (tự động tăng theo thứ tự nhập, tính từ KH01)
Tên khách hàng
Số phòng
Số ngày ở
Thành tiền
Input:
3
Huynh Van Thanh
103
05/06/2010
05/06/2010
15
Le Duc Cong
106
08/03/2010
01/05/2010
22
Tran Thi Bich Tuyen
207
10/04/2010
21/04/2010
96
Output:
KH02 Le Duc Cong 106 55 1595
KH03 Tran Thi Bich Tuyen 207 12 504
KH01 Huynh Van Thanh 103 1 40
"""
import datetime


class HD:
    def __init__(self, code, name, phong, date, gia):
        self.code = "KH{:02d}".format(code)
        self.name = name
        self.phong = phong
        self.date = date
        self.gia = gia


t = int(input())
a = []
for i in range(t):
    gia = 0
    name = input().strip()
    phong = int(input())
    date_in = input().strip()
    date_out = input().strip()
    phatsinh = int(input())
    date_in = datetime.datetime.strptime(date_in, '%d/%m/%Y')
    date_out = datetime.datetime.strptime(date_out, '%d/%m/%Y')
    date = str(date_out - date_in).split()[0]
    if date == '0:00:00':
        date = 1
    else:
        date = int(date) + 1
    phong1 = int(str(phong)[0])

    if phong1 == 1:
        gia = 25 * date
    elif phong1 == 2:
        gia = 34 * date
    elif phong1 == 3:
        gia = 50 * date
    elif phong1 == 4:
        gia = 80 * date
    gia += phatsinh
    a.append(HD(i + 1, name, phong, date, gia))
a = sorted(a, key=lambda x: (-x.gia))
for i in range(len(a)):
    print(a[i].code, a[i].name, a[i].phong, a[i].date, a[i].gia)
