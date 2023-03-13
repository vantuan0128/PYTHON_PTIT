"""
Một file code Python sẽ có phần mở rộng là .py. 
Trong hệ điều hành Windows tên file sẽ không phân biệt chữ hoa, chữ thường. 
Hãy kiểm tra xem tên file có đúng là file code Python hay không. 
Chỉ có một dòng ghi tên file S (1 ≤ |S| ≤ 128). Tên file chỉ chứa các ký tự a-z, A-Z, . và dấu _.
Input:
abc.py
yes
abc.bin
no
"""

if __name__ == "__main__":
    s = input()
    t = s.split('.')
    if t[-1].lower() == 'py': print("yes")
    else: print("no")