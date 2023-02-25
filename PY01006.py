"""
Một số được xem là số may mắn nếu chỉ có các chữ số 4 và 7.
Cho số nguyên dương N không quá 200 chữ số.
Hãy kiểm tra xem N có phải số may mắn hay không.
"""

def LucKyNumber2(n):
    for i in n:
        if i != '4' and i != '7': return False
    return True

t = int(input())
for i in range(0,t):
    n = input()
    if(LucKyNumber2(n)):
        print("YES")
    else:
        print("NO")
