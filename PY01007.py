"""
Ngân hàng thông báo lãi suất là X % mỗi năm.
Với số tiền gửi vào là N. Sau mỗi năm, tiền lãi sẽ được cộng dồn.
Hỏi sau bao nhiêu năm thì số tiền đạt được ít nhất là M.
"""

t = int(input())
for i in range(t):
    n,x,m = map(float,input().split())
    years = 0
    while n < m:
        n = n + n * x/100
        years += 1
    print(years)