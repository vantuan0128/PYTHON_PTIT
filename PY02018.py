"""
Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau. Hãy tìm số nhỏ nhất còn thiếu trong dãy số đó.
(khi dãy số đầy đủ các số từ 1 đến N thì số nhỏ nhất còn thiếu sẽ là N+1).
Input:
3
1 2 4
Output:
3
"""
if __name__ == "__main__":
    n=input()
    s=[ int(x) for x in input().split()]
    print(min([i for i in range(1,max(s)+2) if i not in s]))
