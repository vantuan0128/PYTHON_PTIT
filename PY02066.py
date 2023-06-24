"""
Ngày thi chung kết ICPC PTIT 2020, các lập trình viên đang say sưa đọc đề và fix bug trong Hội trường 1, nhưng từ Ký túc xá thì nhóm bạn nữ xinh đẹp nào đó liên tục đồng thanh lặp đi lại lại câu hát quen thuộc:

“1, 2, 3, 5 anh có đánh rơi nhịp nào không?

Nếu câu trả lời là có …”

Để cho phù hợp với tình hình thời sự và giảm bớt căng thẳng cho các bạn thí sinh, ban tổ chức quyết định thêm một bài toán đơn giản: cho một dãy các số nguyên đếm tăng dần. Hỏi có số nào bị “đánh rơi” khi đếm hay không? Giả sử một dãy đếm chính xác thì luôn luôn đếm bắt đầu từ 1.
Nếu phép đếm là đầy đủ, chính xác thì ghi ra Excellent!
Hoặc lần lượt liệt kê các số bị đánh rơi, mỗi số trên một dòng.
Input:
4
1 2 3 5
-> 4

7
4 5 7 8 9
10 11
-> 1
2
3
6

5
1 2 3
4
5
-> Excellent!
"""
if __name__ == "__main__":
    n = int(input())
    s = []
    while (n > 0):
        a = [int(x) for x in input().split()]
        for i in a: s.append(i)
        n = n - len(a)
    a = min(s)
    b = max(s)
    dem = 0
    for i in range(1, b + 1):
        if i not in s:
            print(i)
            dem += 1
    if dem == 0:
        print("Excellent!")