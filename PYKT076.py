"""
Trên hệ thống phim của một website có các thông tin bộ phim bao gồm Mã phim, Tên phim, Ngày khởi chiếu, Số tập phim, Thể loại. Mã phim được đánh số tự động từ P001, P002 và tự động tăng dần. Thể loại phim bao gồm thông tin Mã thể loại và Tên thể loại. Mã thể loại được đanh số tự động tăng dần từ TL001, TL002

Cho danh sách các phim trên hệ thống, hãy thực hiện sắp xếp danh sách các bộ phim theo thứ tự ưu tiên ngày khởi chiếu tăng dần, tên phim sắp xếp theo thứ tự từ điển, số tập phim giảm dần.

Input:

Dòng đầu tiên cho 2 số N, M lần lượt là số lượng thể loại và số lượng bộ phim.

N dòng tiếp theo là thông tin tên thể loại. Mã thể loại tự động sinh theo thứ tự nhập vào

M dòng còn lại mỗi dòng là thông tin phim bao gồm Mã thể loại, ngày khởi chiếu (dd/mm/yyyy) tên phim và số tập phim (số nguyên tối đa 10000).

Output:

Danh sách phim đã sắp xếp như mẫu, mỗi phim trên một dòng
Input:
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
Output:
P001 Hai huoc 25/11/2021 Phim so 1 10
P003 Tinh cam 25/11/2021 Phim so 3 5
P002 Hai huoc 04/12/2021 Phim so 2 15

"""
class PHIM:
    def __init__(self, code,theloai, date, name, sotap):
        self.code="P{:03d}".format(code)
        self.theloai=theloai
        self.date=date
        self.ngay=date[:2]
        self.thang=date[3:5]
        self.nam=date[6:]
        self.name=name
        self.sotap=sotap

n,m=[int(x) for x in input().split()]
b=[]
a=[]
for i in range(n):
    a.append(input())
for j in range(m):
    theloai=''
    ma=input()
    date=input()
    name=input()
    sotap=int(input())
    i=int(ma[2]+ma[3]+ma[4])-1
    theloai=a[i]
    b.append(PHIM(j+1,theloai,date, name, sotap))

b=sorted(b,key=lambda x: (x.nam,x.thang,x.ngay,x.name,-x.sotap))
for i in b:
    print(i.code, i.theloai,i.date,i.name,i.sotap)