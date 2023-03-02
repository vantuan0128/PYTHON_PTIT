"""
Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số
nguyên dương b thỏa mãn cả hai điều kiện:
a + b ≤ N
a + b chia hết cho K
Input:
10 1 10
10 6 40
Output:
-1
2 8 14 20 26
"""

def check(a,K,N):
    if a >= N :
        print(-1)
        return
    # Lưu ý thứ tự K và a % K
    dautien = K - a % K
    if dautien > N - a:
        print(-1)
        return
    i = dautien
    while i <= N-a:
        print(i,end=' ')
        i += K

if __name__ == "__main__":
    a,K,N = map(int,input().split())
    ok = False
    b = []
    check(a,K,N)
