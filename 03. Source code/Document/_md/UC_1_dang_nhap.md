## Use case “Đăng nhập”

Cho phép chủ quán đăng nhập vào hệ thống để quản lý việc bán hàng.

### **Business rules**

|           |                                                   |
|-----------|---------------------------------------------------|
| **ID**    | **Business rules**                                |
| BR-UC1-01 | “Tên đăng nhập” và “Mật khẩu” không được để trống |

*Bảng 3. Business rules của use case “Đăng nhập”*

### **Đăng nhập**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_1</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Đăng nhập</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn đăng nhập vào hệ thống để quản lý việc bán hàng</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán truy cập đến trang web của hệ thống</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán có thể truy cập đến trang web</p>
<p>Chủ quán đã có tài khoản trong hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Chủ quán đăng nhập vào hệ thống thành công</p>
<p>Hệ thống hiển thị màn hình Trang chủ</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán truy cập đến trang web của hệ thống</p>
<p>2. Hệ thống hiển thị màn hình đăng nhập</p>
<p>3. Chủ quán nhập “Tên đăng nhập” và “Mật khẩu”</p>
<p>4. Chủ quán nhấn “Đăng nhập”</p>
<p>5. Hệ thống kiểm tra thông tin đã nhập</p>
<p>6. Hệ thống xác thực thông tin đăng nhập</p>
<p>7. Hệ thống hiển thị màn hình Trang chủ sau khi xác thực thông tin đăng nhập hợp lệ</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>5a. Chủ quán bỏ trống trường “Tên đăng nhập” hoặc “Mật khẩu”</p>
<p>5a1. Hệ thống hiển thị thông báo “Không được để trống!” ngay dưới trường bị bỏ trống</p>
<p>UC quay lại bước 3.</p>
<p>6a. Hệ thống xác thực thông tin đăng nhập không hợp lệ</p>
<p>6a1. Hiển thị thông báo “Đăng nhập không thành công!” tại màn hình đăng nhập và kết thúc</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. “Tên đăng nhập” và “Mật khẩu” không được để trống</p></td>
</tr>
</tbody>
</table>

*Bảng 4. Đặc tả use case “Đăng nhập”*

**Sơ đồ Activity Diagram**

<img src="media/image1.png" style="width:5.80005in;height:5.71501in" />

*Hình 3. Sơ đồ activity diagram “Đăng nhập”*

