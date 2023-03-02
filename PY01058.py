"""
Cho số nguyên dương N có không quá 500 chữ số.
Hãy kiểm tra xem 4 chữ số cuối cùng
ghép lại có tạo thành một số nguyên tố hay không.
Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận
Input:
3
12234323130097
3443354654654654461123
43543543434554659999
Output:
YES
YES
NO
"""
import math

def SNT(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if n % i == 0: return False
    return True

def func():
    s = int(input())
    s = s % 10000;
    if SNT(s): print("YES")
    else: print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        func()