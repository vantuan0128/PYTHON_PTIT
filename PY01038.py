"""
Cho một số nguyên dương N.
Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N.
Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7
hoặc khi đã thực hiện quá 1000 bước lặp.
Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên
hoặc ghi ra -1 nếu không thể tìm ra đáp án.
"""
def reverseN(n):
    m = 0
    while n > 0:
        m = m*10 + n%10
        n //= 10
    return m

t = int(input())
for i in range(t):
    n = int(input())
    dem = 0
    ok = 0
    if n % 7 == 0:
        print(n)
        ok = 1
    else:
        while dem!= 1000:
            n = n + reverseN(n)
            dem += 1
            if n % 7 == 0:
                print(n)
                ok = 1
                break
    if ok == 0: print("-1")