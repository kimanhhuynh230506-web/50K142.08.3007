## Use case “Quản lý doanh thu”

Cho phép chủ quán xem tổng doanh thu, doanh thu theo phương thức thanh toán và thống kê bán hàng theo ngày, tháng hoặc năm.

<img src="media/image16.png" style="width:6.5in;height:4.30556in" />

*Hình 18. Sơ đồ Use Case phân rã chức năng Quản lý doanh thu*

### **Business rules**

|  |  |
|----|----|
| **ID** | **Business rules** |
| BR-UC5-01 | Chỉ tính đơn ở trạng thái “Đã xác nhận thanh toán” và chưa bị xóa |
| BR-UC5-02 | Tổng doanh thu của ngày = doanh thu tiền mặt + doanh thu chuyển khoản |
| BR-UC5-03 | Tổng doanh thu tháng = tổng doanh thu tất cả các ngày trong tháng |
| BR-UC5-04 | Tổng doanh thu năm = tổng doanh thu tất cả các tháng trong năm |
| BR-UC5-05 | Danh sách mặc định theo ngày, kỳ mới nhất ở trên cùng |
| BR-UC5-06 | Tổng doanh thu = doanh thu tiền mặt + doanh thu chuyển khoản |
| BR-UC5-07 | Kỳ được xem là kỳ (ngày, tháng hoặc năm) chủ quán đã chọn trong danh sách tổng doanh thu |
| BR-UC5-08 | Tổng số ly = tổng số lượng của tất cả món trong các đơn tính được |
| BR-UC5-09 | Lấy đồng hạng nếu có nhiều món có cùng số lượng bán nhiều nhất |
| BR-UC5-10 | Danh sách món sắp xếp theo số lượng bán giảm dần |

*Bảng 19. Business rules của use case “Quản lý doanh thu”*

### **Xem tổng doanh thu**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_5.1</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xem tổng doanh thu</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xem tổng doanh thu theo từng ngày, tháng hoặc năm</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Doanh thu”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Hệ thống hiển thị danh sách tổng doanh thu theo ngày, tháng hoặc năm</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Doanh thu”</p>
<p>2. Hệ thống hiển thị danh sách tổng doanh thu theo ngày gồm ngày và tổng doanh thu, ngày mới nhất ở trên cùng</p>
<p>3. Chủ quán xem danh sách tổng doanh thu</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>3a. Chủ quán muốn xem kỳ khác</p>
<p>3a1. Chủ quán chọn “Ngày”, “Tháng” hoặc “Năm”.</p>
<p>3a2. Hệ thống hiển thị danh sách tổng doanh thu theo kỳ đã chọn gồm kỳ và tổng doanh thu, kỳ mới nhất ở trên cùng.</p>
<p>3a3. Chủ quán xem danh sách tổng doanh thu theo kỳ đã chọn.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>2a. Hệ thống truy xuất dữ liệu không thành công</p>
<p>2a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p>
<p>2b. Chưa có ngày nào có doanh thu</p>
<p>2b1. Hệ thống hiển thị thông báo “Chưa có doanh thu nào”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Chỉ tính đơn ở trạng thái “Đã xác nhận thanh toán” và chưa bị xóa</p>
<p>BR02. Tổng doanh thu của ngày = doanh thu tiền mặt + doanh thu chuyển khoản</p>
<p>BR03. Tổng doanh thu tháng = tổng doanh thu tất cả các ngày trong tháng</p>
<p>BR04. Tổng doanh thu năm = tổng doanh thu tất cả các tháng trong năm</p>
<p>BR05. Danh sách mặc định theo ngày, kỳ mới nhất ở trên cùng</p></td>
</tr>
</tbody>
</table>

*Bảng 20. Đặc tả use case “Xem tổng doanh thu”*

**Sơ đồ Activity Diagram**

<img src="media/image17.png" style="width:6.10236in;height:6.5153in" />

*Hình 19. Sơ đồ activity diagram “Xem tổng doanh thu”*

### **Xem thống kê doanh thu theo phương thức thanh toán**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_5.2</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xem thống kê doanh thu theo phương thức thanh toán</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xem doanh thu tiền mặt và doanh thu chuyển khoản của ngày, tháng hoặc năm tôi chọn</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn một ngày, tháng hoặc năm trong danh sách tổng doanh thu</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Chủ quán đang ở màn hình danh sách tổng doanh thu trong “Doanh thu”</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Hệ thống hiển thị doanh thu tiền mặt, doanh thu chuyển khoản của kỳ đã chọn</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn một ngày, tháng hoặc năm trong danh sách tổng doanh thu</p>
<p>2. Hệ thống hiển thị bảng chi tiết của kỳ đã chọn gồm doanh thu tiền mặt, doanh thu chuyển khoản và tổng doanh thu</p>
<p>3. Chủ quán xem doanh thu theo phương thức thanh toán</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>2a. Hệ thống truy xuất dữ liệu không thành công</p>
<p>2a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Chỉ tính đơn ở trạng thái “Đã xác nhận thanh toán” và chưa bị xóa</p>
<p>BR02. Tổng doanh thu = doanh thu tiền mặt + doanh thu chuyển khoản</p>
<p>BR03. Kỳ được xem là kỳ (ngày, tháng hoặc năm) chủ quán đã chọn trong danh sách tổng doanh thu</p></td>
</tr>
</tbody>
</table>

*Bảng 21. Đặc tả use case “Xem thống kê doanh thu theo phương thức thanh toán”*

**Sơ đồ Activity Diagram**

<img src="media/image18.png" style="width:6.5in;height:5.53611in" />

*Hình 20. Sơ đồ activity diagram “Xem thống kê doanh thu theo phương thức thanh toán”*

### **Xem thống kê bán hàng**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_5.3</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xem thống kê bán hàng</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xem tổng số ly đã bán, số lượng bán của từng món và món bán chạy nhất của ngày, tháng hoặc năm tôi chọn</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn một ngày, tháng hoặc năm trong danh sách tổng doanh thu</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Chủ quán đang ở màn hình danh sách tổng doanh thu trong “Doanh thu”</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Hệ thống hiển thị tổng số ly bán ra, số lượng bán của từng món và món bán chạy nhất của kỳ đã chọn</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn một ngày, tháng hoặc năm trong danh sách tổng doanh thu</p>
<p>2. Hệ thống hiển thị bảng chi tiết của kỳ đã chọn gồm tổng số ly bán ra, số lượng bán của từng món và món bán chạy nhất</p>
<p>3. Chủ quán xem thống kê bán hàng</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>2a. Hệ thống truy xuất dữ liệu không thành công</p>
<p>2a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Chỉ tính đơn ở trạng thái “Đã xác nhận thanh toán” và chưa bị xóa</p>
<p>BR02. Tổng số ly = tổng số lượng của tất cả món trong các đơn tính được</p>
<p>BR03. Lấy đồng hạng nếu có nhiều món có cùng số lượng bán nhiều nhất</p>
<p>BR04. Kỳ được xem là kỳ (ngày, tháng hoặc năm) chủ quán đã chọn trong danh sách tổng doanh thu</p>
<p>BR05. Danh sách món sắp xếp theo số lượng bán giảm dần</p></td>
</tr>
</tbody>
</table>

*Bảng 22. Đặc tả use case “Xem thống kê bán hàng”*

**Sơ đồ Activity Diagram**

<img src="media/image19.png" style="width:6.72398in;height:5.72688in" />

*Hình 21. Sơ đồ activity diagram “Xem thống kê bán hàng”*

