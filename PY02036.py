"""
Cho dãy số A[] có n phần tử là các số nguyên dương khác nhau, giá trị không quá 100.
 Hãy liệt kê các cặp số nguyên tố cùng nhau xuất hiện trong dãy theo thứ tự tăng dần, mỗi cặp số in trên một dòng.
Một cặp số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng 1.
Input:
5
3 7 9 6 13
Output:
3 7
3 13
6 7
6 13
7 9
7 13
9 13
"""

import math

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n-1):
        for j in range(i+1,n):
            if math.gcd(a[i],a[j]) == 1: print(a[i], a[j])