"""
Một số kết thúc bởi hai chữ số 86 được gọi là số phát lộc.
 Cho một số nguyên dương không quá 500 chữ số,
 hãy kiểm tra số đó có phải số phát lộc hay không.
"""
t = int(input())
for i in range(t):
    s = input()
    if len(s) == 1 : print("NO")
    else:
        if s[-1]=='6' and s[-2]=='8': print("YES")
        else:
            print("NO")