"""
Cho số nguyên dương N có ít nhất 4 chữ số và không quá 500 chữ số.
Một số được gọi là số đầu cuối nguyên tố nếu thỏa mãn cả hai điều kiện:
Ba chữ số đầu ghép lại được một số nguyên tố
Ba chữ số cuối ghép lại được một số nguyên tố
Input:
3
12743
7337
12345678901234
Output:
YES
YES
NO
"""
import math

def SNT(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1),1):
        if n % i == 0: return False
    return True

def check(s):
    dau = int(s[0]+s[1]+s[2])
    cuoi = int(s[len(s)-3]+s[len(s)-2]+s[len(s)-1])
    return SNT(dau) and SNT(cuoi)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s): print("YES")
        else: print("NO")