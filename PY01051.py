"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem tổng các chữ số của N có phải là một số thuận nghịch hay không.
Một số chỉ được coi là thuận nghịch nếu nhiều hơn 1 chữ số
và số đảo của nó đúng bằng nó.
"""
def check(s):
    m = s
    tmp = 0
    while s > 0:
        tmp = tmp*10 + s % 10
        s //= 10
    return tmp == m

t = int(input())
for i in range(t):
    s = int(input())
    if s < 10: print("NO")
    else:
        sum = 0
        while s > 0:
            sum += s % 10
            s //= 10
        if sum >= 10 and check(sum): print("YES")
        else: print("NO")