"""
Tiền nước hàng tháng của thành phố ABC được tính theo đơn giá trong bảng sau:
Số m khối: 0-50 Đơn giá 100 Phụ phí 2%
Số m khối: 51-100 Đơn giá 150 Phụ phí 3%
Số m khối: Trên 100 Đơn giá 200 Phụ phí 5%

Trong đó, phụ phí được hiểu là số tiền tính thêm (theo phần trăm) trên tổng số tiền nước tiêu thụ.
Cho danh sách khách hàng và chỉ số đồng hộ. Hãy sắp xếp danh sách hóa đơn theo tổng số tiền giảm dần.
Ghi ra danh sách khách hàng đã sắp xếp theo tổng tiền giảm dần gồm các thông tin

Mã khách hàng (tự động gán tăng dần theo thứ tự nhập, bắt đầu từ KH01)
Tên khách hàng
Tổng số tiền (được làm tròn ở dạng số nguyên)
Input:
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
Output:
KH03 Ha Hue Anh 34545
KH02 Le Duc Cong 8240
KH01 Le Thi Thanh 3264
"""
class HĐ:
    def __init__(self,code, name, tien):
        self.code=str("KH{:02d}".format(code))
        self.name=name
        self.tien=tien

if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        tien = 0
        name = input()
        new = int(input())
        old = int(input())
        dien = old-new
        money = dien
        if money > 100:
            tien = (dien-100)*200 + 50*100 + 50*150
            tien += tien * 0.05
        elif money > 50:
            tien += 50*100 + (dien-50)*150
            tien += tien * 0.03
        else:
            tien = dien*100 + dien*100*0.02

        a.append(HĐ(i+1,name,tien))

    a = sorted(a,key=lambda x: (-x.tien,x.code))
    for i in range(len(a)):
        print(a[i].code,a[i].name,"{:.0f}".format(a[i].tien))