"""
Địa chỉ IP (IP là viết tắt của từ tiếng Anh: Internet Protocol - giao thức Internet) là một địa chỉ đơn nhất mà những thiết bị điện tử hiện
 nay đang sử dụng để nhận diện và liên lạc với nhau trên mạng máy tính bằng cách sử dụng giao thức Internet.

Bất kỳ thiết bị mạng nào bao gồm bộ định tuyến, bộ chuyển mạch mạng, máy vi tính, máy chủ hạ tầng (như NTP, DNS, DHCP, SNMP, v.v.),
máy in, máy fax qua Internet, và vài loại điện thoại—tham gia vào mạng đều có địa chỉ riêng, và địa chỉ này là đơn nhất trong phạm vi của một mạng cụ thể.
 Vài địa chỉ IP có giá trị đơn nhất trong phạm vi Internet toàn cầu, trong khi một số khác chỉ cần phải đơn nhất trong phạm vi một công ty.

Ipv4 viết tắt cho Internet Protocol Version 4, dịch ra có nghĩa là giao thức Internet phiên bản thứ 4.
Ipv4 đã được bộ quốc phòng Hoa Kỳ chuẩn hóa trong bản MIL-STD-1777. Giao thức Internet IP đã trải qua nhiều phiên bản khác nhau và phiên bản Ipv4
là phiên bản đầu tiên được sử dụng rộng rãi trên toàn thế giới và hiện vẫn còn đang là nòng cốt của Internet trên toàn thế giới.

Để hiểu địa chỉ Ipv4 là gì có thể lấy ví dụ như sau: Giả sử ta có 1 dải số như sau: 172.16.254.1. Dải số này có thể được dùng để đặt tên cho 1 địa chỉ
Ipv4 nào đó. Có thể thấy địa chỉ Ipv4 có tổng cộng 4 số và mỗi số phải nằm trong giới hạn từ 0-255.

Cho một danh sách các chuỗi ký tự, hãy kiểm tra xem chuỗi ký tự này có phải địa chỉ IP hợp lệ hay không.
Input:
2
192.168.1.1
256.255.255.255
Output:
YES
NO
"""
def func():
    s=input()
    a=s.split(".")
    if len(a)==4:
        dem=0
        i=0
        while i<4:
            res=0
            for j in a[i]:
                if j>='0' and j<='9': res+=1
            if res==len(a[i]):
                m=int(a[i])
                if m>=0 and m<=255 : dem+=1
            i+=1
        if dem==4: print("YES")
        else: print("NO")
    else: print("NO")
for i in range(int(input())):
    func()