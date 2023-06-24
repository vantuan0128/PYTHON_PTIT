"""
Cho một đoạn văn bản có N dòng trong đó có thể có các dấu câu như dẩy phẩy (,) dấu chấm (.) dấu chấm hỏi (?) dấu chấm cảm (!) dấu hai chấm (:) dấu chấm phẩy (;) dấu ngoặc đơn, dấu gạch ngang (-), dấu gạch chéo (/).

Hãy liệt kê các từ khác nhau xuất hiện trong đoạn văn bản theo thứ tự số lần xuất hiện giảm dần.

Chú ý:

Khi thống kê thì không phân biệt chữ hoa, chữ thường.
Bỏ qua các dấu câu đã liệt kê ở trên khi tách từ
Tất cả các chữ số không được xem xét khi đếm. Nếu trong một từ có chữ số thì các chữ số đó cũng sẽ bị bỏ qua.
Ghi ra danh sách các từ (ở dạng in thường) theo thứ tự số lần xuất hiện giảm dần.

Trong trường hợp số lần xuất hiện bằng nhau thì liệt kê theo thứ tự từ điển tăng dần.
Input:
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
Output:
ptit 4
dong 2
ho 2
nam 2
sinh 2
tro 2
va 2
vien 2
benh 1
dich 1
dinh 1
duy 1
hien 1
hoc 1
hon 1
khi 1
khong 1
muc 1
on 1
phi 1
tang 1
tri 1
trich 1
trong 1
ty 1
voi 1
xuat 1
"""
if __name__ == "__main__":
    n = int(input())
    m = {}
    for i in range(n):
        s = input().lower() + ' '
        x = ''
        for i in s:
            if (i >= 'a' and i <= 'z'):
                x += i
            else:
                if x != '':
                    if x in m:
                        m[x] += 1
                    else:
                        m[x] = 1
                    x = ''
    m = sorted(m.items(), key=lambda x: (-x[1], x[0]))
    for i in m:
        print(i[0], i[1])