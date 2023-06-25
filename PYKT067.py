"""
Cho số nguyên dương N. Nhiệm vụ của bạn là hãy liệt kê tất cả các hoán vị của 1, 2, .., N theo thứ tự ngược. Ví dụ với N = 3 ta có kết quả: 321, 312, 231, 213, 132, 123.
Input:
2
2
3
Output:
2
21 12
6
321 312 231 213 132 123
"""
import itertools
for i in range(int(input())):
    n=int(input())
    a=[]
    for i in range(1,n+1): a.append(i)
    x=list(itertools.permutations(a))
    x.reverse()
    print(len(x))
    for i in x:
        for j in i: print(j,end='')
        print(end=' ')
    print()