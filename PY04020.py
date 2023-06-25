"""
Cửa hàng điện máy – điện lạnh cần lập hóa đơn tính tiền cho khách hàng. Mỗi mặt hàng sẽ có đơn giá và một số tiền được gọi là chiết khấu trên tổng hóa đơn. Số tiền phải thanh toán sẽ bằng đơn giá * số lượng sau đó trừ đi tiền chiết khấu.

Hãy tính tiền cho từng hóa đơn và sắp xếp theo số tiền giảm dần.

Input

Dòng đầu ghi số lượng hóa đơn. Không quá 20.

Mỗi thông tin hóa đơn gồm 5 dòng:

Mã mặt hàng (xâu ký tự độ dài không quá 10, không có khoảng trống)
Tên mặt hàng (xâu ký tự độ dài không quá 100, có thể có khoảng trống)
Số lượng mua (không quá 50)
Đơn giá (số nguyên dương có thể đến 10 chữ số)
Tiền chiết khấu của hóa đơn (có thể đến 9 chữ số).
Input:
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
Output:
ML02 May lanh HITACHI 4 2550000000 0 10200000000
ML01 May lanh SANYO 12 4000000 2400000 45600000
ML03 May lanh NATIONAL 5 3000000 150000 14850000
"""
class HD:
    def __init__(self, code, name, sl, dongia, ckhau,tien):
        self.code=code
        self.name=name
        self.sl=sl
        self.dongia=dongia
        self.ckhau=ckhau
        self.tien=tien
a=[]
for i in range(int(input())):
    code=input()
    name=input()
    sl=int(input())
    dongia=int(input())
    ckhau=int(input())
    tien=sl*dongia-ckhau

    a.append(HD(code, name, sl, dongia, ckhau, tien))
a=sorted(a,key=lambda x: (-x.tien))
for i in a:
    print(i.code,i.name, i.sl,i.dongia,i.ckhau,i.tien)