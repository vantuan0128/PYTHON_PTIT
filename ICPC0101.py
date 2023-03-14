"""
Cho dãy số A[] chỉ bao gồm các số nguyên dương.
Người ta thu gọn dần dãy số bằng cách loại bỏ các cặp phần tử kề nhau mà có tổng là chẵn. Sau khi cặp phần tử đó bị loại ra thì dãy số được dồn lại.
Cứ tiếp tục như vậy cho đến khi không còn cặp phần tử nào kề nhau có tổng chẵn nữa.
Hãy tính xem cuối cùng dãy A[] còn bao nhiêu phần tử.
Input1:
5
2 3 4 5 6
Output1: 5
Input2:
10
1 5 5 8 6 4 3 5 9 3
Output2: 2
"""
if __name__ == "__main__":
    n = int(input())
    if n == 1:
        print(1)
    else:
        a = []
        for i in input().split():
            if len(a) == 0:
                a.append(int(i))
            elif (a[-1]+int(i)) % 2 == 0:
                # a.pop()
                a = a[:-1]
            else:
                a.append(int(i))
        print(len(a))
