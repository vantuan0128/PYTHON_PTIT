"""
Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.
Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân có chữ số đầu và chữ số cuối giống nhau không?
1≤n≤10^100
Ứng với mỗi số nguyên dương n, ghi ra trên một dòng là YES nếu số n tương ứng có chữ số đầu và chữ số cuối giống nhau, NO nếu ngược lại.
Input:
2
12345
123451
Output:
NO
YES
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        if s[0] != s[-1]: print("NO")
        else: print("YES")