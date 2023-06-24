"""
Xâu ký tự S được tạo ra bằng cách bổ sung dần các ký tự chữ cái Tiếng Anh in hoa như sau.

Bước 1: Chỉ có chữ cái A
Bước 2: Thêm chữ cái B vào giữa 2 chữ A => S = "ABA"
Bước 3: Thêm chữ cái C vào giữa 2 xâu đã có ở bước 2: S = "ABACABA"
Cứ như vậy cho đến bước thứ N (0 < N < 26)

Hãy xác định ký tự thứ K trong bước biến đổi thứ N là chữ cái gì?

Input:

Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm số nguyên dương N và K (1 ≤ N ≤ 25, 1 ≤ K ≤ 2N - 1).
Input:
2
3 2
4 8
Output:
B
D
"""
if __name__ == "__main__":
    for i in range(int(input())):
        n, k = map(int, input().split())
        x = 65
        s = chr(x)
        if k == 1:
            print(s)
        else:
            while n > 1:
                x += 1
                s = s + chr(x) + s
                n -= 1
            print(s[k - 1])
