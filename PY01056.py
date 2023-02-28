"""
Cho một số nguyên dương không quá 500 chữ số.
Hãy kiểm tra xem số đó có thỏa mãn đồng thời ba tính chất sau hay không?
    Vị trí chẵn là chữ số chẵn
    Vị trí lẻ là chữ số lẻ
    Tổng chữ số là một số nguyên tố.
Input:
2
2345678521
1212121212121212121212121
Output:
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
    sum = 0
    for i in range(0,len(s)):
        sum += int(s[i])
        if i % 2 == 0:
            if int(s[i]) % 2 != 0: return False
        else:
            if int(s[i]) % 2 != 1: return False
    return SNT(sum)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s): print("YES")
        else: print("NO")
