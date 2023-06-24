"""
Cho dãy số a[] có n phần tử và dãy số b[] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a[], tập hợp B là tập các số khác nhau trong b[].

Tập A và tập B được coi là bằng nhau nếu số phần tử bằng nhau và tất cả các giá trị số từ nhỏ đến lớn đều bằng nhau từng đôi một. Khi A = B ta cũng có thể kết luận là hai dãy a[] và b[] chứa các số giống nhau.

Hãy kiểm tra xem A có bằng B hay không?
Input:
12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
Output:
YES
"""
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    x = set()
    y = set()
    z = set()
    for i in a:
        x.add(i)
    for i in b:
        y.add(i)
    if x == y:
        print("YES")
    else:
        print("NO")