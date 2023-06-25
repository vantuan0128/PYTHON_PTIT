"""
Lớp học phần môn XYZ của trường ABC có không quá 100 sinh viên. Danh sách sinh viên gồm các thông tin: mã sinh viên, họ tên, lớp. Môn học có 10 buổi. Dữ liệu điểm danh với mỗi sinh viên được cho bởi một xâu ký tự gồm 10 ký tự trong đó: x là có mặt, m là đến muộn, v là vắng.

Với điểm chuyên cần tối đa là 10. Giả sử mỗi buổi vắng bị trừ 2 điểm, mỗi buổi đến muộn bị trừ 1 điểm. Hãy tính điểm chuyên cần cho mỗi sinh viên (tất nhiên nếu tính ra điểm âm thì ghi vào bảng điểm vẫn là 0).

Nếu điểm bằng 0 thì in thêm ghi chú KDDK (tức là không đủ điều kiện dự thi hết môn).

Input

Dòng đầu ghi số n là số sinh viên. Mỗi sinh viên ghi trên 3 dòng lần lượt là mã sinh viên, họ tên, lớp.

Tiếp theo là n dòng ghi dữ liệu điểm danh. Mỗi dòng gồm mã sinh viên, sau đó là một khoảng trống rồi đến xâu ký tự điểm danh có đúng 10 chữ cái.

Output

Ghi ra danh sách điểm chuyên cần (theo đúng thứ tự ban đầu) gồm các thông tin:

Mã sinh viên
Họ và tên
Lớp
Điểm chuyên cần
Ghi chú (nếu có)
Mỗi thông tin cách nhau một khoảng trống.
Input:
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
Output:
B19DCCN999 Le Cong Minh D19CQAT02-B 0 KDDK
B19DCCN998 Tran Truong Giang D19CQAT02-B 4
B19DCCN997 Nguyen Tuan Anh D19CQCN04-B 6
"""
class SV:
    def __init__(self,msv, name, lop):
        self.msv=msv
        self.name=name
        self.lop=lop

t=int(input())
a=[]

for i in range(t):
    msv=input()
    name=input()
    lop=input()
    a.append(SV(msv,name,lop))
for i in range(t):
    diem=10
    msv1,x=[str(s) for s in input().split()]
    for i in x:
        if i=='x': diem=diem
        elif i=='m': diem-=1
        elif i=='v': diem-=2
    for j in range(len(a)):
        if msv1==a[j].msv:
            a[j].diem=diem

for i in range(len(a)):
    print(a[i].msv,a[i].name,a[i].lop,end=' ')
    if a[i].diem>0: print(a[i].diem)
    else: print("0 KDDK")