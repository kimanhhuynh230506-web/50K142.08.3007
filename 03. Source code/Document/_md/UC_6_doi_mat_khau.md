## Use case “Đổi mật khẩu”

Cho phép chủ quán đổi mật khẩu đăng nhập để bảo mật dữ liệu kinh doanh.

### **Business rules**

|  |  |
|----|----|
| **ID** | **Business rules** |
| BR-UC6-01 | “Mật khẩu cũ”, “Mật khẩu mới” và “Nhập lại mật khẩu mới” không được để trống |
| BR-UC6-02 | “Mật khẩu cũ” phải đúng với mật khẩu hiện tại của chủ quán |
| BR-UC6-03 | “Mật khẩu mới” và “Nhập lại mật khẩu mới” phải giống nhau |

*Bảng 23. Business rules của use case “Đổi mật khẩu”*

### **Đổi mật khẩu**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_6</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Đổi mật khẩu</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn đổi mật khẩu đăng nhập để bảo mật tài khoản</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Đổi mật khẩu”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Mật khẩu mới được lưu vào hệ thống</p>
<p>Hệ thống chuyển chủ quán về màn hình đăng nhập</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Đổi mật khẩu”</p>
<p>2. Hệ thống hiển thị màn hình đổi mật khẩu</p>
<p>3. Chủ quán nhập “Mật khẩu cũ”, “Mật khẩu mới”, “Nhập lại mật khẩu mới”</p>
<p>4. Chủ quán nhấn “Lưu”</p>
<p>5. Hệ thống kiểm tra thông tin đã nhập</p>
<p>6. Hệ thống cập nhật mật khẩu mới</p>
<p>7. Hệ thống đồng thời hiển thị thông báo “Đổi mật khẩu thành công!” và chuyển về màn hình đăng nhập</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>5a. Chủ quán để trống một trong ba trường</p>
<p>5a1. Hệ thống hiển thị thông báo “Không được để trống!”.</p>
<p>UC quay lại bước 3.</p>
<p>5b. Mật khẩu cũ không đúng</p>
<p>5b1. Hệ thống hiển thị thông báo “Mật khẩu cũ không đúng!”.</p>
<p>UC quay lại bước 3.</p>
<p>5c. Mật khẩu mới và mật khẩu nhập lại không giống nhau</p>
<p>5c1. Hệ thống hiển thị thông báo “Mật khẩu mới và mật khẩu nhập lại không giống nhau!”.</p>
<p>UC quay lại bước 3.</p>
<p>6a. Hệ thống lưu không thành công</p>
<p>6a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. “Mật khẩu cũ”, “Mật khẩu mới” và “Nhập lại mật khẩu mới” không được để trống</p>
<p>BR02. “Mật khẩu cũ” phải đúng với mật khẩu hiện tại của chủ quán</p>
<p>BR03. “Mật khẩu mới” và “Nhập lại mật khẩu mới” phải giống nhau</p></td>
</tr>
</tbody>
</table>

*Bảng 24. Đặc tả use case “Đổi mật khẩu”*

**Sơ đồ Activity Diagram**

<img src="media/image20.png" style="width:5.43947in;height:7.87401in" />

*Hình 22. Sơ đồ activity diagram “Đổi mật khẩu”*

