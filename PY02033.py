"""
Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.

Hãy liệt kê các số khác nhau xuất hiện trong A[] theo thứ tự xuất hiện.

Input

Chỉ có một dòng ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.
Input:
124356141111434356149
Output:
12 43 56 14 11

"""
import re

if __name__ == "__main__":
    s = input()
    regex = '\d'+'\d'
    a = re.findall(regex,s)
    b = []
    for i in a:
        if i not in b: b.append(i)
    for i in b: print(i,end=' ')