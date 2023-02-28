"""
Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.
Nhập vào dãy biểu diễn không quá 18 ký tự, hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.
Input:
3
1214AB
10210221
22222222
Output:
NO
YES
YES
"""

def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2': return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s): print("YES")
        else: print("NO")