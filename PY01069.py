"""
Chúng ta đều biết chỉ có 4 chữ số nguyên tố là 2, 3, 5, 7. Hãy liệt kê tất cả các số có ít nhất 4 chữ số nhưng không quá N chữ số và thỏa mãn tất cả các điều kiện sau:

Chỉ có các chữ số 2, 3, 5, 7
Có đầy đủ 4 chữ số 2, 3, 5, 7
Không phải là số chẵn.
Input:
4
Output:
2357
2375
2537
2573
2735
2753
3257
3275
3527
3725
5237
5273
5327
5723
7235
7253
7325
7523
"""
def Try(s,n,a,b,c,d):
    if len(s)==n and int(s[len(s)-1])!=2 and a>0 and b>0 and c>0 and d>0: print(s)
    if len(s)<n:
        Try(s+'2',n,a+1,b,c,d)
        Try(s+'3',n,a,b+1,c,d)
        Try(s+'5',n,a,b,c+1,d)
        Try(s+'7',n,a,b,c,d+1)
n= int(input())
for i in range(4,n+1):
    Try("",i,0,0,0,0)