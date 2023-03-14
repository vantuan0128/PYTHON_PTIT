"""
Cho dãy số A[] có N phần tử. Hãy liệt kê tất cả các tổ hợp chập K của tập các phần tử khác nhau trong A[].
Các tổ hợp cần liệt kê theo thứ tự từ điển (tức là trong mỗi tổ hợp thì giá trị từ nhỏ đến lớn,
và tổ hợp sau lớn hơn tổ hợp trước).
Dòng đầu ghi hai số N và K.
Dòng thứ 2 ghi N số của mảng A[]. Các giá trị không quá 1000.
Dữ liệu đảm bảo số phần tử khác nhau của A[] không quá 20 và K không quá 10.
Input:
8 3
2 4 4 3 5 1 3 4
Output:
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
"""
from itertools import combinations

if __name__ == "__main__":
    n,k = map(int,input().split())
    a = sorted(list(set(list(map(int, input().split())))))
    ds = list(combinations(a,k))
    for i in ds:
        for j in i:
            print(j,end=' ')
        print()