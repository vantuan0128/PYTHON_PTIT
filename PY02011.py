"""
Cho dãy số A[] có N phần tử là các số nguyên dương.

Mỗi bước bạn được phép thay đổi 1 giá trị trong dãy bằng cách tăng lên 1 hoặc giảm đi 1.

Hãy tính xem cần ít nhất bao nhiêu bước để biến đổi dãy về giá trị bằng nhau, với điều kiện giá trị của dãy bằng nhau đó phải là một trong các giá trị ban đầu của dãy.
Ghi ra tổng số bước ít nhất tìm được và giá trị bằng nhau được chọn.

Trong trường hợp có nhiều giá trị có thể chọn thì chọn số đầu tiên theo thứ tự xuất hiện trong dãy ban đầu.
Input:
8
13 5 8 7 9 15 26 34
Output: 59 13
"""
if __name__ == "__main__":
    n = int(input())
    s = [int(x) for x in input().split()]
    max = 10**9
    k = 0
    for i in s:
        res = 0
        for j in s:
            res += abs(i-j)
        if res < max:
            max = res
            k = i
    print(max,k)