## Use case “Quản lý gọi món”

Cho phép chủ quán xem chi tiết đơn, cập nhật trạng thái đơn khi đã nhận tiền và xóa đơn.

<img src="media/image2.png" style="width:6.5in;height:4.68194in" />

*Hình 4. Sơ đồ Use Case phân rã chức năng Quản lý gọi món*

### **Business rules**

|  |  |
|----|----|
| **ID** | **Business rules** |
| BR-UC2-01 | Mỗi đơn chỉ được chuyển sang “Đã xác nhận thanh toán” một lần |
| BR-UC2-02 | Doanh thu của đơn chỉ được tính khi đơn ở trạng thái “Đã xác nhận thanh toán” |
| BR-UC2-03 | Nút “Xác nhận đã nhận tiền” chỉ hiển thị với đơn ở trạng thái “Chưa xác nhận thanh toán” |
| BR-UC2-04 | Danh sách đơn sắp xếp đơn mới nhất lên đầu |
| BR-UC2-05 | Mặc định hiển thị đơn của ngày hiện tại |
| BR-UC2-06 | Trạng thái đơn gồm “Chưa xác nhận thanh toán” và “Đã xác nhận thanh toán”; đơn mới tạo luôn ở trạng thái “Chưa xác nhận thanh toán” |
| BR-UC2-07 | Đơn đã xóa không được tính vào doanh thu. |
| BR-UC2-08 | Hệ thống chỉ đánh dấu xóa, không xóa hẳn dữ liệu đơn. |
| BR-UC2-09 | Xóa đơn không làm thay đổi trạng thái bàn |

*Bảng 5. Business rules của use case “Quản lý gọi món”*

### **Cập nhật trạng thái đơn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_2.1</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Cập nhật trạng thái đơn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn cập nhật đơn bằng cách xác nhận đã nhận tiền để ghi nhận doanh thu chính xác</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Đơn hàng”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Đơn tồn tại và chưa bị xóa</p>
<p>Đơn đang ở trạng thái “Chưa xác nhận thanh toán”</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Đơn được chuyển sang trạng thái “Đã xác nhận thanh toán”</p>
<p>Thời gian giao dịch được ghi nhận và đơn được tính vào doanh thu</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Đơn hàng”</p>
<p>2. Hệ thống hiển thị danh sách đơn</p>
<p>3. Chủ quán chọn đơn cần cập nhật</p>
<p>4. Hệ thống hiển thị chi tiết đơn cùng “Xác nhận đã nhận tiền”</p>
<p>5. Chủ quán nhấn “Xác nhận đã nhận tiền”</p>
<p>6. Hệ thống hiển thị thông báo xác nhận “Bạn đã nhận đủ tiền của đơn này chưa?”</p>
<p>7. Chủ quán nhấn “Có”</p>
<p>8. Hệ thống đồng thời chuyển đơn sang trạng thái “Đã xác nhận thanh toán”, ghi nhận thời gian giao dịch và tính đơn vào doanh thu</p>
<p>9. Hệ thống lưu thông tin xác nhận</p>
<p>10. Hệ thống hiển thị thông báo “Xác nhận đã nhận tiền!”</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>7a. Chủ quán nhấn “Không”</p>
<p>7a1. Hệ thống giữ nguyên đơn.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>9a. Hệ thống lưu không thành công</p>
<p>9a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Mỗi đơn chỉ được chuyển sang “Đã xác nhận thanh toán” một lần</p>
<p>BR02. Doanh thu của đơn chỉ được tính khi đơn ở trạng thái “Đã xác nhận thanh toán”</p>
<p>BR03. Nút “Xác nhận đã nhận tiền” chỉ hiển thị với đơn ở trạng thái “Chưa xác nhận thanh toán”</p></td>
</tr>
</tbody>
</table>

*Bảng 6. Đặc tả use case “Cập nhật trạng thái đơn”*

**Sơ đồ Activity Diagram**

<img src="media/image3.png" style="width:5.79353in;height:7.66652in" />

*Hình 5. Sơ đồ activity diagram “Cập nhật trạng thái đơn”*

### **Xem chi tiết đơn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_2.2</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xem chi tiết đơn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xem chi tiết một đơn để biết khách gọi món gì và trạng thái đơn</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Đơn hàng”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Hệ thống hiển thị chi tiết đơn đã chọn</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Đơn hàng”</p>
<p>2. Hệ thống hiển thị danh sách đơn của ngày hiện tại gồm mã đơn, số bàn, thời gian đặt, tổng tiền và trạng thái đơn</p>
<p>3. Chủ quán chọn đơn cần xem</p>
<p>4. Hệ thống hiển thị chi tiết đơn gồm mã đơn, số bàn, tên món, số lượng, giá, tổng tiền, thời gian đặt, phương thức thanh toán, ghi chú, trạng thái đơn</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>3a. Chủ quán muốn xem đơn của ngày khác</p>
<p>3a1. Chủ quán chọn ngày muốn xem.</p>
<p>3a2. Hệ thống hiển thị danh sách đơn của ngày đã chọn (nếu ngày đó chưa có đơn nào thì xử lý như 2b).</p>
<p>UC tiếp tục bước 3.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>2a. Hệ thống truy xuất dữ liệu không thành công</p>
<p>2a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p>
<p>2b. Ngày đang xem chưa có đơn nào</p>
<p>2b1. Hệ thống hiển thị thông báo “Chưa có đơn nào”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Danh sách đơn sắp xếp đơn mới nhất lên đầu</p>
<p>BR02. Mặc định hiển thị đơn của ngày hiện tại</p>
<p>BR03. Trạng thái đơn gồm “Chưa xác nhận thanh toán” và “Đã xác nhận thanh toán”; đơn mới tạo luôn ở trạng thái “Chưa xác nhận thanh toán”</p></td>
</tr>
</tbody>
</table>

*Bảng 7. Đặc tả use case “Xem chi tiết đơn”*

**Sơ đồ Activity Diagram**

<img src="media/image4.png" style="width:6.5in;height:5.47361in" />

*Hình 6. Sơ đồ activity diagram “Xem chi tiết đơn”*

### **Xóa đơn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_2.3</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xóa đơn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xóa đơn khi khách đổi ý hoặc gọi nhầm món</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Đơn hàng”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Đơn tồn tại và chưa bị xóa</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Đơn được đánh dấu đã xóa</p>
<p>Doanh thu được tính lại sau khi đơn bị xóa</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Đơn hàng”</p>
<p>2. Hệ thống hiển thị danh sách đơn</p>
<p>3. Chủ quán nhấn “Xóa” trên đơn cần xóa</p>
<p>4. Hệ thống hiển thị thông báo xác nhận “Bạn có chắc chắn muốn xóa đơn này không?”</p>
<p>5. Chủ quán nhấn “Xóa”</p>
<p>6. Hệ thống đánh dấu đơn đã xóa và loại đơn khỏi thống kê</p>
<p>7. Hệ thống đồng thời hiển thị thông báo “Đã xóa đơn”, cập nhật lại danh sách đơn và doanh thu</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>3a. Chủ quán chọn vào xem chi tiết đơn để xóa</p>
<p>3a1. Hệ thống hiển thị chi tiết đơn kèm “Xóa đơn”.</p>
<p>3a2. Chủ quán chọn “Xóa đơn”.</p>
<p>UC tiếp tục bước 4.</p>
<p>5a. Chủ quán nhấn “Hủy”</p>
<p>5a1. Hệ thống giữ nguyên đơn.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>6a. Hệ thống lưu không thành công</p>
<p>6a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Đơn đã xóa không được tính vào doanh thu.</p>
<p>BR02. Hệ thống chỉ đánh dấu xóa, không xóa hẳn dữ liệu đơn.</p>
<p>BR03. Xóa đơn không làm thay đổi trạng thái bàn</p></td>
</tr>
</tbody>
</table>

*Bảng 8. Đặc tả use case “Xóa đơn”*

**Sơ đồ Activity Diagram**

<img src="media/image5.png" style="width:6.5in;height:7.99583in" />

*Hình 7. Sơ đồ activity diagram “Xóa đơn”*

