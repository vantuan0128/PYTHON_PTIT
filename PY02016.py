"""
Cho dãy số A[] gồm có N phần tử.
Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.
Với mỗi test in ra đáp án của bài toán trên một dòng. Nếu có nhiều số cùng có tần số xuất hiện nhiều nhất như nhau
và đều thỏa mãn số lần lớn hơn N/2 thì in ra số nhỏ nhất.
Nếu không tìm được đáp án, in ra “NO”.
Input:
2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4
Output:
4
NO
"""
def func():
    m = {}
    n = int(input())
    s = [int(x) for x in input().split()]
    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    max = 0
    j = 0
    for i in m:
        if m[i] > max:
            max = m[i]
            j = i
    if max > n / 2:
        print(j)
    else:
        print("NO")


for i in range(int(input())): func()