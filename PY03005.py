"""
Cho một đoạn văn bản có N dòng trong đó có thể có các dấu câu như dẩy phẩy (,) dấu chấm (.) dấu chấm hỏi (?) dấu chấm cảm (!) dấu hai chấm (:) dấu chấm phẩy (;) dấu ngoặc đơn, dấu gạch ngang (-), dấu gạch chéo (/).

Nhập thêm số nguyên dương K (1 < K < 50). Hãy liệt kê các từ khác nhau xuất hiện ít nhất K lần trong đoạn văn bản. Danh sách được sắp xếp theo thứ tự số lần xuất hiện giảm dần, nếu số lần xuất hiện bằng nhau thì sắp xếp theo thứ tự từ điển tăng dần.

Chú ý:

Khi thống kê thì không phân biệt chữ hoa, chữ thường.
Bỏ qua các dấu câu đã liệt kê ở trên khi tách từ
Ghi ra danh sách các từ (ở dạng in thường) xuất hiện ít nhất K lần trong dữ liệu vào. Danh sách được sắp xếp theo thứ tự số lần xuất hiện giảm dần. Trong trường hợp số lần xuất hiện bằng nhau thì liệt kê theo thứ tự từ điển tăng dần.
Input:
3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
Output:
ptit 4
2021 2
dong 2
ho 2
nam 2
sinh 2
tro 2
va 2
vien 2
"""
if __name__ == "__main__":
    n, k = map(int, input().split())
    m = {}
    for i in range(n):
        s = input().lower() + ' '
        x = ''
        for i in s:
            if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
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
        if i[1] >= k:
            print(i[0], i[1])