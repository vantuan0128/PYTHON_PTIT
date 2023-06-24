"""
Ai cũng biết số lộc phát theo quan niệm người Việt là số chỉ chứa các chữ số 6 và/hoặc 8.
Người ta định nghĩa thêm “số lộc phát đẹp” là số thỏa mãn tính chất nếu xét từ trái qua phải thì nó được ghép bởi 3 số: 6; 68; 688. Không nhất thiết phải dùng đủ cả 3 số này.

Ví dụ: các số 666666; 668688; 688688688 là các số lộc phát đẹp.

Cho trước một số nguyên dương N không quá 100 chữ số. Hãy kiểm tra xem đó có phải là số lộc phát đẹp hay không.
Input:
666666 -> YES
668688 -> YES
886236 -> NO
"""

if __name__ == "__main__":
    s = input()
    if len(s) == 0:
        print("NO")
    else:
        while 1:
            m = s.find('688')
            s = s.replace('688', '111')
            if m == -1: break
        while 1:
            m = s.find('68')
            s = s.replace('68', '11')
            if m == -1: break
        while 1:
            m = s.find('6')
            s = s.replace('6', '1')
            if m == -1: break
        str = ''
        for i in range(len(s)): str += '1'

        if s == str:
            print("YES")
        else:
            print("NO")