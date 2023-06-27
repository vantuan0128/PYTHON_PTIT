"""
Nhóm sinh viên PTIT cùng nhau đăng ký 3 môn học trong Học kỳ hè năm 2021 theo đúng thứ tự:

Môn 1: Lập trình hướng đối tượng: 3 tín chỉ
Môn 2: Ngôn ngữ lập trình C++: 3 tín chỉ
Môn 3: Tin học cơ sở 2: 2 tín chỉ
Người ta muốn xếp hạng thứ tự các sinh viên trong danh sách theo điểm trung bình giảm dần. Biết rằng điểm trung bình tính đến 2 số phần thập phân và nếu điểm bằng nhau thì thứ hạng cũng bằng nhau.
Chú ý: 2 sinh viên có điểm trung bình bằng nhau thì xếp hạng bằng nhau, và nếu có 2 sinh viên hạng là X thì sinh viên tiếp theo trong danh sách có hạng X+2.

Trong trường hợp xếp hạng bằng nhau thì cần sắp xếp theo mã sinh viên tăng dần.
Ghi ra danh sách sinh viên đã tính điểm và sắp xếp theo xếp hạng từ cao nhất đến thấp nhất, gồm các thông tin:

Mã sinh viên (tự động tăng theo thứ tự nhập, tính từ SV01)
Họ tên đã chuẩn hóa
Điểm trung bình với đúng 2 số phần thập phân
Xếp hạng
Input:
2
 ha Thi kieu     anh
7
6
7
Pham    THI  HAO
6
7
6
Output:
SV01 Ha Thi Kieu Anh 6.63 1
SV02 Pham Thi Hao 6.38 2
"""
import math
class SV:
    def __init__(self,id,name,diem):
        self.id="SV{:02d}".format(id)
        self.name=name
        self.diem=diem

a=[]
for i in range(int(input())):
    name1=input().lower().title().strip().split()
    name=''
    for x in name1: name+= x+' '
    name=name.rstrip()
    mon1,mon2, mon3=int(input()),int(input()),int(input())
    diem=(mon1*3+mon2*3+mon3*2)*0.125
    a.append(SV(i+1,name,diem))

a=sorted(a,key=lambda x: (-x.diem))
print(a[0].id ,a[0].name ,"{:.2f}".format(math.ceil(a[0].diem*100)/100), 1)
j=1
for i in range(1,len(a)):
    print(a[i].id ,a[i].name ,"{:.2f}".format(math.ceil(a[i].diem*100)/100), end=' ')
    if a[i].diem==a[i-1].diem:
        j=j
    else: j=i+1
    print(j)