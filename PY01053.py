"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem N có chia hết cho 3 hay không.
"""

def check(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0: return True
    else: return False

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if check(n): print('YES')
        else: print('NO')