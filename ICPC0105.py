"""
Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9.
Nhiệm vụ của bạn là tìm số lớn nhất xuất hiện trong xâu.
Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 29.
Input:
2
12ab29cd19
ab123gh456cd
Output:
29
456
"""

import re

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        num = 0
        a = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i].isalpha() and num != 0:
                a.append(num)
                num = 0
        if num != 0: a.append(num)
        print(max(a))

        # s = input()
        # a = re.findall('\d+',s);
        # s = []
        # for i in range(len(a)):
        #     s.append(int(a[i]))
        # if len(s) == 0:
        #     print()
        # else: print(max(s))