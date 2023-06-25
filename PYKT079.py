"""
Cho mảng A[] gồm n số nguyên dương. Gọi L, R là max và min các phần tử của A[]. Nhiệm vụ của bạn là tìm số phần tử cần thiết cần thêm vào mảng để mảng có đầy đủ các số trong khoảng [L, R]. Ví dụ A[] = {5, 7, 9, 3, 6, 2 }
 ta nhận được kết quả là 2 tương ứng với các số còn thiếu là 4, 8.
Input:
2
5
4 5 3 8 6
3
2 1 3
Output:
1
0
"""
def func():
    n=int(input())
    a=[]
    s=[int(x) for x in input().split()]
    for i in s:
        if i not in a: a.append(i)
    a=sorted(a)
    l=len(a)
    x=max(a)-min(a)
    print(x+1-l)
for i in range(int(input())): func()