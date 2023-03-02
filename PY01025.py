"""
Khi  viết giá trị số nguyên trong Tiếng Anh, người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số (tính từ cuối).
Ví dụ số 153920529 được viết lại thành 153,920,529.
Input:
153920529
Output:
153,920,529
"""
if __name__ == "__main__":
    n = input()
    s = ""
    if len(n) <= 3: print(n)
    else:
        dem = 0;
        for i in range(len(n)-1,-1,-1):
            dem += 1;
            if dem % 3 == 0:
                s += n[i]
                s += ","
            else: s += n[i]
            # 925,029,351,
        if s[len(s)-1] == ",": s = s[:-1]
    print(s[::-1])
