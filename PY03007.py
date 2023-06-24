"""
Cho dữ liệu vào là luồng văn bản bất kỳ, gồm các ký tự viết hoa, viết thường, các ký tự số và các dấu câu, không có các ký tự đặc biệt khác.
Người ta muốn tách văn bản thành các câu. Mỗi câu in trên một dòng.
Một câu được định nghĩa là dãy ký tự có ít nhất 1 ký tự chữ cái hoặc chữ số, không chứa các dấu ngắt câu gồm:
dấu chấm (.), dấu chấm hỏi (?) và dấu chấm cảm (!). Dấu phẩy (,) và dấu hai chấm (:) không được coi là dấu ngắt câu.
Nhiệm vụ của bạn là in ra mỗi câu trên một dòng, ký tự đầu câu viết hoa, các ký tự khác viết thường, các từ cách nhau đúng một khoảng trống.
Không có khoảng trống ở đầu và cuối câu, và không in ra các dấu ngắt câu.
Dữ liệu vào
Gồm một luồng văn bản không quá 100 dòng, mỗi dòng không quá 200 ký tự.
Kết quả
In ra các câu, mỗi câu trên một dòng theo quy tắc đã cho.
Input:
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!

    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
Output:
Ky thi lap trinh icpc ptit bat dau to chuc tu nam 2010
Nhu vay, nam nay la tron 10 nam
Vay co phai nam nay la ky thi lan thu 10
Khong phai

Nam nay la ky thi lan thu 11
"""

import re

if __name__ == "__main__":
    s = ""
    regex = '[\w\s,:]+'
    while True:
        try : s += input()
        except EOFError : break
    s = re.findall(regex, s)
    for i in s:
        x = i.lower().split()
        x[0] = x[0].title()
        print(' '.join(x))