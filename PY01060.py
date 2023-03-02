"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:
Tích các chữ số ở vị trí chẵn – giá trị tích chữ số có thể đến 18 chữ số.
Chú ý khi tính tích bỏ qua các chữ số 0.
Tổng các chữ số ở vị trí lẻ
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        tong = 0
        tich = 1
        chan = len(n) // 2
        dem = 0
        # chan = len(n) // 2
        if len(n) % 2 == 1: chan += 1
        for i in range (0,len(n)):
            if i % 2 == 1:
                tong += int(n[i])
            else:
                if n[i] != '0': tich *= int(n[i])
                else: dem += 1
        if dem == chan: print(0,tong)
        else: print(tich,tong)