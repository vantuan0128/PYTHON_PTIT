"""
Cho một số nguyên dương không quá 200 chữ số. Mỗi bước tách số nguyên thành hai nửa: nửa đầu là n/2 chữ số đầu tiên, nửa sau là phần còn lại (trong đó n là số chữ số của số ban đầu, nếu n lẻ thì phép chia 2 sẽ tính phần nguyên). Sau đó thực hiện tính tổng của hai nửa này.

Lặp lại các bước trên cho đến khi kết quả chỉ còn là số có 1 chữ số.

Hãy thực hiện tính toán và in kết quả của từng bước.
Input:
123456
Output:
579
84
12
3
"""
s = input()
while len(s)>1:
    s = str(int(s[:int(len(s) / 2):]) + int(s[int(len(s) / 2)::]))
    print(s)
