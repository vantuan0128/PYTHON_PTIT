"""
Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa.
Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau và
viết số lượng phía sau các chữ cái đó.
Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1
Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.
Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.
"""

t = int(input())
for i in range(t):
    s = input()
    for j in range(0,len(s)):
        if s[j].isdigit():
            for k in range(0,int(s[j])):
                print(s[j-1],end='')
        else: continue
    print()