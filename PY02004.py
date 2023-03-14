"""
Cho dãy số A[] chỉ có các giá trị nhị phân 0 và 1.
Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.
Input
Dòng 1 ghi số N là số phần tử của dãy (không quá 100).
Dòng 2 ghi N số nhị phân.
Input:
6
1 0 0 1 1 1
Output: 2
"""

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(0, n-1, 1):
        if a[i] != a[i + 1]: cnt += 1
    print(cnt)