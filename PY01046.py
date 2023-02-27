"""
Bài toán Tháp Hà Nội đã rất nổi tiểng.
Bắt đầu có các đĩa xếp chồng lên cột A theo thứ tự kích thước giảm dần,
nhỏ nhất ở trên cùng. Cột B và cột C ban đầu không có đĩa nào cả.
Mục tiêu của bạn là di chuyển toàn bộ các đĩa theo đúng thứ tự về cột C,
tuân theo các quy tắc sau:
Mỗi lần chỉ có thể di chuyển một đĩa.
Mỗi lần di chuyển sẽ lấy đĩa trên từ một trong các cột
và đặt nó lên trên một cột khác.
Không được đặt đĩa lên trên đĩa nhỏ hơn..
"""
def ThapHaNoi(n,a,b,c):
    if n == 1: print(f"{a} -> {c}")
    else:
        ThapHaNoi(n-1,a,c,b)
        print(f"{a} -> {c}")
        ThapHaNoi(n-1,b,a,c)

n = int(input())
ThapHaNoi(n,'A','B','C')