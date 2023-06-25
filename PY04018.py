"""
Trường THPT ACB tuyển giáo viên mới cho ba môn Toán, Lý, Hóa. Theo yêu cầu mới, bài thi tuyển gồm 2 nội dung: Tin học và Chuyên môn. Điểm thi Tin học sẽ được nhân đôi khi tính tổng điểm.

Mỗi GV có thể có điểm ưu tiên được xét theo mã như trong bảng sau:
Mã 1 -> 2.0
Mã 2 -> 1.5
Mã 3 -> 1.0
Mã 4 -> 0
Mã xét tuyển gồm 2 thành phần. Chữ cái đầu tiên ứng với môn học: A là Toán, B là Lý và C là Hóa; tiếp theo là 1 chữ số thể hiện mã ưu tiên.

Tổng điểm sau khi cộng điểm ưu tiên nếu từ 18 trở lên sẽ được xét TRÚNG TUYỂN, nhỏ hơn sẽ bị LOẠI.

Viết chương trình nhập danh sách điểm thi và sắp xếp GV theo thứ tự tổng điểm giảm dần. Mã GV dự thi được tự động gán theo thứ tự bắt đầu từ 01.
Ghi ra danh sách đã sắp xếp. Thông tin mỗi GV gồm: Mã GV, Tên, Môn học, Tổng điểm (1 chữ số phần thập phân), Kết quả. Mỗi thông tin cách nhau một khoảng trống.
Input:
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
Output:
GV03 Hoang Thi Tam HOA 21.5 TRUNG TUYEN
GV01 Le Van Binh TOAN 19.0 TRUNG TUYEN
GV02 Tran Van Toan LY 16.0 LOAI
"""
class GV:
    def __init__(self, id, name,mon, diem, xl):
        self.id="GV{:02d}".format(id)
        self.name=name
        self.diem=diem
        self.xl=xl
        self.mon=mon

t= int(input())
a=[]
for i in range(t):
    xl=''
    mon=''
    dem=0.0
    name=input()
    code=input()
    tinhoc=float(input())
    chuyen=float(input())
    x=int(code[1])
    y=code[0]
    if x==1: diem=2.0
    elif x==2: diem=1.5
    elif x==3: diem=1.0
    elif x==4: diem=0.0
    diem+=tinhoc*2+chuyen
    if diem>=18: xl="TRUNG TUYEN"
    else: xl="LOAI"

    if y=='A': mon="TOAN"
    elif y=='B': mon="LY"
    elif y=='C': mon="HOA"
    a.append(GV(i+1,name,mon,diem,xl))

a=sorted(a,key= lambda x: (-x.diem))
for i in a:
    print(i.id, i.name,i.mon,"{:.1f}".format(i.diem),i.xl)