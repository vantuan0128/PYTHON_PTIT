"""
Nhập số nguyên dương N (1 < N < 10000).
Viết chương trình tính tổng:
    S = 1 + 1/3 + 1/5 + … + 1/N nếu N lẻ
    S = 1/2 + 1/4 + 1/6 + … + 1/N nếu N chẵn
Kết quả được in ra với 6 chữ số phần thập phân.
Input: 10
Output: 1.141667
- Co 3 cach de format:
C1: round(sum,6)
C2: "{0:.6f}".format(sum)
C3: '%.6f' % sum
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            sum = 0
            for i in range(2,n+1,2):
                sum += 1/i
            print('%.6f' % sum)
        else:
            sum = 0
            for i in range(1, n + 1, 2):
                sum += 1 / i
            print("{0:.6f}".format(sum))