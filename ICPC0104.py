"""
Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu.
Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.
Input:
2
12ab29cd19
ab123gh456cd
Output:
12
123
"""
import re
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        # s = input()
        # a = []
        # num=0
        # for x in range(0,len(s)):
        #     if s[x].isdigit():
        #         num = num*10 +int(s[x])
        #     elif(s[x].isalpha() and num != 0):
        #         a.append(num)
        #         num = 0
        # if num != 0: a.append(num)
        # print(min(a))

        s = input()
        a = ((re.findall('\d+', s)))
        s = []
        for i in range(len(a)):
            s.append(int(a[i]))
        if s == []:
            print()
        else:
            print(min(s))


