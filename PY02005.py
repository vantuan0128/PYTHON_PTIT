"""
Cho dãy số A[] gồm có N phần tử.
Một cặp nghịch thế là một cặp số (u, v) sao cho u < v và A[u] > A[v].
Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A[] ban đầu.
Input:
5
2 4 1 3 5
Output:
3
"""

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    dem = 0
    for i in range(0,n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]: dem += 1
    print(dem)