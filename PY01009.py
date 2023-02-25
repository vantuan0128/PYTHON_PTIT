s = input()
thuong = 0
hoa = 0
for x in s:
    if(x.islower()): thuong += 1
    else : hoa += 1
if(thuong >= hoa): print(s.lower())
else: print(s.upper())

"""
Biến đổi tất cả xâu thành viết thường, nếu số lượng chữ cái viết thường lớn hơn hoặc bằng số lượng chữ cái viết hoa.
Biến đổi tất cả xâu thành chữ hoa, nếu số lượng chữ cái viết hoa lớn hơn số lượng chữ cái viết thường.
"""