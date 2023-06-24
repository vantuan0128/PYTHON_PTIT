"""
Trong một ngày mưa nhiều, các trạm đo mưa hoạt động hết công suất.
Tại mỗi trạm đo, các cơn mưa được ghi nhận thời điểm bắt đầu, thời điểm kết thúc và lượng mưa đo được.
Một trạm mưa có thể có nhiều lần mưa trong ngày.
Hãy tính lượng mưa trung bình trong 1 giờ (60 phút) của từng trạm theo đúng thứ tự trong danh sách ban đầu.
Chú ý để tính lượng mưa trung bình thì cần tính tất các lần đo mưa tại trạm đó.
Dòng đầu ghi số lượt đo lượng mưa.
Thông tin về một lần đo lượng mưa gồm 4 dòng:
Tên trạm
Thời điểm bắt đầu mưa (hh:mm)
Thời điểm kết thúc mưa (hh:mm)
Lượng mưa đo được
Số trạm đo khác nhau nhỏ hơn 10.

Ghi ra danh sách các trạm khác nhau trong danh sách đo mưa và lượng mưa trung bình của từng trạm.
Thông tin trên mỗi dòng lần lượt gồm:
Mã trạm đo (tính từ T01). Chú ý: nếu cùng tên trong danh sách đo thì cũng sẽ cùng mà trạm.
Tên trạm đo mưa
Lượng mưa trung bình trong 1 giờ tại mỗi trạm (tính chính xác đến 2 số phần thập phân).

Input:
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
Output:
T01 Dong Anh 59.22
T02 Cau Giay 80.70
T03 Soc Son 57.60
"""
import datetime
class M:
    def __init__(self,id,name, time,lm):
        self.id="T{:02d}".format(id)
        self.name=name
        self.time=time
        self.lm=lm

if __name__ == "__main__":
    a = []
    k = 0
    for i in range(int(input())):
        dem = 0
        name = input().strip()
        time_in,time_out = input(),input()
        lm = int(input())
        time_in = datetime.datetime.strptime(time_in,'%H:%M')
        time_out = datetime.datetime.strptime(time_out,'%H:%M')
        time1 = str(time_out-time_in)
        b = [str(x) for x in time1.split(':')]
        time = int(b[0])+int(b[1])/60
        j = 0
        for i in range(len(a)):
            if name == a[i].name:
                a[i].time += time
                a[i].lm += lm
                j += 1
        if j == 0:
            k = k + 1
            a.append(M(k,name,time,lm))
    for i in a:
        print(i.id,i.name, "{:.2f}".format(i.lm/i.time))