## Use case “Đăng xuất”

Cho phép chủ quán đăng xuất khỏi hệ thống.

### **Business rules**

|           |                    |
|-----------|--------------------|
| **ID**    | **Business rules** |
| BR-UC8-01 | N/A                |

*Bảng 28. Business rules của use case “Đăng xuất”*

### **Đăng xuất**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_8</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Đăng xuất</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là chủ quán, tôi muốn đăng xuất khỏi hệ thống để kết thúc phiên làm việc</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Chủ quán</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Chủ quán chọn “Đăng xuất”</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Chủ quán đã đăng nhập thành công vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Phiên đăng nhập của chủ quán kết thúc</p>
<p>Hệ thống hiển thị màn hình đăng nhập</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Chủ quán chọn “Đăng xuất”</p>
<p>2. Hệ thống hiển thị “Bạn có muốn đăng xuất không?”</p>
<p>3. Chủ quán chọn “Có”</p>
<p>4. Hệ thống kết thúc phiên đăng nhập của chủ quán</p>
<p>5. Hệ thống hiển thị màn hình đăng nhập</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>3a. Chủ quán không chọn “Có”</p>
<p>3a1. Hệ thống giữ nguyên màn hình hiện tại.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>4a. Hệ thống kết thúc phiên không thành công</p>
<p>4a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>N/A</p></td>
</tr>
</tbody>
</table>

*Bảng 29. Đặc tả use case “Đăng xuất”*

**Sơ đồ Activity Diagram**

<img src="media/image24.png" style="width:4.93527in;height:4.57345in" />

*Hình 26. Sơ đồ activity diagram “Đăng xuất”*

