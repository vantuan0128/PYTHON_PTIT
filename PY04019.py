"""
Doanh nghiệp X cần tuyển một số nhân viên mới. Bài thi tuyển có hai phần: lý thuyết và thực hành. Sau khi tính điểm trung bình, các thí sinh sẽ được xếp thành 4 loại:
Nếu điểm dưới 5 -> TRUOT
Nếu điểm lớn hơn hoặc bằng 5 nhưng nhỏ hơn 8 -> CAN NHAC
Nếu điểm từ 8 đến 9.5 -> DAT
Nếu điểm lớn hơn 9.5 -> XUAT SAC
Điểm các bài thi lý thuyết và thực hành đều là số thực trong phạm vi từ 0 đến 10.
Tuy nhiên, khi nhập điểm các bài thi, cán bộ tuyển dụng có thể quên mất dấu . phân cách phần nguyên và phần thập phân.
Do đó nếu điểm ghi là 78 thì cần được hiểu là 7.8
Hãy sắp xếp danh sách thí sinh đã được xếp loại theo điểm trung bình giảm dần.
Dòng đầu ghi số thí sinh. Mỗi thí sinh ghi trên 3 dòng lần lượt là:

Họ và tên (xâu ký tự độ dài không quá 100)
Điểm lý thuyết
Điểm thực hành
Mã thí sinh cần được tự động gán theo mẫu TS + số thứ tự (tính từ 01).
Input:
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Output:
TS01 Nguyen Thai Binh 6.00 CAN NHAC
TS03 Phan Van Duc 5.60 CAN NHAC
TS02 Le Cong Hoa 4.25 TRUOT
"""
class NV:
    def __init__(self, code, name, lt, th,xl):
        self.code=str("TS0{:01d}".format(code))
        self.name=name
        self.lt=lt
        self.th=th
        self.xl=xl

if __name__ == "__main__":
    t = int(input())
    a = []
    xl = ''
    for i in range(t):
        name = input()
        lt = float(input())
        th = float(input())
        if lt > 10: lt /= 10
        if th > 10: th /= 10
        lt = (lt+th)/2
        if lt > 9.5: xl = "XUAT SAC"
        elif lt >= 8: xl = "DAT"
        elif lt >= 5: xl = "CAN NHAC"
        else: xl = "TRUOT"
        a.append(NV(i+1,name,lt,th,xl))

    a = sorted(a,key=lambda x:(-x.lt))
    for i in range(len(a)):
        print(a[i].code,a[i].name,"{:.2f}".format(a[i].lt),a[i].xl)