"""
Cho xâu ký tự S bao gồm các ký tự ‘A’,..,’Z’ và các chữ số ‘0’,...,’9’. Nhiệm vụ của bạn in các ký tự từ ’A’,.., ‘Z’ trong S theo thứ tự từ điển và nối với tổng các chữ số trong S ở cuối cùng. Ví dụ S =”ACCBA10D2EW30” ta nhận được kết quả: “AABCCDEW6”.
Input:
Dòng đầu tiên đưa vào số lượng bộ test T.
Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test là một xâu ký tự S.
T, S thỏa mãn ràng buộc: 1≤ T ≤100; 1≤ Length(S)≤105.
Output:

Đưa ra kết quả mỗi test theo từng dòng.
Input:
2
AC2BEW3
ACCBA10D2EW30
Output:
ABCEW5
AABCCDEW6
"""

if __name__ == "__main__":
    def func():
        str = input()
        s = (sorted(str))
        sum = 0
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                sum += int(s[i])
            else:
                print(s[i], end='')
        print(sum)


    for i in range(int(input())):
        func()