"""
Trong lập trình cơ bản, một từ được hiểu là một dãy ký tự liên tiếp không chứa khoảng trống, dấu tab hoặc dấu xuống dòng.

Viết chương trình nhập hai dòng ký tự và hiển thị hợp và giao của hai tập từ tương ứng.
Các từ trong tập từ không được phép trùng nhau, mỗi từ chỉ liệt kê một lần và theo đúng thứ tự từ điển. Các từ đều được chuyển hết về chữ viết thường.
Input:
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
Output:
c++ doi huong lap ngon ngu trinh tuong
lap trinh
"""
if __name__ == "__main__":
    s1 = input()
    s1 = s1.lower()
    words1 = [word for word in s1.split(" ")]
    s2 = input()
    s2 = s2.lower()
    words2 = [word for word in s2.split(" ")]

    print(" ".join(sorted(set(words1) | set(words2))))
    print(" ".join(sorted(set(words1) & set(words2))))