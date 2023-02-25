"""
Viết chương trình kiểm tra xem số nguyên dương N có thỏa mãn tính chất:
nếu ta lấy hai chữ số đầu và hai chữ số cuối của nó
thì sẽ tạo ra số có hai chữ số giống nhau hay không?
"""

t = int(input())
for i in range(t):
    s = input()
    m = int(s[0])*10 + int(s[1])
    n = int(s[len(s)-2])*10 + int(s[len(s)-1])
    if m == n: print("YES")
    else: print("NO")