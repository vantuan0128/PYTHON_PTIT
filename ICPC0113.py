"""
Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố, đảo các chữ số của K cũng là
một số nguyên tố nhưng không phải chính nó (không đối xứng). Ví dụ số 11 không phải là số Emirp Number.
Cho số tự nhiên N, nhiệm vụ của bạn là hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.
Input:
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤10^6;
2
40
100
Output:
13  31
13  31  17  71  37 73 79  97
"""
from math import isqrt

a = [1] * 1000001

def sieve():
    a[0] = a[1] = 0
    for i in range (2, isqrt(1000000)+1):
        if a[i] == 1:
            for j in range(i * i, 1000001, i): a[j] = 0

if __name__ == "__main__":
    t = int(input())
    sieve()
    for _ in range(t):
        n = int(input())
        sto = []
        for i in range(13,n,2):
            m = int(str(i)[::-1])
            if m < n and a[i] == 1 and a[m] == 1 and i != m and i not in sto:
                sto.append(i)
                sto.append(m)
        for x in sto: print(x,end = ' ')
        print()