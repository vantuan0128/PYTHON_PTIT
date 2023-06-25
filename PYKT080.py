"""
Trước diễn biến phức tạp của dịch bệnh, thành phố đang có chủ chương thống kê dịch tễ các trường hợp liên quan đến bệnh nhân mắc COVID-19.

Thông tin về bệnh nhân được biểu diễn trên ma trận. Bạn hãy thực hiện thống kê nhanh các trường hợp có nguy cơ lây nhiễm. Nguyên tắc tính là đếm các trường hợp xung quanh bệnh nhân đã tiếp xúc (8 ô xung quanh).
Dòng đầu tiên là 2 số M, N là các số nguyên <= 100, cho biết kích thước của ma trận.

Tiếp theo là ma trận M x N, các số nguyên A[i][j] có giá trị < 10. Vị trí của mỗi bệnh nhân được đánh số -1. Các ô mang giá trị >= 0 thể hiện số trường hợp có nguy cơ lây nhiễm (không tính các bệnh nhân).

Output:

Tổng số các ca có nguy cơ lây nhiễm trên toàn thành phố.
Input:
4 4
1 1 0 1
2 -1 4 5
0 0 0 0
1 0 2 1
Output:
8
"""
m, n = [int(i) for i in input().split()]
b = []
a = [[]] * m
for i in range(m):
    a[i] = [int(x) for x in input().split()]
    for j in range(n):
        if a[i][j] == -1:
            b.append([i, j])
dem = 0
while len(b) > 0:
    u = b[0]
    b.pop(0)
    x0, x, x1, y0, y, y1 = u[0] - 1, u[0], u[0] + 1, u[1] - 1, u[1], u[1] + 1
    if x0 >= 0 and x0 < m:
        dem += a[x0][y]
        a[x0][y] = 0
    if x1 >= 0 and x1 < m:
        dem += a[x1][y]
        a[x1][y] = 0

    if y0 >= 0 and y0 < n:
        dem += a[x][y0]
        a[x][y0] = 0
    if y1 >= 0 and y1 < n:
        dem += a[x][y1]
        a[x][y1] = 0

    if y0 >= 0 and y0 < n and x0 >= 0 and x0 < m:
        dem += a[x0][y0]
        a[x0][y0] = 0
    if y1 >= 0 and y1 < n and x1 >= 0 and x1 < m:
        dem += a[x1][y1]
        a[x1][y1] = 0

    if y1 >= 0 and y1 < n and x0 >= 0 and x0 < m:
        dem += a[x0][y1]
        a[x0][y1] = 0
    if y0 >= 0 and y0 < n and x1 >= 0 and x1 < m:
        dem += a[x1][y0]
        a[x1][y0] = 0
print(dem)