## Đặc tả giao diện quản lý gọi món

### **Màn hình Danh sách đơn (UC 2.1, UC 2.2, UC 2.3)**

<img src="media/image1.png" style="width:2.5in;height:5.41026in" />

*Hình 49. Màn hình Danh sách đơn (UC 2.1, UC 2.2, UC 2.3)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon quay lại, nhấn để trở về màn hình trước |  |
| 2 | Text | Tiêu đề “Quản lý gọi món” |  |
| 3 | Icon | Icon chuông thông báo | Báo khi có đơn mới |
| 4 | Button | Avatar “C” của chủ quán, nhấn để mở menu “Đổi mật khẩu” và “Đăng xuất” |  |
| 5 | Text | Đường dẫn “Danh sách đơn \>\> 31/10/2026” | Cho biết đang xem ngày nào |
| 6 | Text | Số đơn của ngày đang xem |  |
| 7 | Button | Ô chọn ngày, nhấn để mở lịch chọn ngày khác | Mặc định là ngày hôm nay |
| 8 | Text | Mã đơn và số bàn của đơn | Đơn mới nhất nằm trên cùng |
| 9 | Text | Giờ đặt và tổng tiền của đơn |  |
| 10 | Text | Nhãn trạng thái đơn: “Chưa xác nhận thanh toán” (màu vàng) hoặc “Đã xác nhận thanh toán” (màu xanh) |  |
| 11 | Button | Nút “Xóa”, nhấn để xóa đơn |  |
| 12 | Button | Mục “Trang chủ” trên thanh điều hướng, nhấn để về màn hình Trang chủ |  |
| 13 | Button | Mục “Đơn hàng” trên thanh điều hướng, nhấn để mở danh sách đơn | Đang được chọn, tô màu đỏ |
| 14 | Button | Mục “Menu” trên thanh điều hướng, nhấn để mở danh sách món |  |
| 15 | Button | Mục “Bàn” trên thanh điều hướng, nhấn để mở sơ đồ bàn |  |
| 16 | Button | Mục “Doanh thu” trên thanh điều hướng, nhấn để mở màn hình doanh thu |  |

*Bảng 55. Mô tả màn hình Danh sách đơn (UC 2.1, UC 2.2, UC 2.3)*

### **Màn hình Chi tiết đơn chưa xác nhận thanh toán (UC 2.1)**

<img src="media/image2.png" style="width:2.5in;height:5.41026in" />

*Hình 50. Màn hình Chi tiết đơn chưa xác nhận thanh toán (UC 2.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Mã đơn |  |
| 2 | Text | Số bàn của đơn |  |
| 3 | Text | Nhãn trạng thái “Chưa xác nhận thanh toán” |  |
| 4 | Text | Tiêu đề “Món đã gọi” |  |
| 5 | Text | Ngày giờ đặt đơn |  |
| 6 | Text | Món trong đơn gồm tên món, đơn giá, số lượng, thành tiền |  |
| 7 | Text | Tổng tiền của đơn |  |
| 8 | Text | Phương thức thanh toán của đơn |  |
| 9 | Text | Ghi chú của khách |  |
| 10 | Button | Nút “Xác nhận đã nhận tiền”, nhấn sau khi đã nhận đủ tiền của đơn | Chỉ hiện với đơn chưa xác nhận thanh toán |
| 11 | Button | Nút “Xóa đơn”, nhấn để xóa đơn |  |

*Bảng 56. Mô tả màn hình Chi tiết đơn chưa xác nhận thanh toán (UC 2.1)*

### **Màn hình Bấm xác nhận đã nhận tiền (UC 2.1)**

<img src="media/image3.png" style="width:2.5in;height:5.41026in" />

*Hình 51. Màn hình Xác nhận đã nhận tiền (UC 2.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Câu hỏi “Bạn đã nhận đủ tiền của đơn này chưa?” |  |
| 2 | Button | Nút “Không”, nhấn để đóng hộp thoại, đơn giữ nguyên |  |
| 3 | Button | Nút “Có”, nhấn để xác nhận đã nhận tiền | Đơn chuyển sang “Đã xác nhận thanh toán” và được tính vào doanh thu |

*Bảng 57. Mô tả màn hình Xác nhận đã nhận tiền (UC 2.1)*

### **Màn hình Xác nhận đã nhận tiền thành công (UC 2.1)**

<img src="media/image4.png" style="width:2.5in;height:5.41026in" />

*Hình 52. Màn hình Xác nhận đã nhận tiền thành công (UC 2.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Nhãn trạng thái đổi thành “Đã xác nhận thanh toán” | Nút “Xác nhận đã nhận tiền” không còn hiện |
| 2 | Icon | Icon dấu tích màu xanh |  |
| 3 | Text | Thông báo “Xác nhận đã nhận tiền!” | Hiện khi lưu thành công |

*Bảng 58. Mô tả màn hình Xác nhận đã nhận tiền thành công (UC 2.1)*

### **Màn hình Xác nhận đã nhận tiền – Lỗi lưu (UC 2.1)**

<img src="media/image5.png" style="width:2.5in;height:5.41026in" />

*Hình 53. Màn hình Xác nhận đã nhận tiền – Lỗi lưu (UC 2.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon cảnh báo màu đỏ |  |
| 2 | Text | Thông báo “Có lỗi xảy ra, vui lòng thử lại!” | Hiện khi lưu không thành công, đơn vẫn “Chưa xác nhận thanh toán” |

*Bảng 59. Mô tả màn hình Xác nhận đã nhận tiền – Lỗi lưu (UC 2.1)*

### **Màn hình Danh sách đơn – Chọn ngày (UC 2.2)**

<img src="media/image6.png" style="width:2.5in;height:5.41026in" />

*Hình 54. Màn hình Danh sách đơn – Chọn ngày (UC 2.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Tháng và năm đang xem: “Tháng 10, 2026” |  |
| 2 | Text | Lịch các ngày trong tháng |  |
| 3 | Button | Ngày được chọn, tô màu đỏ |  |
| 4 | Button | Nút “Tiếp tục”, nhấn để xem danh sách đơn của ngày đã chọn |  |

*Bảng 60. Mô tả màn hình Danh sách đơn – Chọn ngày (UC 2.2)*

### **Màn hình Danh sách đơn – Chưa có đơn (UC 2.2)**

<img src="media/image7.png" style="width:2.5in;height:5.41026in" />

*Hình 55. Màn hình Danh sách đơn – Chưa có đơn (UC 2.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Số đơn của ngày đang xem, ví dụ “0 đơn hàng” |  |
| 2 | Button | Ô chọn ngày, nhấn để chọn ngày khác |  |
| 3 | Icon | Icon danh sách đơn |  |
| 4 | Text | Thông báo “Chưa có đơn nào” | Hiện khi ngày đang xem không có đơn |

*Bảng 61. Mô tả màn hình Danh sách đơn – Chưa có đơn (UC 2.2)*

### **Màn hình Danh sách đơn – Lỗi truy xuất dữ liệu (UC 2.2)**

<img src="media/image8.png" style="width:2.5in;height:5.41026in" />

*Hình 56. Màn hình Danh sách đơn – Lỗi truy xuất dữ liệu (UC 2.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon cảnh báo màu đỏ |  |
| 2 | Text | Thông báo “Có lỗi xảy ra, vui lòng thử lại!” | Hiện khi hệ thống không lấy được danh sách đơn |

*Bảng 62. Mô tả màn hình Danh sách đơn – Lỗi truy xuất dữ liệu (UC 2.2)*

### **Màn hình Chi tiết đơn (UC 2.2)**

<img src="media/image9.png" style="width:2.5in;height:5.41026in" />

*Hình 57. Màn hình Chi tiết đơn (UC 2.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Đường dẫn “Danh sách đơn \>\> Chi tiết đơn” |  |
| 2 | Text | Mã đơn |  |
| 3 | Text | Số bàn của đơn |  |
| 4 | Text | Nhãn trạng thái đơn |  |
| 5 | Text | Tiêu đề “Món đã gọi” |  |
| 6 | Text | Ngày giờ đặt đơn |  |
| 7 | Text | Tên các cột: Tên món / Đơn giá, SL, Thành tiền |  |
| 8 | Text | Các món trong đơn gồm tên món, đơn giá, số lượng, thành tiền | Thành tiền = đơn giá × số lượng |
| 9 | Text | Tổng tiền của đơn | Tổng tiền = cộng thành tiền các món |
| 10 | Text | Phương thức thanh toán của đơn |  |
| 11 | Text | Ghi chú của khách |  |
| 12 | Button | Nút “Xóa đơn”, nhấn để xóa đơn | Đơn đã xác nhận thanh toán thì không có nút “Xác nhận đã nhận tiền” |

*Bảng 63. Mô tả màn hình Chi tiết đơn (UC 2.2)*

### **Màn hình Xác nhận xóa đơn từ danh sách (UC 2.3)**

<img src="media/image10.png" style="width:2.5in;height:5.39182in" />

*Hình 58. Màn hình Xác nhận xóa đơn từ danh sách (UC 2.3)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Button | Nút “Xóa” của đơn cần xóa, ví dụ đơn \#0101 |  |
| 2 | Text | Câu hỏi “Bạn có chắc chắn muốn xóa đơn này không?” |  |
| 3 | Button | Nút “Hủy”, nhấn để đóng hộp thoại, đơn giữ nguyên |  |
| 4 | Button | Nút “Xóa”, nhấn để xóa đơn | Đơn bị đánh dấu đã xóa, không tính vào thống kê |

*Bảng 64. Mô tả màn hình Xác nhận xóa đơn từ danh sách (UC 2.3)*

### **Màn hình Xóa đơn thành công (UC 2.3)**

<img src="media/image11.png" style="width:2.5in;height:5.41026in" />

*Hình 59. Màn hình Xóa đơn thành công (UC 2.3)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Số đơn sau khi xóa, ví dụ “5 đơn hàng” | Danh sách được cập nhật, không còn đơn đã xóa |
| 2 | Icon | Icon dấu tích màu xanh |  |
| 3 | Text | Thông báo “Đã xóa đơn” | Hiện khi xóa đơn thành công |

*Bảng 65. Mô tả màn hình Xóa đơn thành công (UC 2.3)*

### **Màn hình Xác nhận xóa đơn từ chi tiết đơn (UC 2.3)**

<img src="media/image12.png" style="width:2.5in;height:5.41026in" />

*Hình 60. Màn hình Xác nhận xóa đơn từ chi tiết đơn (UC 2.3)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Button | Nút “Xóa đơn” ở màn hình Chi tiết đơn |  |
| 2 | Text | Câu hỏi “Bạn có chắc chắn muốn xóa đơn này không?” |  |
| 3 | Button | Nút “Hủy”, nhấn để đóng hộp thoại, đơn giữ nguyên |  |
| 4 | Button | Nút “Xóa”, nhấn để xóa đơn |  |

*Bảng 66. Mô tả màn hình Xác nhận xóa đơn từ chi tiết đơn (UC 2.3)*

### **Màn hình Xóa đơn thành công từ chi tiết đơn (UC 2.3)**

<img src="media/image13.png" style="width:2.5in;height:5.41026in" />

*Hình 61. Màn hình Xóa đơn thành công từ chi tiết đơn (UC 2.3)*

| **STT** | **Loại** | **Mô tả**              | **Ghi chú**                  |
|:-------:|:--------:|------------------------|------------------------------|
|    1    |   Icon   | Icon dấu tích màu xanh |                              |
|    2    |   Text   | Thông báo “Đã xóa đơn” | Sau đó quay về danh sách đơn |

*Bảng 67. Mô tả màn hình Xóa đơn thành công từ chi tiết đơn (UC 2.3)*

### **Màn hình Xóa đơn – Lỗi lưu (UC 2.3)**

<img src="media/image14.png" style="width:2.5in;height:5.41026in" />

*Hình 62. Màn hình Xóa đơn – Lỗi lưu (UC 2.3)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon cảnh báo màu đỏ |  |
| 2 | Text | Thông báo “Có lỗi xảy ra, vui lòng thử lại!” | Hiện khi xóa không thành công, đơn vẫn giữ nguyên |

*Bảng 68. Mô tả màn hình Xóa đơn – Lỗi lưu (UC 2.3)*
