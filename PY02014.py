"""
Cho dãy số A[] có N số nguyên dương. Người ta muốn biến đổi tất cả các số trong dãy về số nguyên tố. Tại mỗi bước, mỗi số chưa nguyên tố được phép tăng hoặc giảm 1 đơn vị để biến đổi dần về số nguyên tố gần nhất.

Hãy tính xem cần ít nhất bao nhiêu bước cần thực hiện để biến đổi tất cả các phần tử của dãy về nguyên tố.
Input:
8
13 5 8 7 9 15 26 34
Output:
3
"""
import math


def nto(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    s = []
    for i in a:
        if nto(i) == False and i not in s: s.append(i)
    if s != []:
        xs = 0
        for x in s:
            k, l = x, x
            while 1:
                if nto(k) == True: break
                k += 1
            while 1:
                if nto(l) == True: break
                l -= 1
            res = min(k - x, x - l)
            xs = max(xs, res)
        print(xs)
    else:
        print(0)


