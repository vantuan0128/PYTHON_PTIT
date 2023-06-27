"""
Cho danh  sách chủ đề và bộ câu hỏi đi kèm theo chủ đề đó trong một bộ đề bài Tiếng Anh.

Mỗi bộ câu hỏi theo chủ đề sẽ cách nhau một dòng trống. Mỗi câu hỏi được viết trên một dòng.

Ghi ra thống kê số lượng câu hỏi theo từng chủ đề. Thứ tự của chủ đề ở kết quả được giữ nguyên với thứ tự xuất hiện trong dữ liệu vào.
Input:
9
Home/accommodatio
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?

Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?

Output:
Home/accommodation: 3
Study: 3
"""
if __name__ == "__main__":
    n=int(input())
    a=[]
    for i in range(n):
        s=input()
        a.append(s)
        if s=='':
            print(a[0]+': '+str(len(a)-2))
            a.clear()
    print(a[0]+': '+str(len(a)-1))
