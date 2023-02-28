"""
Trong 10 chữ số thập phân thì có 4 chữ số nguyên tố là 2, 3, 5, 7.
Một số nguyên dương được coi là thỏa mãn nguyên tố đúng vị trí nếu thỏa mãn cả hai điều kiện:
Nếu i là nguyên tố thì vị trí thứ i cũng phải là chữ số nguyên tố.
Ngược lại nếu i không phải là số nguyên tố thì vị trí thứ i không phải là chữ số nguyên tố.
Input:
2
14239567
2314514535353
Output:
YES
NO
"""
import math

def SNT(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1),1):
        if n % i == 0: return False
    return True

def check(s):
    for i in range(0,len(s)):
        if s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7':
            if not SNT(i): return False
        else:
            if SNT(i): return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s): print("YES")
        else: print("NO")