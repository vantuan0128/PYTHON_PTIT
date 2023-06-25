"""
Cho một xâu ký tự. Quá trình mã hóa D - R - M sẽ trải qua ba bước Chia (Divide), Xoay (Rotate) và Trộn (Merge). Ví dụ với xâu: EWPGAJRB  quá trình này sẽ diễn ra như sau:

Devide: Xâu ban đầu được chia thành 2 nửa: “EWPG” và “AJRB”.
Rotate: Với mỗi nửa, tính toán giá trị xoay của nó bằng cách tính tổng giá trị các ký tự. (A = 0; B = 1; … Z = 25).  Giá trị xoay của “EWPG” là 4 + 22 + 15 + 6 = 47. Tiến hành xoay xâu  “EWPG”  đi 47 ký tự (tính cả bước chuyển từ Z về A nếu cần) ta sẽ được xâu: “ZRKB”. Tương tự, “AJRB” được chuyển thành “BKSC”
Merge: Trong bước này, mỗi ký tự trong xâu thứ nhất sẽ được xoay theo giá trị của ký tự ở vị trí tương ứng trong xâu thứ 2. Trong ví dụ trên, chữ Z trong xâu thứ nhất sẽ xoay theo giá trị B, tức là 1 vị trí. Do đó sẽ chuyển thành chữ A. Tiếp tục thực hiện với các ký tự tiếp theo ta sẽ có kết quả là “ABCD”.
Input:
3
EWPGAJRB
BB
TPQJDRJWSQXGRRIPXFMINTELHBJA
Output:
ABCD
E
FIRSTDATAFILEV
"""
def func():
    ss=input()
    l=int(len(ss)/2)
    str=''
    str1=''
    #devide
    for i in range(l): str+=ss[i]
    for i in range(l,l*2): str1+=ss[i]
    #rotate
    x=0
    x1=0

    for i in str: x+=ord(i)-65
    for i in str1: x1+=ord(i)-65

    s=''
    s1=''
    for i in str:
        m=(ord(i)-65+x)%26
        s+= chr(m+65)
    for i in str1:
        m=(ord(i)-65+x1)%26
        s1+= chr(m+65)

    #Merge
    for i in range(l):
        m=(ord(s[i])-65 + ord(s1[i])-65)%26
        print(chr(m+65),end='')
    print()

for i in range(int(input())):func()
