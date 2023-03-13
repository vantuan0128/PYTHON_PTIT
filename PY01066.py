"""
Một xâu ký tự được gọi là “thăng bằng” nếu khoảng cách của tất cả các cặp ký tự cạnh nhau trong xâu đó đều đúng bằng khoảng cách của hai vị trí tương ứng trong xâu đảo của nó.
Ví dụ xâu s1 có độ dài N và xâu đảo của nó là s2 thì xâu này sẽ thỏa mãn tính chất thăng bằng nếu:
|s1[i] – s1[i-1]| = |s2[i] – s2[i-1]| với tất cả giá trị 0 < i < N
Hãy kiểm tra xem một xâu ký tự bất kỳ có phải là xâu “thăng bằng” hay không.
Input:
2
acxz
bcxz
Output:
YES
NO
"""
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        t = ''.join(reversed(s))
        # t = s[::-1]
        ok = 0
        for i in range(1, len(s)):
            if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(t[i]) - ord(t[i - 1])):
                print("NO")
                ok = 1
                break
        if ok == 0: print("YES")