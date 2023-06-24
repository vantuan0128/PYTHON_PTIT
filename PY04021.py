"""
Quán Game mùa này vắng khách nên chủ quán quyết định tính tiền chi tiết đến từng phút.
Dựa trên dữ liệu giờ vào và giờ ra, hãy tính thời gian chơi game của các Game thủ nhé.
Input
Dòng đầu của dữ liệu vào ghi số lượng game thủ trong ngày (không quá 20).
Thông tin về một game thủ đến chơi game được ghi lại trên 4 dòng lần lượt là:
Mã người chơi (xâu ký tự độ dài không quá 10, không có khoảng trống)
Tên người chơi (xâu ký tự độ dài không quá 100, có thể có khoảng trống).
Giờ vào (định dạng hh:mm)
Giờ ra (định dạng hh:mm)
Ghi ra danh sách game thủ đã được sắp xếp theo thời gian chơi game giảm dần.
Input:
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
Output:
06T  Hoang Van Nam 2 gio 30 phut
01T  Nguyen Van An 1 gio 30 phut
02I  Tran Hoa Binh 0 gio 55 phut
"""
import datetime
class Person:
    def __init__(self, code, name, time):
        self.code=code
        self.name=name
        self.time=time

if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        code = input()
        name = input()
        time_in = input()
        time_out = input()
        time_in = datetime.datetime.strptime(time_in,'%H:%M')
        time_out = datetime.datetime.strptime(time_out,'%H:%M')
        time = (time_out-time_in)
        a.append(Person(code,name,time))
    a = sorted(a,key=lambda x: (-x.time))
    for i in range(len(a)):
        print(a[i].code,a[i].name,end=' ')
        x = [int(i) for i in str(a[i].time).split(':')]
        print("{} gio {} phut".format(x[0],x[1]))
