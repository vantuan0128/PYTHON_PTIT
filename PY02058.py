"""
Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.

Một số được coi là số may mắn nếu giá trị của nó đúng bằng khoảng cách giữa số lớn nhất và số nhỏ nhất của ma trận.

Trong test ví dụ dưới đây, số lớn nhất là 77, số nhỏ nhất là 10. Giá trị may mắn là 67.

Hãy tìm xem trong ma trận có tồn tại số may mắn hay không. Nếu có thì ở các vị trí nào?
Ghi ra giá trị bằng số may mắn nếu tìm được. Sau đó lần lượt là các vị trí tìm thấy, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy giá trị bằng số may mắn nào thì ghi ra NOT FOUND
Input:
6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
Output:
67
Vi tri [2][1]
Vi tri [3][3]
"""
if __name__ == "__main__":

    n, m = map(int, input().split())
    a = [[0]] * n
    x = 0
    for i in range(n): a[i] = [int(x) for x in input().split()]
    min = 1001
    max = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > max: max = a[i][j]
            if a[i][j] < min: min = a[i][j]
    for i in range(n):
        for j in range(m):
            if a[i][j] == max - min: x = max - min
    if x == 0:
        print('NOT FOUND')
    else:
        print(x)
        for i in range(n):
            for j in range(m):
                if a[i][j] == x:
                    print("Vi tri " + '[' + str(i) + ']' + '[' + str(j) + ']')