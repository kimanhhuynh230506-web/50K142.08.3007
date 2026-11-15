## Use case “Quản lý bàn”

Cho phép chủ quán xem trạng thái bàn, thêm bàn kèm mã QR riêng, xóa bàn và xác nhận bàn trống.

<img src="media/image11.png" style="width:6.5in;height:4.2375in" />

*Hình 13. Sơ đồ Use Case phân rã chức năng Quản lý bàn*

### **Business rules**

|  |  |
|----|----|
| **ID** | **Business rules** |
| BR-UC4-01 | Bàn chuyển sang “Đang phục vụ” khi khách gửi đơn |
| BR-UC4-02 | Bàn chuyển về “Trống” khi chủ quán xác nhận bàn trống |
| BR-UC4-03 | “Số bàn” không được để trống |
| BR-UC4-04 | Số bàn là duy nhất trong các bàn đang có trong sơ đồ (không tính bàn đã xóa) |
| BR-UC4-05 | Mỗi bàn có một mã QR riêng gắn sẵn số bàn |
| BR-UC4-06 | Bàn mới mặc định ở trạng thái “Trống” |
| BR-UC4-07 | Bàn và mã QR được tạo cùng nhau |
| BR-UC4-08 | Chỉ được xóa bàn ở trạng thái “Trống” |
| BR-UC4-09 | Nút “Xóa bàn” chỉ hiển thị ở bàn có trạng thái “Trống” |
| BR-UC4-10 | Hệ thống chỉ đánh dấu xóa bàn, đơn cũ vẫn giữ số bàn |
| BR-UC4-11 | Nút “Xác nhận bàn trống” chỉ hiển thị với bàn ở trạng thái “Đang phục vụ” |

*Bảng 14. Business rules của use case “Quản lý bàn”*

### **Xem trạng thái bàn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_4.1</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xem trạng thái bàn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xem trạng thái các bàn để biết bàn nào trống hay đang phục vụ</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Bàn”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Hệ thống hiển thị sơ đồ bàn kèm trạng thái từng bàn</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Bàn”</p>
<p>2. Hệ thống hiển thị sơ đồ bàn gồm số bàn và trạng thái của từng bàn theo 2 trạng thái: “Trống”, “Đang phục vụ”</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>2a. Hệ thống truy xuất dữ liệu không thành công</p>
<p>2a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p>
<p>2b. Chưa có bàn nào trong hệ thống</p>
<p>2b1. Hệ thống hiển thị thông báo “Chưa có bàn nào”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Bàn chuyển sang “Đang phục vụ” khi khách gửi đơn</p>
<p>BR02. Bàn chuyển về “Trống” khi chủ quán xác nhận bàn trống</p></td>
</tr>
</tbody>
</table>

*Bảng 15. Đặc tả use case “Xem trạng thái bàn”*

**Sơ đồ Activity Diagram**

<img src="media/image12.png" style="width:6.10236in;height:4.30755in" />

*Hình 14. Sơ đồ activity diagram “Xem trạng thái bàn”*

### **Thêm bàn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_4.2</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Thêm bàn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn thêm bàn mới vào sơ đồ bàn</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Bàn”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Bàn mới được lưu với trạng thái “Trống”</p>
<p>Mã QR riêng gắn sẵn số bàn được tạo cho bàn</p>
<p>Mã QR của bàn được hiển thị để chủ quán tải về</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Bàn”</p>
<p>2. Hệ thống hiển thị sơ đồ bàn</p>
<p>3. Chủ quán chọn “Thêm bàn”</p>
<p>4. Hệ thống hiển thị màn hình thêm bàn</p>
<p>5. Chủ quán nhập “Số bàn”</p>
<p>6. Chủ quán nhấn “Lưu”</p>
<p>7. Hệ thống kiểm tra “Số bàn”</p>
<p>8. Hệ thống lưu bàn mới với trạng thái “Trống” và tạo mã QR riêng gắn số bàn</p>
<p>9. Hệ thống đồng thời hiển thị thông báo “Thêm bàn thành công”, mã QR của bàn kèm nút “Tải mã QR” và cập nhật sơ đồ bàn</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>9a. Chủ quán nhấn “Tải mã QR”</p>
<p>9a1. Hệ thống tải tệp mã QR của bàn về thiết bị.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>7a. Chủ quán bỏ trống trường “Số bàn”</p>
<p>7a1. Hệ thống hiển thị thông báo “Không được để trống!” ngay dưới trường “Số bàn”.</p>
<p>UC quay lại bước 5.</p>
<p>7b. “Số bàn” đã tồn tại</p>
<p>7b1. Hệ thống hiển thị thông báo “Số bàn đã tồn tại!” ngay dưới trường “Số bàn”.</p>
<p>UC quay lại bước 5.</p>
<p>8a. Hệ thống lưu bàn hoặc tạo mã QR không thành công</p>
<p>8a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. “Số bàn” không được để trống</p>
<p>BR02. Số bàn là duy nhất trong các bàn đang có trong sơ đồ (không tính bàn đã xóa)</p>
<p>BR03. Mỗi bàn có một mã QR riêng gắn sẵn số bàn</p>
<p>BR04. Bàn mới mặc định ở trạng thái “Trống”</p>
<p>BR05. Bàn và mã QR được tạo cùng nhau</p></td>
</tr>
</tbody>
</table>

*Bảng 16. Đặc tả use case “Thêm bàn”*

**Sơ đồ Activity Diagram**

<img src="media/image13.png" style="width:5.48795in;height:7.87401in" />

*Hình 15. Sơ đồ activity diagram “Thêm bàn”*

### **Xóa bàn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_4.3</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xóa bàn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xóa bàn khỏi sơ đồ bàn</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Bàn”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Bàn tồn tại trong sơ đồ bàn và đang ở trạng thái “Trống”</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Bàn bị xóa khỏi sơ đồ bàn</p>
<p>Mã QR của bàn không còn sử dụng được</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Bàn”</p>
<p>2. Hệ thống hiển thị sơ đồ bàn</p>
<p>3. Chủ quán chọn bàn trống cần xóa</p>
<p>4. Hệ thống hiển thị thông tin bàn kèm nút “Xóa bàn”</p>
<p>5. Chủ quán nhấn “Xóa bàn”</p>
<p>6. Hệ thống hiển thị thông báo xác nhận “Bạn có chắc chắn muốn xóa bàn này không?”</p>
<p>7. Chủ quán nhấn “Xóa”</p>
<p>8. Hệ thống đánh dấu bàn đã xóa và vô hiệu hóa mã QR của bàn</p>
<p>9. Hệ thống đồng thời hiển thị thông báo “Xóa bàn thành công” và cập nhật sơ đồ bàn</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>7a. Chủ quán nhấn “Hủy”</p>
<p>7a1. Hệ thống giữ nguyên bàn.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>8a. Hệ thống lưu không thành công</p>
<p>8a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Chỉ được xóa bàn ở trạng thái “Trống”</p>
<p>BR02. Nút “Xóa bàn” chỉ hiển thị ở bàn có trạng thái “Trống”</p>
<p>BR03. Hệ thống chỉ đánh dấu xóa bàn, đơn cũ vẫn giữ số bàn</p></td>
</tr>
</tbody>
</table>

*Bảng 17. Đặc tả use case “Xóa bàn”*

**Sơ đồ Activity Diagram**

<img src="media/image14.png" style="width:6.10236in;height:7.66307in" />

*Hình 16. Sơ đồ activity diagram “Xóa bàn”*

### **Cập nhật trạng thái bàn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_4.4</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Cập nhật trạng thái bàn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xác nhận bàn trống sau khi khách rời đi để bàn được đưa về trạng thái “Trống”</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Bàn”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Bàn tồn tại trong sơ đồ bàn</p>
<p>Bàn đang ở trạng thái “Đang phục vụ”</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Bàn được chuyển về trạng thái “Trống” và sơ đồ bàn được cập nhật</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Bàn”</p>
<p>2. Hệ thống hiển thị sơ đồ bàn</p>
<p>3. Chủ quán chọn bàn đang ở trạng thái “Đang phục vụ”</p>
<p>4. Hệ thống hiển thị thông tin bàn kèm nút “Xác nhận bàn trống”</p>
<p>5. Chủ quán nhấn “Xác nhận bàn trống”</p>
<p>6. Hệ thống chuyển trạng thái bàn về “Trống” và lưu</p>
<p>7. Hệ thống đồng thời hiển thị thông báo “Đã đưa bàn về trạng thái Trống” và cập nhật sơ đồ bàn</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>6a. Hệ thống lưu không thành công</p>
<p>6a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Nút “Xác nhận bàn trống” chỉ hiển thị với bàn ở trạng thái “Đang phục vụ”</p></td>
</tr>
</tbody>
</table>

*Bảng 18. Đặc tả use case “Cập nhật trạng thái bàn”*

**Sơ đồ Activity Diagram**

<img src="media/image15.png" style="width:5.84739in;height:6.93322in" />

*Hình 17. Sơ đồ activity diagram “Cập nhật trạng thái bàn”*

