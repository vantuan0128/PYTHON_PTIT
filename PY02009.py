"""
Chung kết Euro 2020, quá nhiều người dự đoán đúng Italia thắng Anh bằng đá luân lưu 11m. Ban tổ chức chương trình
Dự đoán tỉ số trúng Mercedes thấy rất khó trao giải nên quyết định tìm người được trao thưởng bằng cách chạy đoạn code lựa chọn ngẫu nhiên.

Các người chơi dự đoán đúng được đánh số thứ tự bắt đầu từ 1, giả sử cũng có không quá 1000 người. Chương trình sẽ
thực hiện lấy ngẫu nhiên N lần, mỗi lần 1 giá trị từ 1 đến 1000, N cũng không quá 1000.

Sau khi kết thúc N lần ngẫu nhiên, con số nào được chọn nhiều lần nhất sẽ cho biết người trúng thưởng.
Trong trường hợp có nhiều số có số lần xuất hiện bằng nhau và lớn nhất thì số có giá trị nhỏ nhất sẽ được chọn.

Hãy giúp BTC tìm ra người được trao thưởng.
Input:
3
3
999
999
19
4
13
333
333
13
3
11
12
13
Output:
999
13
11
"""
if __name__ == "__main__":
    n=int(input())
    while n>0:
        t=int(input())
        a=[]
        for i in range(t):
            a.append(int(input()))
        max=0
        x=0
        a.sort()
        for i in range(t):
            sum=a.count(a[i])
            if sum>max:
                max=sum
                x=a[i]
        print(x)
        n-=1