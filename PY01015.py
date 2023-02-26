"""
Một số được gọi là số không giảm nếu
không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.
Viết chương trình kiểm tra số nguyên dương có thỏa mãn
là số không giảm hay không.
"""

t = int(input())
for i in range(t):
    s = input()
    ok = False
    for j in range(0,len(s)-1):
        if int(s[j]) > int(s[j+1]):
            print("NO")
            ok = True
            break
        else: continue
    if ok == False: print("YES")