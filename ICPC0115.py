"""
Một số nguyên dương N được gọi là số Krish nếu tổng giai thừa các chữ số của N bằng chính nó.
Ví dụ N = 145 = 1! + 4! + 5! = 145 là một số Krish. Cho số nguyên dương N, hãy kiểm tra N có phải là một số Krish hay không?
Đưa ra “Yes” nếu N là một số Krish, ngược lại đưa ra “No”.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10^8;
Input:
2
145
235
Output:
Yes
No
"""
def createa(a):
    a.append(1)
    for i in range(1,12):
        a.append(a[i-1] * i)

def func(n,a):
    m = n
    res = 0
    while n > 0:
        s = n % 10
        res += a[s]
        n //= 10
    return res == m

if __name__ == "__main__":
    t = int(input())
    a = []
    createa(a)
    # for x in a: print(x,end=' ')
    for _ in range(t):
        n = int(input())
        if func(n,a): print("Yes")
        else: print("No")