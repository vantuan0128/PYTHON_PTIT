"""
Cho hai dãy số A[] và B[] có cùng N phần tử. Dãy số A[] được gọi là phù hợp với dãy số B[] khi và chỉ khi
tồn tại một phép sắp đặt lại các phần tử trong A[] và B[] sao cho phần tử thứ i của A[] nhỏ hơn
hoặc bằng phần tử thứ i của mảng B[] (với tất cả vị trí trong dãy).
Hãy xác định hai dãy số A[] và B[] có phù hợp với nhau hay không?
Input:
2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84
Output:
YES
NO
"""

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ok = 1
        a.sort()
        b.sort()
        for i in range(n):
            if a[i] > b[i]:
                ok = 0
                break
        if ok: print('YES')
        else: print('NO')