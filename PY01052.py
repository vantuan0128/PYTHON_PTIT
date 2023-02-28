"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.
Input:
2
12341
22222222222222222222
Output:
YES
NO
"""
import math

s = ""

def SNT(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if n % i == 0: return False
    return True

def func():
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if SNT(sum): print("YES")
    else: print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        func()