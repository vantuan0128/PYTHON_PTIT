"""
Cho dãy số A gồm N phần tử là các số nguyên. Hãy tính tích lớn nhất của 2 hoặc 3 phần tử trong dãy.
Input:
6
5 10 -2 3 5 2
Output:
250
"""
if __name__ == "__main__":
    n = int(input())
    s = [int(x) for x in input().split()]
    s.sort()
    l = len(s)
    s1 = s[0]*s[1]
    s2 = s[l-3]*s[l-1]*s[l-2]
    s3 = s[l-1]*s[l-2]
    s4 = s[l-1]*s[0]*s[1]
    print(max(s1,s2,s3,s4))
