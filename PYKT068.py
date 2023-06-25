"""
Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.

Thông tin về mỗi môn học gồm:

Mã môn: xâu ký tự không có khoảng trống, không quá 15 ký tự
Tên môn: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
Hình thức thi: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
Hãy nhập danh sách và in danh sách sắp xếp theo mã môn.
Input:
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
Output:
BAS1203 Giai tich 1 Thi viet + Van dap truc tuyen
MUL1320 Nhap mon da phuong tien Bai tap lon + Van dap truc tuyen
"""
s=[]
for i in range(int(input())):
    x=input()+' '+input()+' '+input()
    s.append(x)
s.sort()
for i in s: print(i)