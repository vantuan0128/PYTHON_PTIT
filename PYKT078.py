"""
Cho dãy số nguyên x1 , x2 , … ,x  và số nguyên m

- Tìm giá trị lớn nhất của dãy số.

- Chèn m vào trước vị trí đầu tiên có giá trị bằng giá trị lớn nhất.

- Sắp xếp lại dãy số sau chèn sao cho phần tử âm về đầu dãy, phần tử dương và bằng 0 về cuối dãy sao cho trật tự các phần tử không thay đổi.
Input:
1
5 3
-1 2 3 4 -1
Output:
-1 -1 2 3 3 4

"""
if __name__ == "__main__":
    for u in range(int(input())):
        b,c=[],[]
        n,m=[int(x) for x in input().split()]
        a=[int(x) for x in input().split()]
        for i in range(len(a)):
            if a[i]==max(a):
                j=i
                break
        a.insert(j,m)
        for i in range(len(a)):
            if a[i]<0:
                b.append(a[i])
            else: c.append(a[i])

        d=b+c
        print(*d)