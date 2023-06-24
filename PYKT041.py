"""
Cho một lưới hình vuông kích thước N*N. Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)).
Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.
Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)
N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)
Ghi ra số cặp đồng xu đếm được.
Input:
4
CC..
C..C
.CC.
.CC.
Output:
9
"""
def gt(n):
    if n == 0:
        return 1
    return n * gt(n - 1)

if __name__ == "__main__":
    n = int(input())
    a = [[]]*n

    for i in range(n): a[i] = input()
    m = 0
    for i in range(n):
        dem = 0
        for j in range(n):
            if a[i][j] == 'C': dem += 1
        if dem >= 2:
            m += int(gt(dem)/(gt(2)*gt(dem-2)))

    for i in range(n):
        dem = 0
        for j in range(n):
            if a[j][i] == 'C': dem += 1
        if dem >= 2:
            m += int(gt(dem)/(gt(2)*gt(dem-2)))

    print(m)