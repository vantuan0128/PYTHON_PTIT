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
    s = input()
    n = 0
    if len(s) >= 4:
        str = ''
        for i in range(len(s)-4,len(s)):
            str = str + s[i]
            if str == '0': str = ''
        if str != '': n = int(str)
    else:
        str = ''
        for i in range(0,len(s)):
            str = str + s[i]
            if str == '0': str = ''
        if str != '': n = int(str)
    if SNT(n): print("YES")
    else: print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        func()