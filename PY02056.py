"""
Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.

Một số được coi là thuận nghịch nếu có từ 2 chữ số trở lên và nếu viết theo thứ tự ngược lại giá trị vẫn không thay đổi so với giá trị ban đầu. Ví dụ: 99, 121, 1331

Hãy tìm số thuận nghịch lớn nhất trong ma trận và các vị trí có giá trị bằng số thuận nghịch lớn nhất đó.
Ghi ra giá trị của số thuận nghịch lớn nhất. Sau đó lần lượt là các vị trí của số thuận nghịch lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy số thuận nghịch nào thì ghi ra NOT FOUND
Input:
6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
Output:
77
Vi tri [0][2]
Vi tri [3][1]
Vi tri [5][2]
Vi tri [5][3]
"""
def tn(n):
    s=str(n)
    l=len(s)
    if l<2: return False
    for i in range(l):
        if s[i]!=s[l-i-1]: return False
    return True

if __name__ == "__main__":
    n,m= map(int,input().split())
    a=[[0]]*n
    x=0
    for i in range(n): a[i]=[int(x) for x in input().split()]
    for i in range(n):
        for j in range(m):
            if tn(a[i][j]) and a[i][j]>x : x=a[i][j]
    if x==0: print('NOT FOUND')
    else:
        print(x)
        for i in range(n):
            for j in range(m):
                if a[i][j]==x:
                    print("Vi tri "+'['+str(i)+']'+'['+str(j)+']')