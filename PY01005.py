"""Cho số nguyên dương N có không quá 18 chữ số.
Hãy đếm xem số chữ số 4 cộng với số chữ số 7
trong N có phải bằng 4 hay bằng 7 hay không."""
s = input()
dem4 = 0
dem7 = 0
for i in s:
    if(int(i)==4): dem4 += 1
    elif(int(i)==7): dem7 += 1
    else: continue
if(dem4+dem7==4 or dem4+dem7==7): print("YES")
else: print("NO")
