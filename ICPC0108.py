"""
Cho mảng A[] gồm N số nguyên khác nhau. Nhiệm vụ của bạn là đếm số lượng các bộ ba phần tử khác nhau có tổng là 0. Ví dụ
A[] = {0, -1, 2, -3, 1}, ta nhận được kết quả là 2 vì có hai bộ 3: (0, -1, 1) và (2, -3, 1).
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A[]; dòng tiếp theo đưa vào các phần tử A[i] của mảng A[].
T, N, A[i] thỏa mãn ràng buộc : 1 ≤ T ≤ 100; 1 ≤ N ≤ 10^3; -10^9≤ A[i] ≤10^9;
Input:
2
5
0 -1 2 -3 1
5
1 -2  1  0  5
Output:
2
1
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        a.sort()
        cnt = 0
        for i in range(0,n-2,1):
            left = i + 1
            right = n - 1
            tmp = 0
            while left < right:
                tmp = a[i] + a[left] + a[right]
                if tmp == 0:
                    cnt += 1
                    left += 1
                elif tmp < 0: left += 1
                else: right -= 1
        print(cnt)