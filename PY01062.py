"""
Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
Số chữ số của nó là một số nguyên tố
Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

Input:
3
1234567
22334455667
23400300489898989
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

def check(n):
    demnt = 0
    dem = 0
    m = 0
    while n > 0:
        if SNT(n%10):
            demnt += 1
            m += 1
        else:
            dem += 1
            m += 1
        n //= 10
    return demnt > dem and SNT(m)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if check(n): print("YES")
        else: print("NO")