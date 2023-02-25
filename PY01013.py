# Cho hai số nguyên dương a và b.
# Hãy kiểm tra xem ước số chung lớn nhất của hai số này có
# tổng chữ số là nguyên tố hay không.
#
# Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14.
# Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.
import math

def snt(n):
    if n < 2: return False
    if n == 2: return True
    if n!=2 and n%2==0: return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0: return False
    return True

def tongSo(n):
    m = 0
    while n>0:
        m += n%10
        n //= 10
    return m

def check(a,b):
    t = math.gcd(int(a),int(b))
    if snt(tongSo(t)): print("YES")
    else: print("NO")

t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    check(a,b)
