"""
Cho dãy số nguyên dương A[] có N phần tử. Các giá trị trong dãy không quá 1000.

Hãy sắp xếp các số nguyên tố trong dãy theo thứ tự tăng dần. Các giá trị không nguyên tố vẫn giữ nguyên vị trí như lúc đầu.

Xem ví dụ để hiểu rõ hơn yêu cầu bài toán.
Input:
8
4 6 3 8 7 2 5 9
Output:
4 6 2 8 3 5 7 9
"""
import math
def nto(n):
    if n<2: return False
    if n==2: return True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

if __name__ == "__main__":
    n = int(input())
    s = [int(x) for x in input().split()]
    a = []
    for i in s:
        if nto(i): a.append(i)
    a.sort()
    j = 0
    for i in s:
        if nto(i):
            print(a[j],end=' ')
            j+=1
        else: print(i,end=' ')