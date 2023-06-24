"""
Cho hai dãy số A[] và B[] có cùng N phần tử.
Dãy số A[] được gọi là phù hợp với dãy số B[] khi và chỉ khi tồn tại một phép sắp đặt lại các phần tử trong A[] và B[]
sao cho phần tử thứ i của A[] nhỏ hơn hoặc bằng phần tử thứ i của mảng B[] (với tất cả vị trí trong dãy).
Hãy xác định hai dãy số A[] và B[] có phù hợp với nhau hay không?
Đưa ra kết quả mỗi test theo từng dòng. Kết quả “YES” nếu A[] phù hợp với B[], ngược lại đưa ra “NO”.
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
def func():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a = sorted(a)
    b = sorted(b)
    dem = 0
    for i in range(n):
        if a[i] <= b[i]: dem += 1
    if dem == n: print("YES")
    else: print("NO")

if __name__ == "__main__":
    for i in range(int(input())):
        func()