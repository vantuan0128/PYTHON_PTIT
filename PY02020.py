"""
Sau khi xem Olympic Tokyo 2020, Nam nhận thấy ở một số nội dung thi có chấm điểm thì điểm được tính cho vận động viên sẽ bỏ qua các giá trị điểm thấp nhất và cao nhất sau đó mới tính trung bình.
Nam mở rộng bài toán như sau: Có N giám khảo, mỗi giám khảo cho một giá trị điểm là một số thực trong đoạn từ 0 đến 10
. Hãy loại bỏ các giá trị điểm bằng với điểm thấp nhất hoặc cao nhất, sau đó in ra điểm trung bình của các giá trị còn lại.
Dữ liệu vào của bài toán đảm bảo luôn có ít nhất 3 giá trị khác nhau trong các giá trị điểm ban đầu.
Input:
6
6.75 8 9.2 7.25 7.75 6.75
Output:
7.67
"""

if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    sum, cnt, mi, ma = 0, 0, min(a), max(a)
    for i in a:
        if i != mi and i != ma:
            sum += i
            cnt += 1
    print(round(sum / cnt, 2))
