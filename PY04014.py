"""
Trường THCS XYZ lập bảng điểm tổng kết cho học sinh. Có 10 môn học lần lượt gồm: Toán, Tiếng Việt, Ngoại ngữ, Vật lý, Hóa học, Sinh học,
Lịch Sử, Địa, Giáo dục công dân và môn Công nghệ. Trong đó môn Toán và Tiếng Việt tính hệ số 2, các môn còn lại hệ số 1.
Học sinh được xếp hạng theo điểm trung bình:
Từ 9 trở lên: loại XUAT SAC
Từ 8 đến 8.9: loại GIOI
Từ 7 đến 7.9: loại KHA
Từ 5 đến 6.9: loại TB
Dưới 5: loai YEU
Hãy lập bảng điểm tổng kết và sắp xếp theo điểm trung bình giảm dần.

Danh sách đã sắp xếp được ghi ra bao gồm các thông tin:

Mã học sinh (tự động gán tăng dần theo thứ tự nhập, bắt đầu là HS01)
Họ và tên
Điểm trung bình (với 1 chữ số phần thập phân)
Xếp loại
Trong trường hợp điểm trung bình bằng nhau thì học sinh nào có mã học sinh nhỏ hơn sẽ xếp trên.

Input:
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
Output:
HS02 Le Van Tam 7.7 KHA
HS01 Luu Thuy Nhi 7.3 KHA
HS03 Nguyen Thai Binh 6.6 TB
"""
from decimal import ROUND_HALF_UP, Decimal


class BD:
    def __init__(self, code, name, tb, xl):
        self.code = str("HS{:02d}".format(code))
        self.name = name
        self.tb = tb
        self.xl = xl

if __name__ == "__main__":
    t = int(input())
    k = 0
    b = []
    for i in range(t):
        code = ''
        xl = ''
        diem = []
        name = input()
        diem = [Decimal(x) for x in input().split()]
        tb = 0
        for j in range(len(diem)):
            tb += diem[j]
        tb += diem[0] + diem[1]
        tb = tb / 12
        tb = tb.quantize(Decimal('0.1'), ROUND_HALF_UP)
        if tb >= 9:
            xl = "XUAT SAC"
        elif tb >= 8:
            xl = "GIOI"
        elif tb >= 7:
            xl = "KHA"
        elif tb >= 5:
            xl = "TB"
        else:
            xl = "YEU"

        b.append(BD(i + 1, name, tb, xl))

    b = sorted(b, key=lambda x: (-x.tb, x.code))
    for i in range(len(b)):
        print(b[i].code, b[i].name, "{:.1f}".format(b[i].tb), b[i].xl)