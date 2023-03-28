"""
Bộ ba số nguyên tố được gọi là Prime- Triplet nếu nó là bộ ba số nguyên tố dưới dạng
(p, p +2, p + 6) hoặc (p, p + 4, p+6), trong đó p là một số nguyên tố.
Ví dụ các bộ ba số (5, 7, 11) hoặc (7, 11, 13) đều là các Prime-Triplet.
Cho số tự nhiên N, nhiệm vụ của bạn là đếm số các Prime-Triplet nhỏ hơn N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10^6;
Input:
2
15
25
Output:
2
5
"""
from math import isqrt

a = [1]*1000001

def sieve():
    a[0] = a[1] = 0
    for i in range(2,isqrt(1000001) + 1):
        if a[i]:
            for j in range(i*i,1000001,i): a[j] = 0

if __name__ == "__main__":
    t = int(input())
    sieve()
    for _ in range(t):
        n = int(input())
        cnt = 0
        for i in range(2,n-6,1):
            if a[i] == 1 and a[i + 2] == 1 and a[i + 6] == 1: cnt += 1
            if a[i] == 1 and a[i + 4] == 1 and a[i + 6] == 1: cnt += 1
        print(cnt,end="\n")