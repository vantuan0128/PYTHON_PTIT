"""
Cho dãy số A[], B[] và C[] là dãy không giảm và có lần lượt N, M, K phần tử. Nhiệm vụ của bạn là hãy tìm các phần tử chung của 3 dãy số này.
Input:
3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9
Output:
20 80
5 5
NO
"""
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m, k = map(int, input().split())
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        c = [int(x) for x in input().split()]
        dem, x, y, z = 0, 0, 0, 0
        while x < n and y < m and z < k:
            if a[x] == b[y] == c[z]:
                print(a[x], end=' ')
                dem += 1
                x, y, z = x + 1, y + 1, z + 1
            elif a[x] < b[y]:
                x += 1
            elif b[y] < c[z]:
                y += 1
            else:
                z += 1
        if dem == 0: print("NO", end=' ')
        print()
        t -= 1
