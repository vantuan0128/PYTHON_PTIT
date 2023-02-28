"""
Một số nguyên dương được gọi là đẹp nếu số đó chỉ có hai chữ số khác nhau
và các chữ số ở cách nhau 2 vị trí đều bằng nhau. Ví dụ: 121, 1313131, 5656 …
Viết chương trình kiểm tra một số có phải số đẹp hay không?
Input:
3
12121212
343433
78789989
Output:
YES
NO
NO
"""

def check(n):
    for i in range(0,len(n)-2):
        if n[i] != n[i+2]: return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if check(n): print("YES")
        else: print("NO")