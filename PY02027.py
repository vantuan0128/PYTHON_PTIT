"""
Cho N xâu ký tự bao gồm cả chữ số và chữ cái. Các chữ số liên tiếp sẽ tạo ra một số nguyên. Hãy sắp xếp các số tách được theo thứ tự tăng dần.

Chú ý: các chữ số 0 ở đầu nếu có sẽ không được tính. Ví dụ: các chữ số tách ra được là 00234 thì được tính như số 234, nếu là 00000000 thì được tính như số 0.
Input:
3
A129h
G07bxjq3
aaaaaaa4aaaa
Output:
3
4
7
129
"""
import re
n=int(input())
a=[]
regex='\d+'
while n>0:
    s=input()
    s=re.findall(regex,s)
    for i in s:
        if i not in a: a.append(int(i))
    n-=1
a.sort()
for i in a:
    print(i)