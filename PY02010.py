"""
Cho dãy số có N số nguyên dương. Các số trong dãy có thể tới 100 chữ số.

Hãy tìm số nhỏ nhất và số lớn nhất trong dãy. Nếu cả dãy bằng nhau thì in ra BANG NHAU.

Input

Có nhiều bộ test. Mỗi bộ test bắt đầu với số N (không quá 20). Tiếp theo là N dòng, mỗi dòng ghi một số trong dãy, giá trị đều nguyên dương nhưng có thể có chữ số 0 ở đâu, và có thể tới 100 chữ số.

Input kết thúc khi N = 0.

Output

Với mỗi test, ghi ra trên một dòng số nhỏ nhất và lớn nhất. Nếu tất cả dãy bằng nhau thì ghi ra BANG NHAU.
Input:
5
1
2
3
4
5
3
001
22
33333333333333333333333333333333333
3
1
1
1
0
Output:
1 5
1 33333333333333333333333333333333333
BANG NHAU
"""
if __name__ == "__main__":
    while 1:
        n = int(input())
        if n == 0: break
        a = []
        while n > 0:
            a.append(int(input()))
            n -= 1
        if min(a) == max(a):
            print("BANG NHAU")
        else:
            print(min(a), max(a))
