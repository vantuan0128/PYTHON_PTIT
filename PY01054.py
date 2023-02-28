"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy tính tích các chữ số của N. Chú ý bỏ qua các chữ số 0 nếu có.
Input:
2
123410
123456789123456789
Output:
24
131681894400
"""

s = ""

def func():
    tich = 1
    s = input()
    for i in s:
        if i != '0': tich *= int(i)
    print(tich)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        func()