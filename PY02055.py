"""
Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.

Hãy tìm số nguyên tố lớn nhất trong ma trận và các vị trí có giá trị bằng số nguyên tố lớn nhất đó.
Ghi ra giá trị của số nguyên tố lớn nhất. Sau đó lần lượt là các vị trí của số nguyên tố lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy số nguyên tố nào thì ghi ra NOT FOUND
Input:
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29
Output:
29
Vi tri [2][1]
Vi tri [3][0]
Vi tri [5][3]
"""
import math

def nto(n) :
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return 1

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    a=[[0]]* n
    x=0
    for i in range(n):
            a[i]=[int(x) for x in input().split()]
    for i in range(n):
        for j in range(m):
            if nto(a[i][j]) and a[i][j]>x:x=a[i][j]
    if x==0: print('NOT FOUND')
    else:
        print(x)
        for i in range(n):
            for j in range(m):
                if a[i][j]==x:
                    print("Vi tri "+'['+str(i)+']'+'['+str(j)+']')