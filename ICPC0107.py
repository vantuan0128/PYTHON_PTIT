"""
Cho hai số nguyên dương X1, X2. Ta chỉ được phép thay đổi chữ số p thành chữ số q và ngược lại chữ.
Hãy đưa ra tổng nhỏ nhất và tổng lớn nhất các số X1 và X2 được tạo ra theo nguyên tắc kể trên.
Input:
1
5 6
645
666
Output:
1100  1312
"""
import math
def func():
    m,n=map(int,input().split())
    a=input().strip()
    if a.count(' '): a,b=a.split()
    else: b=input()
    p=str(min(m,n))
    q=str(max(m,n))
    print(int(a.replace(q,p))+int(b.replace(q,p)),end=' ')
    print(int(a.replace(p,q))+int(b.replace(p,q)))
for i in range(int(input())): func()