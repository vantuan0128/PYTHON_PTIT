"""
Một số được gọi là xen kẽ nếu thỏa mãn cả ba tính chất sau:
Số chữ số là số lẻ
Chữ số đầu tiên khác chữ số thứ hai.
Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5…  và vị trí cuối cùng có giá trị bằng nhau
Input:
2
2324272921262
13141516
Output:
YES
NO
"""
def func(s):
    if int(s[0]) == int(s[1]) or len(s) % 2 == 0 or len(s) < 2: return False
    for i in range(2,len(s),2):
        if int(s[i]) != int(s[i-2]): return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        if func(s): print("YES")
        else: print("NO")