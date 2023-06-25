"""
Trong thơ ca có rất nhiều các thể thơ và những cách gieo vần khác nhau cho các bài thơ. Trong số những thể thơ đó, bạn có thể lựa chọn cho mình một loại thể thơ riêng để đem lại nhiều hiệu quả cho bài thơ và giúp cho bạn có thể thấy được sự hiệu quả trong cách truyền đạt những cung bậc cảm xúc vào trong bài thơ.

Cho danh sách các bài thơ gồm hai thể loại thơ lục bát và thơ thất ngôn tứ tuyệt.

1. Thơ lục bát

- Là thể thơ dân tộc.

- Số chữ và số câu: Một cặp hai câu thơ, câu trên sáu chữ (lục), câu dưới tám chữ (bát). Một bài thơ có thể có nhiều cặp lục bát, số lượng cặp câu không hạn định.

2. Thơ thất ngôn tứ tuyệt

- Xuất xứ: Trung Quốc

- Thơ trung đại, thơ cận đại

- Là bài thơ mà mỗi dòng 7 tiếng, bài có 4 câu (Khai - Thừa - Chuyển - Hợp)

Nhiệm vụ của bạn là hãy viết chương trình xác định số lượng bài thơ và thể thơ (ghi bằng số) của từng bài từ danh sách các bài thơ có sẵn.
In ra kết quả số bài thơ và số tương ứng với thể thơ theo từng dòng.

Input:
8
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Output:
2
1
2
"""
if __name__ == "__main__":
    n = int(input())
    dem = 0
    b = []
    for i in range(n):
        s = [str(x) for x in input().split()]
        l = (len(s))
        if l == 6: b.append(1)
        if l == 7: b.append(2)
    c = []
    l = len(b)
    # print(b)
    i = 0
    while i < l - 1:
        if (b[i] == 1 and b[i + 1] != 1):
            c.append(1)
            i += 1
        elif b[i] == 2:
            c.append(2)
            i += 4
        else:
            i += 1
    if b[l - 1] == 1: c.append(1)
    print(len(c))
    for i in c: print(i)