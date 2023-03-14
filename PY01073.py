"""
Cho xâu ký tự S có không quá 9 ký tự chữ cái in hoa, không có khoảng trống.
Các ký tự khác nhau từng đôi một và đã được sắp xếp từ trái sang phải theo thứ tự từ
điển. Hãy liệt kê tất cả các hoán vị của xâu ký tự S theo đúng thứ tự từ điển,
mỗi hoán vị trên một dòng.
Input: XYZ
Output:
XYZ
XZY
YXZ
YZX
ZXY
ZYX
"""
from itertools import permutations

if __name__ == "__main__":
    s =input()
    a = permutations(s)
    for i in a:
        for j in i:
            print(j,end="")
        print()


