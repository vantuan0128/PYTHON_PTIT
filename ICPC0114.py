"""
Một số nguyên dương N được gọi là Perfect Prime nếu
N là số nguyên tố;
đảo ngược các chữ số của N cũng là một số nguyên tố;
tổng các chữ số của N là một số nguyên tố và
mỗi chữ số của N cũng là một số nguyên tố.
Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không?
Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10^7;
Input:
3
13
753
757
Output:
No
No
Yes
"""
from math import isqrt

def snt(n):
    if n < 2: return False
    for i in range(2,isqrt(n)+1,1):
        if n % i == 0: return False
    return True

def check(n):
    m = n
    res = 0
    sum = 0
    while n > 0:
        if not snt(n % 10): return False
        res = res * 10 + n % 10
        sum += n % 10
        n //= 10
    return snt(sum) and snt(res) and snt(m)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if check(n): print("Yes")
        else: print("No")