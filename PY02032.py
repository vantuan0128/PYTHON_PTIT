"""
Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.

Hãy liệt kê các số khác nhau xuất hiện trong A[] theo thứ tự tăng dần.
Input:
124356141111434356149
Output:
11 12 14 43 56

"""
import re

if __name__ == "__main__":
    s = input()
    regex = '\d'+'\d'
    a = re.findall(regex,s)
    b = set(a)
    b = sorted(b)
    for i in b: print(i,end=' ')