"""
Cho mảng A[] gồm N số nguyên và số tự nhiên d.    Hãy thực hiện quay mảng A[] với d phần tử từ phải qua trái.
Ví dụ A[] = {1, 2, 3, 4, 5}, d = 2 ta nhận được mảng A[] = {3, 4, 5, 1, 2}.
Input:
2
5 2
1 2 3 4 5
10 3
2 4 6 8 10 12 14 16 18 20
Output:
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        for i in range(d,n): print(a[i], end = ' ')
        for i in range(d): print(a[i], end = ' ')
        print()