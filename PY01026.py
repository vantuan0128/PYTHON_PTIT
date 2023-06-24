"""
Cho hai xâu ký tự s1 và s2. Xâu s2 được gọi là một “sắp đặt lại” của xâu s1 nếu tập ký tự của xâu s2
hoàn toàn giống với xâu ký tự s1, tính cả số lần xuất hiện của từng ký tự.

Ví dụ: s2 = “intestg” là sắp đặt lại của xâu “testing”

Còn xâu “aabbbcccc” không được coi là sắp đặt lại của xâu “abc”.

Nhập 2 xâu s1 và s2 có độ dài không quá 1000 ký tự, chỉ bao gồm các ký tự viết thường, không có khoảng trống.
Hãy kiểm tra xem s2 có phải là sắp đặt lại của s1 hay không.

Input

Dòng đầu ghi số bộ test, không quá 5000.

Mỗi test ghi trên 2 dòng lần lượt là xâu s1 và s2.

Output

Ghi ra thứ tự bộ test, sau đó là YES hoặc NO tùy thuộc kết quả kiểm tra.

Xem ví dụ để hiểu rõ hơn.
Input:
4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
Output:
Test 1: YES
Test 2: NO
Test 3: YES
Test 4: NO
"""
if __name__ == "__main__":
    n = int(input())
    i = 1
    while i <= n:
        s1 = input()
        s2 = input()
        print('Test '+str(i)+':',end='')
        if (sorted(s1) == sorted(s2)): print(" YES ")
        else: print(" NO ")
        i += 1