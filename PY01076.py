"""
Cho hai số a và b trong đó a≤10^12, b≤10^250.
Nhiệm vụ của bạn là tìm ước số chung lớn nhất của hai số a, b.
Input:
1
1221
1234567891011121314151617181920212223242526272829
Output:
3
"""
import math

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        print(math.gcd(a,b))