"""
Cho hai xâu ký tự A và B mô tả hai số nguyên dương lớn có thể có đến 1000 chữ số.

Có thể có các chữ số 0 ở đầu của A và B.
Hãy tính A - B.

Kết quả có thể âm, khi ghi ra cần loại bỏ các chữ số 0 ở đầu nếu có.

Tất nhiên nếu kết quả là -0 thì ghi ra là 0.
Input:
000123456789012345678901234567890
00000000000000001234567890
Output:
123456789012345678900000000000
"""
a = int(input())
b = int(input())
print(a-b)