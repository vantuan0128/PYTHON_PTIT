"""
Nhập xâu s1, giả sử gọi xâu đảo là s2. Hãy kiểm tra xem
khoảng cách ký tự cạnh nhau trong hai xâu có thỏa mãn công thức sau hay không:
|s1[i] – s1[i-1]| = |s2[i] – s2[i-1]| với tất cả giá trị 0 < i < N
Ghi ra YES hoặc NO.
Input:
2
acxz
bcxz
Output:
YES
NO
"""

def check(s1):
    s2 = s1[::-1]
    for i in range(1,len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])): return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s1 = input()
        if check(s1): print('YES')
        else: print('NO')
