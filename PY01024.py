"""
Cho số nguyên dương N. Hãy kiểm tra xem N
có thỏa mãn đồng thời hai tính chất sau đây hay không?
Tổng chữ số của N chia hết cho 10
Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
"""
def check1(s):
    m = 0
    while s > 0:
        m += s % 10
        s //= 10
    return m % 10 == 0

def check2(s):
    m = s % 10
    s //= 10
    while s > 0:
        if abs(m-s%10) != 2: return False
        else:
            m = s % 10
            s //= 10
    return True

t = int(input())
for i in range(t):
    s = int(input())
    if check1(s) and check2(s): print("YES")
    else: print("NO")