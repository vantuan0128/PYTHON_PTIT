"""
Cho số nguyên dương không quá 9 chữ số.
Hãy làm tròn số N theo quy tắc sau:
Nếu N>10, làm tròn đến số hàng chục gần nhất
Sau đó nếu kết quả lớn hơn 100 thì làm tròn đến số hàng trăm gần nhất
Sau đó nếu kết quả lớn hơn 1000 thì làm trong đến số hàng nghìn gần nhất
Cứ tiếp tục như vậy …
Input:
7
15
14
5
99
12345678
44444445
1445
Output:
20
10
5
100
10000000
50000000
2000
"""
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = 1
        while n > 10**i:
            x = 10**i # số tròn
            tmp = n % x # số chia dư
            if tmp >= (x-tmp):
                n += x-tmp
            else: n -= tmp
            i += 1
        print(n)