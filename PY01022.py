"""
Cho một số nguyên (có thể âm) không quá 100.000 chữ số.
Mỗi bước thực hiện thay thế số nguyên này bằng giá trị tổng chữ số của số đó.
Hỏi sau mấy bước thì số đó chỉ còn duy nhất 1 chữ số.
Input:
10
919
6
Output:
1
3
1
"""
if __name__ == "__main__":
    dem = 0
    n = int(input())
    while 1:
        if n >= 10:
            n = sum(int(i) for i in str(n))
            dem += 1
        elif n < 0:
            x = ord('-')-ord('0')
            n = abs(n)
            n = sum(int(i) for i in str(n))+x
            dem += 1
        else: break
    print(dem)