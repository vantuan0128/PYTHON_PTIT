"""
Cho xâu ký tự S bao gồm các ký tự ‘A’,..,’Z’ và các chữ số ‘0’,...,’9’. Nhiệm vụ của bạn in các ký tự từ ’A’,.., ‘Z’ trong S theo thứ tự từ điển và nối với tổng các chữ số trong S ở cuối cùng.
Ví dụ S =”ACCBA10D2EW30” ta nhận được kết quả: “AABCCDEW6”.
Input:
2
AC2BEW3
ACCBA10D2EW30
Output:
ABCEW5
AABCCDEW6
"""

if __name__ == "__main__":
     t = int(input())
     for _ in range(t):
         s = input()
         s = sorted(s)
         t = ""
         sum = 0
         for x in range(0,len(s)):
             if s[x].isalpha(): t += s[x]
             else: sum += int(s[x])
         t += str(sum)
         print(t)
