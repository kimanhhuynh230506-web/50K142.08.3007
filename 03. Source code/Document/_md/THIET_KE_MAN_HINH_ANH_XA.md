# THIẾT KẾ VÀ ĐẶC TẢ GIAO DIỆN

## Sơ đồ luồng màn hình

Giao diện của khách hàng (sau khi quét mã QR tại bàn):

<img src="media/image1.png" style="width:2.6in;height:4.38626in" />

*Hình 29. Sơ đồ luồng màn hình của khách hàng*

Giao diện của chủ quán (sau khi đăng nhập):

<img src="media/image2.png" style="width:6.5in;height:2.72093in" />

*Hình 30. Sơ đồ luồng màn hình của chủ quán*

## Ánh xạ màn hình và use case

### **Danh sách màn hình**

| **Mã** | **Tên màn hình** | **Người dùng** | **Mô tả** |
|:--:|----|:--:|----|
| U1 | Menu (khách quét QR) | Khách hàng | Xem menu, chọn món và số lượng |
| U2 | Thanh toán | Khách hàng | Xem lại đơn, nhập ghi chú, chọn phương thức thanh toán |
| U3 | Thanh toán chuyển khoản | Khách hàng | Hiển thị mã QR ngân hàng kèm số tiền, gửi đơn |
| U4 | Thanh toán tiền mặt | Khách hàng | Hiển thị tổng tiền, gửi đơn |
| U5 | Đăng nhập | Chủ quán | Nhập tên đăng nhập và mật khẩu |
| U6 | Trang chủ | Chủ quán | Vào các chức năng quản lý, mở menu tài khoản |
| U7 | Danh sách đơn | Chủ quán | Xem danh sách đơn theo ngày, xóa đơn |
| U8 | Chi tiết đơn | Chủ quán | Xem chi tiết đơn, xác nhận đã nhận tiền, xóa đơn |
| U9 | Danh sách món | Chủ quán | Xem danh sách món, chọn thêm, cập nhật, xóa món |
| U10 | Thêm món | Chủ quán | Nhập tên, giá, hình ảnh của món mới |
| U11 | Cập nhật món | Chủ quán | Sửa tên, giá, hình ảnh, trạng thái món |
| U12 | Sơ đồ bàn | Chủ quán | Xem trạng thái bàn, xóa bàn, xác nhận bàn trống |
| U13 | Thêm bàn | Chủ quán | Nhập số bàn, tạo và tải mã QR của bàn |
| U14 | Tổng doanh thu | Chủ quán | Xem tổng doanh thu theo ngày, tháng, năm |
| U15 | Chi tiết doanh thu | Chủ quán | Xem doanh thu theo phương thức thanh toán và thống kê bán hàng của kỳ đã chọn |
| U16 | Đổi mật khẩu | Chủ quán | Nhập mật khẩu cũ, mật khẩu mới |

*Bảng 34. Danh sách màn hình*

### **Danh sách use case**

| **STT** | **Mã use case** | **Tên use case** | **Actor** |
|:--:|:--:|----|:--:|
| 1 | UC_1 | Đăng nhập | Chủ quán |
| 2 | UC_2.1 | Cập nhật trạng thái đơn | Chủ quán |
| 3 | UC_2.2 | Xem chi tiết đơn | Chủ quán |
| 4 | UC_2.3 | Xóa đơn | Chủ quán |
| 5 | UC_3.1 | Xem danh sách món | Chủ quán |
| 6 | UC_3.2 | Thêm món | Chủ quán |
| 7 | UC_3.3 | Xóa món | Chủ quán |
| 8 | UC_3.4 | Cập nhật món | Chủ quán |
| 9 | UC_4.1 | Xem trạng thái bàn | Chủ quán |
| 10 | UC_4.2 | Thêm bàn | Chủ quán |
| 11 | UC_4.3 | Xóa bàn | Chủ quán |
| 12 | UC_4.4 | Cập nhật trạng thái bàn | Chủ quán |
| 13 | UC_5.1 | Xem tổng doanh thu | Chủ quán |
| 14 | UC_5.2 | Xem thống kê doanh thu theo phương thức thanh toán | Chủ quán |
| 15 | UC_5.3 | Xem thống kê bán hàng | Chủ quán |
| 16 | UC_6 | Đổi mật khẩu | Chủ quán |
| 17 | UC_7.1 | Xem menu | Khách hàng |
| 18 | UC_7.2 | Tạo đơn | Khách hàng |
| 19 | UC_8 | Đăng xuất | Chủ quán |

*Bảng 35. Danh sách use case*

### **Bảng ánh xạ use case – màn hình**

| **UC \\ UI** | **U1** | **U2** | **U3** | **U4** | **U5** | **U6** | **U7** | **U8** | **U9** | **U10** | **U11** | **U12** | **U13** | **U14** | **U15** | **U16** |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 2.1 |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  |
| 2.2 |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  |
| 2.3 |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  |
| 3.1 |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |
| 3.2 |  |  |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |
| 3.3 |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |
| 3.4 |  |  |  |  |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |
| 4.1 |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |
| 4.2 |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |  |  |
| 4.3 |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |
| 4.4 |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |
| 5.1 |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |
| 5.2 |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |
| 5.3 |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |
| 6 |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  | ✓ |
| 7.1 | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7.2 | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |

*Bảng 36. Bảng ánh xạ use case – màn hình*
