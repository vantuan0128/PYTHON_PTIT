"""
Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.

Hãy liệt kê và đếm các số khác nhau xuất hiện trong A[] theo thứ tự xuất hiện.
Input:
124356141111434356149
Output:
12 1
43 3
56 2
14 2
11 2
"""
import re

if __name__ == "__main__":
    s = input()
    regex = '\d'+'\d'
    a = re.findall(regex,s)
    b = {}
    for i in a:
        if i not in b: b[i] = 1
        else: b[i] += 1
    for i in b:
        print(i,b[i])