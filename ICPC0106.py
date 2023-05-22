"""
Cho xâu nhị phân X[] có độ dài n. Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
T, n, X[] thỏa mãn ràng buộc : 1≤T≤10; 1≤ n≤10^5; X[i] =0, 1;
Input:
2
8
10010100010010101
2
10010100010010101
Output:
224225
10010100010010101
"""
n = int(input())
while n>0:
    a = ['000','001','010','011','100','101','110','111']
    b = ['00','01','10','11']
    c = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    k = int(input())
    s = input()
    l = len(s)
    if k == 2: print(s)

    elif k == 8:
        if l % 3 == 1: s = '00' + s
        if l % 3 == 2: s = '0' + s
        sum = ''
        for i in range(0,l,3):
            s1 = s[i] + s[i+1] + s[i+2]
            for j in range(len(a)):
                if s1 == a[j]:
                    sum += str(j)
                    break
        print(sum)

    elif k == 4:
        if l % 2 == 1: s = '0' + s
        sum = ''
        for i in range(0,l,2):
            s1 = s[i] + s[i+1]
            for j in range(len(b)):
                if s1 == b[j]:
                    sum += str(j)
                    break
        print(sum)
    elif k == 16:
        if l % 4 == 1: s = '000' + s
        if l % 4 == 2: s = '00' + s
        if l % 4 == 3: s = '0' + s
        sum = ''
        for i in range(0,l,4):
            s1 = s[i] + s[i+1] + s[i+2] + s[i+3]
            for j in range(len(c)):
                if s1 == c[j]:
                    if j >= 10:
                        sum += chr(j+55)
                    else: sum += str(j)
                    break
        print(sum)
    n -= 1



