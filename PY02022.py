"""
Cho dãy số nguyên dương A[] có N phần tử.
Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.
Các số được liệt kê theo thứ tự xuất hiện.
Input:
10
2 4 7 5 7 8 9 3 7 2
Output:
2 2
7 3
5 1
3 1
"""

import math

def SNT(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if n % i == 0: return False
    return True

if __name__ =="__main__":
    n = input()
    a = list(map(int,input().split()))
    b = [0]*(max(a)+1)
    for i in range(len(a)):
        if SNT(a[i]):
            b[a[i]] += 1
        else: continue
    for i in range(len(a)):
        if b[a[i]] != 0:
            print(a[i],end=' ')
            print(b[a[i]],end='\n')
            b[a[i]] = 0