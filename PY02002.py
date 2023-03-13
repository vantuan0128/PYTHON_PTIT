"""
Dãy số Fibonacci được định nghĩa theo công thức như sau:
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 với n>2
Cho hai số nguyên dương a và b (1 < a < b < 93).
Viết chương trình liệt kê các số Fibonacci từ a đến b.
Input:
1
1 10
Output:
1 1 2 3 5 8 13 21 34 55
"""

f = [0] * 95

def fibo():
    f[1] = 1
    f[2] = 1
    for i in range (3,95,1):
        f[i] = f[i-1] + f[i-2]

if __name__ == "__main__":
    fibo()
    for _ in range(int(input())):
        a , b = map(int,input().split())
        for i in range (a,b + 1):
            print(f[i],end = ' ')
        print()