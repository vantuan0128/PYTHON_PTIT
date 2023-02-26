"""
Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:
Có từ 3 chữ số trở lên
Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó
thỏa mãn thứ tự tăng dần (tăng chặt)
còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
"""

def check(s):
    if int(s) < 10**2 : return False
    else:
        for i in range(0,len(s)-1):
            if int(s[i]) < int(s[i+1]): continue
            elif int(s[i]) == int(s[i+1]): return False
            else:
                for j in range(i,len(s)-1):
                    if int(s[j]) > int(s[j + 1]): continue
                    else: return False
    return True

t = int(input())
for i in range(t):
    s = input()
    if check(s): print('YES')
    else: print('NO')