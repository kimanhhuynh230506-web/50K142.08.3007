## Đặc tả giao diện khách hàng

### **Màn hình Menu (UC 7.1)**

<img src="media/image1.png" style="width:2.5in;height:5.41026in" />

*Hình 31. Màn hình Menu (UC 7.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Tiêu đề “Menu” |  |
| 2 | Text | Số bàn khách đang ngồi | Lấy theo mã QR khách đã quét |
| 3 | Text | Tiêu đề “Món đề cử” |  |
| 4 | Text | Nhãn thứ hạng của món đề cử |  |
| 5 | Image | Hình ảnh của món đề cử | Món không có hình thì dùng hình mặc định |
| 6 | Text | Tên món đề cử |  |
| 7 | Text | Giá bán của món đề cử |  |
| 8 | Text | Tiêu đề “Tất cả món” |  |
| 9 | Image | Hình ảnh của món | Món không có hình thì dùng hình mặc định |
| 10 | Text | Tên món |  |
| 11 | Text | Giá bán của món |  |
| 12 | Button | Nút “+”, nhấn để thêm món vào đơn | Mỗi lần nhấn tăng số lượng lên 1 |

*Bảng 37. Mô tả màn hình Menu (UC 7.1)*

### **Màn hình Menu – Chưa có món (UC 7.1)**

<img src="media/image2.png" style="width:2.5in;height:5.33733in" />

*Hình 32. Màn hình Menu – Chưa có món (UC 7.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Tiêu đề “Menu” |  |
| 2 | Text | Số bàn khách đang ngồi: “Bàn 03” |  |
| 3 | Icon | Icon ly cà phê |  |
| 4 | Text | Thông báo “Menu chưa có món nào” | Hiện khi quán chưa có món nào đang hiển thị |

*Bảng 38. Mô tả màn hình Menu – Chưa có món (UC 7.1)*

### **Màn hình Menu – Lỗi tải dữ liệu (UC 7.1)**

<img src="media/image3.png" style="width:2.5in;height:5.41026in" />

*Hình 33. Màn hình Menu – Lỗi tải dữ liệu (UC 7.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon cảnh báo màu đỏ |  |
| 2 | Text | Thông báo “Có lỗi xảy ra, vui lòng thử lại!” | Hiện khi hệ thống không tải được menu |

*Bảng 39. Mô tả màn hình Menu – Lỗi tải dữ liệu (UC 7.1)*

### **Màn hình Menu – Mã QR không hợp lệ (UC 7.1)**

<img src="media/image4.png" style="width:2.5in;height:5.41026in" />

*Hình 34. Màn hình Menu – Mã QR không hợp lệ (UC 7.1)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon cảnh báo màu đỏ |  |
| 2 | Text | Thông báo “Mã QR không hợp lệ” | Hiện khi mã QR sai hoặc bàn đã bị xóa |

*Bảng 40. Mô tả màn hình Menu – Mã QR không hợp lệ (UC 7.1)*

### **Màn hình Menu – Đã chọn món (UC 7.2)**

<img src="media/image5.png" style="width:2.5in;height:5.41026in" />

*Hình 35. Màn hình Menu – Đã chọn món (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Button | Nút “−”, nhấn để giảm số lượng món |  |
| 2 | Text | Số lượng đã chọn của món |  |
| 3 | Text | Tổng số món đã chọn |  |
| 4 | Text | Tổng tiền của đơn | Tổng tiền = giá × số lượng của các món cộng lại |
| 5 | Button | Nút “Tiếp tục”, nhấn để chuyển sang màn hình Thanh toán |  |

*Bảng 41. Mô tả màn hình Menu – Đã chọn món (UC 7.2)*

### **Màn hình Menu – Chưa chọn món (UC 7.2)**

<img src="media/image6.png" style="width:2.5in;height:5.41026in" />

*Hình 36. Màn hình Menu – Chưa chọn món (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon cảnh báo màu đỏ |  |
| 2 | Text | Thông báo “Vui lòng chọn ít nhất một món” | Hiện khi nhấn “Tiếp tục” mà chưa chọn món |

*Bảng 42. Mô tả màn hình Menu – Chưa chọn món (UC 7.2)*

### **Màn hình Thanh toán – Đơn của bạn (UC 7.2)**

<img src="media/image7.png" style="width:2.5in;height:5.42124in" />

*Hình 37. Màn hình Thanh toán – Đơn của bạn (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon quay lại, nhấn để trở về màn hình Menu |  |
| 2 | Text | Tiêu đề “Thanh toán” |  |
| 3 | Text | Tiêu đề “Đơn của bạn” |  |
| 4 | Text | Tên món đã chọn |  |
| 5 | Text | Đơn giá của món |  |
| 6 | Button | Nút “−”, nhấn để giảm số lượng món |  |
| 7 | Text | Số lượng của món |  |
| 8 | Button | Nút “+”, nhấn để tăng số lượng món |  |
| 9 | Text | Nhãn “Ghi chú (không bắt buộc)” |  |
| 10 | Input Text | Ô nhập ghi chú cho cả đơn | Không bắt buộc, tối đa 200 ký tự |
| 11 | Text | Chữ gợi ý (placeholder) “Ví dụ: ít đá, không đường…” |  |
| 12 | Text | Bộ đếm số ký tự đã nhập “0/200” |  |

*Bảng 43. Mô tả màn hình Thanh toán – Đơn của bạn (UC 7.2)*

### **Màn hình Thanh toán – Phương thức thanh toán (UC 7.2)**

<img src="media/image8.png" style="width:2.5in;height:5.41026in" />

*Hình 38. Màn hình Thanh toán – Phương thức thanh toán (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Tên món và số lượng: “Bạc xỉu x2” |  |
| 2 | Text | Thành tiền của món | Thành tiền = giá × số lượng |
| 3 | Text | Chữ “Tổng tiền” |  |
| 4 | Text | Tổng tiền của đơn |  |
| 5 | Text | Tiêu đề “Phương thức thanh toán” |  |
| 6 | Radio | Lựa chọn “Chuyển khoản – Quét mã QR ngân hàng” |  |
| 7 | Radio | Lựa chọn “Tiền mặt – Trả tiền khi nhận món tại bàn” |  |

*Bảng 44. Mô tả màn hình Thanh toán – Phương thức thanh toán (UC 7.2)*

### **Màn hình Thanh toán chuyển khoản (UC 7.2)**

<img src="media/image9.png" style="width:2.5in;height:5.41026in" />

*Hình 39. Màn hình Thanh toán chuyển khoản (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Số bàn và phương thức đã chọn “Bàn 03 · Chuyển khoản” |  |
| 2 | Text | Dòng chữ “Quét mã QR để chuyển khoản” |  |
| 3 | Image | Mã QR ngân hàng để khách quét chuyển khoản | Mã QR có sẵn số tiền của đơn |
| 4 | Text | Số tiền cần chuyển |  |
| 5 | Text | Tên ngân hàng |  |
| 6 | Text | Số tài khoản của quán |  |
| 7 | Text | Tên chủ tài khoản |  |
| 8 | Text | Nội dung chuyển khoản | Nội dung là số bàn |
| 9 | Button | Nút “Hoàn tất”, nhấn sau khi đã chuyển khoản để gửi đơn | Đơn được lưu với trạng thái “Chưa xác nhận thanh toán” |
| 10 | Text | Lời nhắc “Sau khi chuyển khoản, nhấn Hoàn tất. Vui lòng chụp lại giao dịch để đối chiếu khi cần thiết” |  |

*Bảng 45. Mô tả màn hình Thanh toán chuyển khoản (UC 7.2)*

### **Màn hình Thanh toán tiền mặt (UC 7.2)**

<img src="media/image10.png" style="width:2.5in;height:5.41026in" />

*Hình 40. Màn hình Thanh toán tiền mặt (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Text | Số bàn và phương thức đã chọn “Bàn 03 · Tiền mặt” |  |
| 2 | Text | Chữ “Tổng tiền” |  |
| 3 | Text | Tổng tiền của đơn |  |
| 4 | Text | Thông báo “Chờ thu tiền sau khi bưng nước ra” |  |
| 5 | Button | Nút “Hoàn tất”, nhấn để gửi đơn | Đơn được lưu với trạng thái “Chưa xác nhận thanh toán” |

*Bảng 46. Mô tả màn hình Thanh toán tiền mặt (UC 7.2)*

### **Màn hình Đặt món thành công (UC 7.2)**

<img src="media/image11.png" style="width:2.5in;height:5.41026in" />

*Hình 41. Màn hình Đặt món thành công (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon dấu tích màu xanh |  |
| 2 | Text | Thông báo “Đặt món thành công” | Hiện khi đơn được lưu thành công |

*Bảng 47. Mô tả màn hình Đặt món thành công (UC 7.2)*

### **Màn hình Đặt món không thành công (UC 7.2)**

<img src="media/image12.png" style="width:2.5in;height:5.41026in" />

*Hình 42. Màn hình Đặt món không thành công (UC 7.2)*

| **STT** | **Loại** | **Mô tả** | **Ghi chú** |
|:--:|:--:|----|----|
| 1 | Icon | Icon cảnh báo màu đỏ |  |
| 2 | Text | Thông báo “Đặt món không thành công, vui lòng thử lại!” | Hiện khi lưu đơn bị lỗi |

*Bảng 48. Mô tả màn hình Đặt món không thành công (UC 7.2)*
