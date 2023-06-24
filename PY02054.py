"""
Cho ma trận A kích thước N*M chỉ bao gồm các số nguyên dương.

Trong trường hợp N # M, hãy biến đổi ma trận A về dạng ma trận vuông theo quy tắc sau:

Nếu N > M, hãy loại bỏ các hàng có thứ tự lẻ trong ma trận ban đầu (thứ tự hàng tính từ 1) cho đến khi N = M. Ví dụ N = 6, M = 4 thì cần loại bỏ hàng thứ 1 và hàng thứ 3.
Nếu M > N, hãy loại bỏ các cột có thứ tự chẵn trong ma trận ban đầu (thứ tự cột tính từ 1). Ví dụ: N = 4, M = 6 thì cần loại bỏ cột thứ 2 và cột thứ 4.
Input:
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9
Output:
6 3 2 6
9 9 9 8
9 6 6 3
7 7 4 9

Input:
4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
Output:
2 7 4 3
6 2 7 2
7 2 9 1
9 9 0 7
"""
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [[0]] * n
    for i in range(n): a[i] = [int(x) for x in input().split()]
    if n == m:
        for i in range(n):
            for j in range(m):
                print(a[i][j], end=' ')
            print()
    elif n > m:
        dem = n - m
        for i in range(n):
            if (i + 1) % 2 == 1 and i + 1 > dem * 2:
                for j in range(m): print(a[i][j], end=' ')
                print()
            if (i + 1) % 2 == 0:
                for j in range(m): print(a[i][j], end=' ')
                print()
    else:
        dem = m - n
        for i in range(n):
            for j in range(m):
                if (j + 1) % 2 == 0 and j + 1 > dem * 2: print(a[i][j], end=' ')
                if (j + 1) % 2 == 1: print(a[i][j], end=' ')
            print()