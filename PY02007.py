"""
Cho dãy số A có 10 phần tử là các số nguyên dương.
Hãy đếm xem sẽ có bao nhiêu số khác nhau trong dãy nếu tất cả các phần tử đều được chia dư cho 42.
Input:
1 2 3 4 5 6  7 8  9 10
Out: 10

42 84 252 420 840
126 42 84 420 126
Out: 1

39 40 41 42 43 44 82
83 84 85
Out: 6
"""

if __name__ == "__main__":
    t = 10
    a = []
    while t != 0:
        n = input().split()
        for x in n: a.append(int(x))
        t -= len(n)
    print(len(set(list(map(lambda x : x % 42, a)))))