"""
Thang điểm IELTS được tính từ 1.0 – 9.0 IELTS (Overall điểm thi IELTS được tính trung bình cộng điểm 4 kỹ năng Reading, Listening, Speaking và Writing).

4 kỹ năng của IELTS cũng tính từ 1.0-9.0 để sau đó tính điểm thi IELTS Overall.

Cả 2 phần thi nghe (Listening) và đọc (Reading) đều có 40 câu hỏi thí sinh cần trả lời. Với một câu trả lời đúng sẽ được 1 điểm, tối đa là 40 điểm và quy đổi sang thang điểm 1.0 – 9.0 dựa trên tổng số câu trả lời đúng.

Dưới đây là bảng điểm quy đổi sẽ giúp cho các bạn hiểu hơn về cách chuyển đổi điểm cho từng phần thi Reading và Listening.
39-40 -> 9.0
37-38 -> 8.5
35-36 -> 8.0
33-34 -> 7.5
30-32 -> 7.0
27-29 -> 6.5
23-26 -> 6.0
20-22 -> 5.5
16-19 -> 5.0
13-15 -> 4.5
10-12 -> 4.0
7-9 -> 3.5
5-6 -> 3.0
3-4 -> 2.5
Thang điểm IELTS trên bảng kết quả của thí sinh sẽ thể hiện điểm của từng kỹ năng thi cùng với điểm overall. Phần điểm tổng sẽ được tính dựa trên điểm trung bình cộng của 4 kỹ năng.



Điểm tổng của 4 kỹ năng sẽ được làm tròn số theo quy ước chung như sau: Nếu điểm trung bình cộng của 4 kỹ năng có số lẻ là .25, thì sẽ được làm tròn lên thành .5, còn nếu là .75 sẽ được làm tròn thành 1.0.

Một trung tâm tổ chức thi thử Tiếng Anh cho các học viên. Hãy giúp trung tâm tính điểm overall dựa trên kết quả bài làm của thí sinh nhé.

Input:

Dòng đầu cho số T là số lượng thí sinh

T dòng tiếp theo mỗi dòng cho 4 số là số câu đúng lần lượt của kỹ năng Reading, Listening, điểm kỹ năng speaking, và điểm kỹ năng writing.

Output:

In ra kết quả theo từng dòng.
Input:
2
15 25 5.0 5.5
22 32 6.0 6.0
Output:
5.5
6.0
"""

if __name__ == "__main__":
    for i in range(int(input())):
        read1, read11 = 0, 0
        read, lis, speak, write = [float(x) for x in input().split()]
        if read >= 3 and read <= 4:
            read1 = 2.5
        elif read >= 5 and read <= 6:
            read1 = 3.0
        elif read >= 7 and read <= 9:
            read1 = 3.5
        elif read >= 10 and read <= 12:
            read1 = 4.0
        elif read >= 13 and read <= 15:
            read1 = 4.5
        elif read >= 16 and read <= 19:
            read1 = 5.0
        elif read >= 20 and read <= 22:
            read1 = 5.5
        elif read >= 23 and read <= 26:
            read1 = 6.0
        elif read >= 27 and read <= 29:
            read1 = 6.5
        elif read >= 30 and read <= 32:
            read1 = 7.0
        elif read >= 33 and read <= 34:
            read1 = 7.5
        elif read >= 35 and read <= 36:
            read1 = 8.0
        elif read >= 37 and read <= 38:
            read1 = 8.5
        elif read >= 39 and read <= 40:
            read1 = 9.

        if lis >= 3 and lis <= 4:
            read11 = 2.5
        elif lis >= 5 and lis <= 6:
            read11 = 3.0
        elif lis >= 7 and lis <= 9:
            read11 = 3.5
        elif lis >= 10 and lis <= 12:
            read11 = 4.0
        elif lis >= 13 and lis <= 15:
            read11 = 4.5
        elif lis >= 16 and lis <= 19:
            read11 = 5.0
        elif lis >= 20 and lis <= 22:
            read11 = 5.5
        elif lis >= 23 and lis <= 26:
            read11 = 6.0
        elif lis >= 27 and lis <= 29:
            read11 = 6.5
        elif lis >= 30 and lis <= 32:
            read11 = 7.0
        elif lis >= 33 and lis <= 34:
            read11 = 7.5
        elif lis >= 35 and lis <= 36:
            read11 = 8.0
        elif lis >= 37 and lis <= 38:
            read11 = 8.5
        elif lis >= 39 and lis <= 40:
            read11 = 9.0

        sum = (read1 + read11 + speak + write) / 4
        if sum - int(sum) >= 0.75:
            print(int(sum) + 1.0)
        elif sum - int(sum) >= 0.25:
            print(int(sum) + 0.5)
        else:
            print(int(sum) + 0.0)