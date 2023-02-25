"""Cho một phép toán có dạng a + b = c
với a,b,c chỉ là các số nguyên dương có một chữ số.
Hãy kiểm tra xem phép toán đó có đúng hay không."""
s = input()
a,b,c = int(s[0]), int(s[4]), int(s[8])
if(a + b == c):
    print("YES")
else:
    print("NO")