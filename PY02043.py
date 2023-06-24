"""
Cho một ký tự S[] chỉ có các chữ số, độ dài không quá 1000, và số nguyên dương N (không quá 9 chữ số). Hãy đếm xem số N xuất hiện bao nhiêu lần trong S[].

Chú ý: các ký tự số không được đếm lặp. Tức là mỗi ký tự chỉ được xét một lần.

Ví dụ: S[] = “1212121112211221121”, N = 121 thì đáp án là 3.
Input:
2
1212121112211221121
121
2222222222322292
2222
Output:
3
2
"""
def func():
    s=input()
    x=input()
    print(s.count(x))
for i in range(int(input())): func()