"""
Cho một xâu ký tự có thể có các ký tự chữ cái và chữ số.
Người ta thực hiện một phép mã hóa đơn giản, trong đó
đếm từ trái qua phải các ký tự giống nhau liên tiếp và
viết số đếm trước ký tự đó.
VD: AACDD -> 2A1C2D
"""
t = int(input())
for _ in range(t):
    a = []
    dem = 1
    s = input()
    for i in range(len(s)-1):
        if s[i] == s[i+1]: dem += 1
        else:
            a.append(str(dem)+s[i])
            dem = 1
    a.append(str(dem)+s[len(s)-1])
    print(''.join(a))