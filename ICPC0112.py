"""
Bộ ba số nguyên tố được gọi là Prime- Triplet nếu nó là bộ ba số nguyên tố dưới dạng (p, p +2, p + 6) hoặc (p, p + 4, p+6),
 trong đó p là một số nguyên tố. Ví dụ các bộ ba số (5, 7, 11) hoặc (7, 11, 13) đều là các Prime-Triplet.
Cho số tự nhiên N, nhiệm vụ của bạn là đếm số các Prime-Triplet nhỏ hơn N.
Input:
2
15
25
Output:
2
5
"""

import math
def nto(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

if __name__ == "__main__":
    t=int(input())
    while t>0:
        n=int(input())
        dem=0
        for i in range(5,n-5,2):
            if nto(i) and nto(i+2) and nto(i+6):
                dem+=1
            elif nto(i) and nto(i+4) and nto(i+6):
                dem+=1
        print(dem)
        t-=1