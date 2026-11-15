## Use case “Quản lý menu”

Cho phép chủ quán xem danh sách món, thêm món, xóa món và cập nhật thông tin món.

<img src="media/image6.png" style="width:6.5in;height:4.23889in" />

*Hình 8. Sơ đồ Use Case phân rã chức năng Quản lý menu*

### **Business rules**

|  |  |
|----|----|
| **ID** | **Business rules** |
| BR-UC3-01 | Trạng thái món bao gồm hai trạng thái “Hiển thị” hoặc “Ẩn” |
| BR-UC3-02 | “Tên món” và “Giá bán” không được để trống |
| BR-UC3-03 | Tên món là duy nhất trong menu (không tính món đã xóa) |
| BR-UC3-04 | Giá bán là số lớn hơn 0 |
| BR-UC3-05 | Hình ảnh minh họa là tùy chọn, món không có hình thì dùng hình mặc định |
| BR-UC3-06 | Khi “Tên món” hoặc “Giá bán” không hợp lệ, hệ thống giữ nguyên hình ảnh minh họa đã chọn và chỉ báo lỗi tại trường sai |
| BR-UC3-07 | Hệ thống chỉ đánh dấu xóa, không xóa hẳn dữ liệu món |
| BR-UC3-08 | Đơn cũ vẫn giữ tên món và giá tại thời điểm đặt nên thống kê cũ không thay đổi |
| BR-UC3-09 | Món đã xóa không hiển thị cho khách hàng và trong danh sách quản lý menu |
| BR-UC3-10 | Giá mới chỉ áp dụng cho đơn tạo sau, đơn cũ giữ giá lúc đặt |
| BR-UC3-11 | Khi “Tên món” hoặc “Giá bán” không hợp lệ, hệ thống giữ nguyên hình ảnh và trạng thái đã chọn, chỉ báo lỗi tại trường sai |
| BR-UC3-12 | Chủ quán có thể sửa một hoặc nhiều thông tin (tên, giá, hình ảnh, trạng thái) trong cùng một lần cập nhật |

*Bảng 9. Business rules của use case “Quản lý menu”*

### **Xem danh sách món**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_3.1</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xem danh sách món</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xem danh sách món trong menu để biết tên món, giá.</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Menu”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Hệ thống hiển thị danh sách món</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Menu”</p>
<p>2. Hệ thống hiển thị danh sách món gồm tên món, giá, hình ảnh, trạng thái, nút “Cập nhật món” và “Xóa món”</p></td>
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
<p>2b. Menu chưa có món nào</p>
<p>2b1. Hệ thống hiển thị thông báo “Menu chưa có món nào”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Trạng thái món bao gồm hai trạng thái “Hiển thị” hoặc “Ẩn”</p></td>
</tr>
</tbody>
</table>

*Bảng 10. Đặc tả use case “Xem danh sách món”*

**Sơ đồ Activity Diagram**

<img src="media/image7.png" style="width:6.10236in;height:4.30755in" />

*Hình 9. Sơ đồ activity diagram “Xem danh sách món”*

### **Thêm món**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_3.2</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Thêm món</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn thêm món mới vào menu</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Menu”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Món mới được lưu vào hệ thống</p>
<p>Món mới xuất hiện trong danh sách món</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Menu”</p>
<p>2. Hệ thống hiển thị danh sách món</p>
<p>3. Chủ quán chọn “Thêm món”</p>
<p>4. Hệ thống hiển thị màn hình thêm món</p>
<p>5. Chủ quán nhập “Tên món” và “Giá bán”</p>
<p>6. Chủ quán chọn hình ảnh minh họa</p>
<p>7. Chủ quán nhấn “Lưu”</p>
<p>8. Hệ thống kiểm tra “Tên món” và “Giá bán”</p>
<p>9. Hệ thống lưu món mới</p>
<p>10. Hệ thống đồng thời hiển thị thông báo “Thêm món thành công” và cập nhật danh sách món</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>6a. Chủ quán không chọn hình ảnh minh họa</p>
<p>6a1. Hệ thống dùng hình ảnh mặc định cho món.</p>
<p>UC tiếp tục bước 7.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>8a. Chủ quán bỏ trống trường “Tên món”</p>
<p>8a1. Hệ thống hiển thị thông báo “Không được để trống!” ngay dưới trường “Tên món”.</p>
<p>UC quay lại bước 5.</p>
<p>8b. “Tên món” đã tồn tại trong menu</p>
<p>8b1. Hệ thống hiển thị thông báo “Tên món đã tồn tại!” ngay dưới trường “Tên món”.</p>
<p>UC quay lại bước 5.</p>
<p>8c. Chủ quán bỏ trống trường “Giá bán”</p>
<p>8c1. Hệ thống hiển thị thông báo “Không được để trống!” ngay dưới trường “Giá bán”.</p>
<p>UC quay lại bước 5.</p>
<p>8d. “Giá bán” không phải số lớn hơn 0</p>
<p>8d1. Hệ thống hiển thị thông báo “Giá bán phải là số lớn hơn 0!” ngay dưới trường “Giá bán”.</p>
<p>UC quay lại bước 5.</p>
<p>9a. Hệ thống lưu không thành công</p>
<p>9a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. “Tên món” và “Giá bán” không được để trống</p>
<p>BR02. Tên món là duy nhất trong menu (không tính món đã xóa)</p>
<p>BR03. Giá bán là số lớn hơn 0</p>
<p>BR04. Hình ảnh minh họa là tùy chọn, món không có hình thì dùng hình mặc định</p>
<p>BR05. Khi “Tên món” hoặc “Giá bán” không hợp lệ, hệ thống giữ nguyên hình ảnh minh họa đã chọn và chỉ báo lỗi tại trường sai</p>
<p>BR06. Món mới thêm mặc định ở trạng thái “Hiển thị”</p></td>
</tr>
</tbody>
</table>

*Bảng 11. Đặc tả use case “Thêm món”*

**Sơ đồ Activity Diagram**

<img src="media/image8.png" style="width:4.21168in;height:7.87401in" />

*Hình 10. Sơ đồ activity diagram “Thêm món”*

### **Xóa món**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_3.3</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xóa món</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn xóa món khỏi menu</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Menu”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Món tồn tại trong menu</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Món bị xóa khỏi menu, không còn hiển thị trong danh sách món và với khách hàng</p>
<p>Số liệu thống kê cũ và các đơn cũ không thay đổi</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Menu”</p>
<p>2. Hệ thống hiển thị danh sách món</p>
<p>3. Chủ quán nhấn “Xóa món” trên món cần xóa</p>
<p>4. Hệ thống hiển thị thông báo xác nhận “Bạn có chắc chắn muốn xóa món này không?”</p>
<p>5. Chủ quán nhấn “Xóa”</p>
<p>6. Hệ thống đánh dấu món đã xóa</p>
<p>7. Hệ thống lưu thay đổi</p>
<p>8. Hệ thống đồng thời hiển thị thông báo “Đã xóa món thành công” và cập nhật danh sách món</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>5a. Chủ quán nhấn “Hủy”</p>
<p>5a1. Hệ thống giữ nguyên món.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>7a. Hệ thống lưu không thành công</p>
<p>7a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Hệ thống chỉ đánh dấu xóa, không xóa hẳn dữ liệu món</p>
<p>BR02. Đơn cũ vẫn giữ tên món và giá tại thời điểm đặt nên thống kê cũ không thay đổi</p>
<p>BR03. Món đã xóa không hiển thị cho khách hàng và trong danh sách quản lý menu</p></td>
</tr>
</tbody>
</table>

*Bảng 12. Đặc tả use case “Xóa món”*

**Sơ đồ Activity Diagram**

<img src="media/image9.png" style="width:6.5in;height:7.99583in" />

*Hình 11. Sơ đồ activity diagram “Xóa món”*

### **Cập nhật món**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_3.4</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Cập nhật món</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn sửa tên, giá, hình ảnh hoặc bật, tắt hiển thị của món</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Menu”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p>
<p>Món tồn tại trong menu</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Thông tin món mới được lưu vào hệ thống</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Menu”</p>
<p>2. Hệ thống hiển thị danh sách món</p>
<p>3. Chủ quán nhấn “Cập nhật món” trên món cần cập nhật</p>
<p>4. Hệ thống hiển thị màn hình cập nhật món kèm thông tin hiện tại của món</p>
<p>5. Chủ quán sửa “Tên món”, “Giá bán”, hình ảnh minh họa, “Trạng thái” (“Hiển thị” hoặc “Ẩn”)</p>
<p>6. Chủ quán nhấn “Lưu”</p>
<p>7. Hệ thống kiểm tra “Tên món” và “Giá bán”</p>
<p>8. Hệ thống lưu thông tin món</p>
<p>9. Hệ thống đồng thời hiển thị thông báo “Cập nhật món thành công” và cập nhật danh sách món</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>7a. Chủ quán để trống trường “Tên món”</p>
<p>7a1. Hệ thống hiển thị thông báo “Không được để trống!” ngay dưới trường “Tên món”.</p>
<p>UC quay lại bước 5.</p>
<p>7b. “Tên món” trùng với món khác trong menu</p>
<p>7b1. Hệ thống hiển thị thông báo “Tên món đã tồn tại!” ngay dưới trường “Tên món”.</p>
<p>UC quay lại bước 5.</p>
<p>7c. Chủ quán để trống trường “Giá bán”</p>
<p>7c1. Hệ thống hiển thị thông báo “Không được để trống!” ngay dưới trường “Giá bán”.</p>
<p>UC quay lại bước 5.</p>
<p>7d. “Giá bán” không phải số lớn hơn 0</p>
<p>7d1. Hệ thống hiển thị thông báo “Giá bán phải là số lớn hơn 0!” ngay dưới trường “Giá bán”.</p>
<p>UC quay lại bước 5.</p>
<p>8a. Hệ thống lưu không thành công</p>
<p>8a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. “Tên món” và “Giá bán” không được để trống</p>
<p>BR02. Tên món là duy nhất trong menu (không tính món đã xóa)</p>
<p>BR03. Giá bán là số lớn hơn 0</p>
<p>BR04. Giá mới chỉ áp dụng cho đơn tạo sau, đơn cũ giữ giá lúc đặt</p>
<p>BR05. Khi “Tên món” hoặc “Giá bán” không hợp lệ, hệ thống giữ nguyên hình ảnh và trạng thái đã chọn, chỉ báo lỗi tại trường sai</p>
<p>BR06. Chủ quán có thể sửa một hoặc nhiều thông tin (tên, giá, hình ảnh, trạng thái) trong cùng một lần cập nhật</p></td>
</tr>
</tbody>
</table>

*Bảng 13. Đặc tả use case “Cập nhật món”*

**Sơ đồ Activity Diagram**

<img src="media/image10.png" style="width:5.40746in;height:7.87402in" />

*Hình 12. Sơ đồ activity diagram “Cập nhật món”*

