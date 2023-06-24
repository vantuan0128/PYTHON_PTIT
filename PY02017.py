"""
Cho dãy số A[] gồm có N phần tử. Các phần tử trong dãy số đều xuất hiện với tần suất chẵn, chỉ có duy nhất 1 số có số lần xuất hiện là số lẻ. Nhiệm vụ của bạn là hãy tìm số này.
Input:
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
Output:
3
2
"""
def func():
    m={}
    n=int(input())
    s=[int(x) for x in input().split()]
    for i in s:
        if i in m: m[i]+=1
        else: m[i]=1
    for i in m:
        if m[i]%2==1:
            print(i)
            break
for i in range(int(input())):
    func()