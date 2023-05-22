"""
Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.

Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).
Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy tổng giá trị các phần tử ở nửa trên trừ đi tổng giá trị các phần tử ở nửa dưới.

Nhập thêm một giá trị K gọi là ngưỡng cân đối của ma trận.  Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối,
nếu lớn hơn K thì không cân đối.

Hãy xác định độ chênh lệch và tính cân đối của ma trận.
Input:
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
Output:
NO
11
"""

if __name__ == "__main__":
    n=int(input())
    s=[[]] * n
    for i in range(n):
        s[i]= [int(x) for x in input().split()]
    k=int(input())
    sumup=0
    sumd=0
    for i in range(n):
        for j in range(n):
            if j<n-i-1:sumup+=s[i][j]
            if j>=n-i:sumd+=s[i][j]
    u=abs(sumup-sumd)
    if u<=k: print("YES")
    else: print("NO")
    print(u)