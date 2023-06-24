"""
Cho dãy số A[] có n phần tử. Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần và các số lẻ theo thứ tự giảm dần.

In ra dãy kết quả đã sắp xếp trong đó vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.
Input:
10
1 2 3 4 5 6 7 7 9 6
Output:
9 2 7 4 7 6 5 3 1 6
"""
if __name__ == "__main__":
    n = int(input())
    s = []
    a = []  # chan
    b = []  # le
    while n > 0:
        m = [int(x) for x in input().split()]
        for i in m:
            s.append(i)
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)
        n -= len(m)
    a = sorted(a)
    b = sorted(b)
    tang = 0
    giam = len(b) - 1
    for i in range(len(s)):
        if int(s[i]) % 2 == 0:
            print(a[tang], end=' ')
            tang += 1
        else:
            print(b[giam], end=' ')
            giam -= 1