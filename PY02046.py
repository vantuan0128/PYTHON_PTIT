"""
Cho dãy số A[] có N phần tử là các số nguyên dương không quá 1000. Sau khi loại bỏ tất cả các giá trị bị lặp lại ở trong A[] ta tạo được dãy B[] có m phần tử là các giá trị khác nhau theo đúng thứ tự xuất hiện trong dãy A[].

Hãy tìm vị trí i nhỏ nhất (tính từ 0) trong dãy B[] thỏa mãn:

Tổng các phần tử từ B[0] đến B[i] là một số nguyên tố
Tổng các phần tử từ B[i+1] đến B[m-1] cũng là một số nguyên tố.
Giải thích test 1:
Dãy B[] = {3, 6, 7, 4}
Vị trí 0 thỏa mãn vì 3 là số nguyên tố; 6+7+4 = 17 cũng là số nguyên tố.
Input:
10
3 6 7 3 4 7 3 6 4 4
-> 0
10
3 6 7 3 5 7 3 6 6 7
-> NOT FOUND
"""
import math
def nto(n):
    if n<2: return False
    if n==2: return True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    sum = 0
    for i in a:
        if i not in b:
            b.append(i)
            sum+=i
    l = len(b)
    tong = 0
    check = 0
    for i in range(l):
        tong += b[i]
        if nto(tong) and nto(sum-tong):
            print(i)
            check = 1
            break
    if check == 0: print("NOT FOUND")