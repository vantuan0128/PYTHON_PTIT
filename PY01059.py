"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:
Tổng các chữ số ở vị trí chẵn
Tích các chữ số ở vị trí lẻ. – giá trị tích chữ số có thể đến 18 chữ số.
Chú ý khi tính tích bỏ qua các chữ số 0,
nhưng nếu tất cả các vị trí lẻ đều là giá trị 0 thì tích = 0.
Input:
3
12345678
20000
22334455667788
Output:
16 384
2 0
35 40320
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        tong = 0
        tich = 1
        le = len(n) // 2
        dem = 0
        # chan = len(n) // 2
        # if len(n) % 2 == 1: chan += 1
        for i in range (0,len(n)):
            if i % 2 == 0:
                tong += int(n[i])
            else:
                if n[i] != '0': tich *= int(n[i])
                else: dem += 1
        if dem == le: print(tong,0)
        else: print(tong,tich)