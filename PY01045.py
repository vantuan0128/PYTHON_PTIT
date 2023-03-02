"""
Một xâu ký tự là xâu palindrome là một xâu khác rỗng mà nếu lật ngược xâu ấy ta thu được xâu ban đầu. Ví dụ các xâu abcba, dd là xâu palindrome,
trong khi các xâu abc, ptit thì không phải.
Cho một xâu ký tự A. Tìm cách xoá đi nhiều nhất các kí tự của A để
thu được một xâu palindrome.
Input:
abccba
Output:
5
"""

if __name__ == "__main__":
    print(len(input()) - 1)