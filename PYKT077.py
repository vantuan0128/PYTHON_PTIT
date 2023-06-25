"""
Hệ thống quản lý lịch thi học kỳ cho nhiều Môn học, mỗi môn học có các (Có thông tin Mã môn học, tên môn học) Lịch thi học kỳ bao gồm nhiều thông tin gồm: Mã ca thi, Mã môn học, Ngày thi, Giờ thi, Nhóm thi. Mã ca thi được đánh số từ T001, T002 và tự động tăng dần.

Cho danh sách các ca thi, mỗi môn học có nhiều ca thi, hãy thực hiện sắp xếp danh sách các ca thi theo thứ tự ưu tiên như sau ngày tăng dần, giờ tăng dần, mã môn học tăng dần.

Input:

Dòng đầu tiên cho 2 số N, M lần lượt là số môn học và số ca thi.

N * 2 dòng tiếp theo là thông tin mã môn học và tên môn học.

M dòng còn lại mỗi dòng là thông tin lịch thi bao gồm Mã môn học, ngày thi (dd/mm/yyyy) giờ thi (hh:mm) và nhóm thi (dạng xâu ký có 2 ký tự bất kỳ).

Output:

Lịch thi đã sắp xếp như mẫu, mỗi lịch thi trên một dòng
Input:
2 10
INT1155
Tin hoc co so 2
INT1339
Ngon ngu lap trinh C++
INT1155 25/11/2021 08:00 01
INT1155 04/12/2021 08:00 02
INT1155 04/12/2021 13:30 03
INT1155 25/11/2021 13:30 04
INT1155 25/11/2021 15:00 05
INT1339 25/11/2021 08:00 01
INT1339 25/11/2021 08:00 02
INT1339 04/12/2021 13:30 03
INT1339 04/12/2021 13:30 04
INT1339 04/12/2021 15:00 05
Output:
T001 INT1155 Tin hoc co so 2 25/11/2021 08:00 01
T006 INT1339 Ngon ngu lap trinh C++ 25/11/2021 08:00 01
T007 INT1339 Ngon ngu lap trinh C++ 25/11/2021 08:00 02
T004 INT1155 Tin hoc co so 2 25/11/2021 13:30 04
T005 INT1155 Tin hoc co so 2 25/11/2021 15:00 05
T002 INT1155 Tin hoc co so 2 04/12/2021 08:00 02
T003 INT1155 Tin hoc co so 2 04/12/2021 13:30 03
T008 INT1339 Ngon ngu lap trinh C++ 04/12/2021 13:30 03
T009 INT1339 Ngon ngu lap trinh C++ 04/12/2021 13:30 04
T010 INT1339 Ngon ngu lap trinh C++ 04/12/2021 15:00 05

"""


class LT:
    def __init__(self, id, ma, name, date, time, nhom):
        self.id = "T{:03d}".format(id)
        self.ma = ma
        self.name = name
        self.date = date
        self.time = time
        self.nhom = nhom
        self.ngay = date[:2]
        self.thang = date[3:5]
        self.nam = date[6:]
        self.gio = time[:2]
        self.phut = time[3:5]
        self.giay = time[6:]


ma1 = []
ten1 = []
c = []
n, m = [int(i) for i in input().split()]
for i in range(n):
    ma1.append(input())
    ten1.append(input())
for j in range(m):
    ma, date, time, nhom = [str(s) for s in input().split()]
    name = ''
    for i in range(len(ma)):
        if ma == ma1[i]:
            name = ten1[i]
            break
    c.append(LT(j + 1, ma, name, date, time, nhom))

c = sorted(c, key=lambda x: (x.nam, x.thang, x.ngay, x.gio, x.phut, x.giay, x.ma))
for i in c:
    print(i.id, i.ma, i.name, i.date, i.time, i.nhom)

