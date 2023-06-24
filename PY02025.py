"""
Cho dãy số a[] có n phần tử và dãy số b[] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a[], tập hợp B là tập các số khác nhau trong b[].

Hãy tìm tập giao của A và B, hiệu A – B và hiệu B – A. Mỗi tập kết quả viết trên một dòng theo thứ tự từ nhỏ đến lớn.

Dòng đầu ghi tập giao của A và B

Dòng thứ 2 ghi tập A – B

Dòng thứ 3 ghi tập B - A
Input:
5 6
1 2 3 4 5
3 4 5 6 7 8
Output:
3 4 5
1 2
6 7 8
"""
if __name__ == "__main__":
    n, m = map(int, input().split())
    c = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    a = []
    b = []
    for i in c:
        if i not in a: a.append(i)
    for i in d:
        if i not in b: b.append(i)
    a.sort()
    b.sort()
    for i in a:
        if i in b: print(i, end=' ')
    print()
    for i in a:
        if i not in b: print(i, end=' ')
    print()
    for i in b:
        if i not in a: print(i, end=' ')
    print()