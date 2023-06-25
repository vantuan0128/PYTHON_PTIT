"""
Một thông báo (notification) là một tin nhắn, thông điệp được hiển thị trong một thời gian ngắn trên thanh trạng thái của thiết bị
nhằm gây sự chú ý của người dùng. Nó tương tự như một tin nhắn thông thường (SMS ), tuy nhiên nó khác SMS là dịch vụ này hiện nay là hoàn toàn miễn phí
 và cần có kết nối internet mới có thể gửi và nhận notification. và notification chỉ có thể gửi cho ứng dụng mà nhà phát triển đã đăng ký và người dùng
  có cài ứng dụng đó. Các notification này sẽ hiển thị trên thanh trạng thái của smartphone và tablet, thường thanh trạng thái ở phía trên cùng của
  màn hình. Thông thường một thông báo là được tự động kích hoạt nhằm thông báo tới người dùng là ứng dụng đó đã hoàn thành một công việc nào đó.
  Hoặc bạn có thể gửi thông tin khuyến mãi tới cho khách hàng của bạn, mời khách hàng tham gia một sự kiện nào đó...

Theo quy định của một số thiết bị. Nội dung thông báo chỉ được phép chứa tối đa 100 ký tự.
Điều này đòi hỏi lập trình viên phải xử lý nội dung các thông báo có độ dài lớn hơn 100 ký tự bằng cách rút gọn thông tin.
Tuy nhiên, việc rút gọn phải đảm bảo nguyên tắc không bị cắt giữa từ. Trong trường hợp nếu từ hiện tại làm độ dài thông báo
vượt quá 100 ký tự sẽ loại bỏ từ đó khỏi thông báo.

Nhiệm vụ của bạn là hãy viết chương trình xử lý yêu cầu trên.
Input:
2
Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
Output:
Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va
Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
"""
def func():
    s=[str(x) for x in input().split(" ")]
    l=len(s)
    sum=0
    for i in range(l):
        sum+=len(s[i])
        if sum<=100:
            print(s[i],end=' ')
            sum+=1
    print()
for i in range(int(input())):func()