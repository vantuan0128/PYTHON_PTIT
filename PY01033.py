"""
Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1.
Một bộ ba số (a, b, c) được gọi là bộ ba nguyên tố cùng nhau
nếu a < b < c và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.
Cho hai số nguyên dương L và R (10 < L < R < 200).
Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn [L, R].
Input: 15 20
Output:
(15, 16, 17)
(15, 16, 19)
(15, 17, 19)
(16, 17, 19)
(17, 18, 19)
(17, 19, 20)
"""
import math

def func(l,r):
    for i in range(l,r-1,1):
        for j in range (i+1,r,1):
            for k in range(j+1,r+1,1):
                if math.gcd(i,j) == 1 and math.gcd(j,k) == 1 and math.gcd(i,k) == 1:
                    print(f"({i}, {j}, {k})",end="\n")


if __name__ == "__main__":
     l,r = map(int,input().split())
     func(l,r)