"""
Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.

Nhập thêm số nguyên dương K gọi là giá trị ngưỡng tối thiểu. Hãy liệt kê các số xuất hiện từ K lần trở lên trong dãy A[] theo thứ tự từ nhỏ đến lớn.
Ghi ra lần lượt các số khác nhau của dãy A[] thỏa mãn xuất hiện ít nhất K lần và số lần xuất hiện tương ứng, mỗi số viết trên một dòng theo thứ tự tăng dần.

Nếu không có số nào thỏa mãn ghi ra dòng chữ NOT FOUND
Input:
124356141111434356149
2
Output:
11 2
14 2
43 3
56 2

Input:
124356141111434356149
10
Output: NOT FOUND
"""
import re

if __name__ == "__main__":
    s = input()
    n = int(input())
    regex = '\d' + '\d'
    a = re.findall(regex, s)
    a = sorted(a)
    m = {}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    dem = 0
    for i in m:
        if m[i] >= n:
            print(i, m[i])
            dem += 1
    if dem == 0:
        print("NOT FOUND")
