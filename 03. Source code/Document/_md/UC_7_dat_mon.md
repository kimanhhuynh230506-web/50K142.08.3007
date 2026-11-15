## Use case “Đặt món”

Cho phép khách hàng quét mã QR tại bàn, xem menu và tạo đơn gọi món.

<img src="media/image21.png" style="width:6.5in;height:4.37569in" />

*Hình 23. Sơ đồ Use Case phân rã chức năng Đặt món (khách hàng)*

### **Business rules**

|  |  |
|----|----|
| **ID** | **Business rules** |
| BR-UC7-01 | Món đang ẩn hoặc đã xóa không hiển thị cho khách hàng |
| BR-UC7-02 | Mỗi đơn gắn với một bàn do mã QR xác định |
| BR-UC7-03 | Tổng tiền bằng tổng (giá x số lượng) theo giá tại thời điểm đặt |
| BR-UC7-04 | Mã QR ngân hàng kèm số tiền chính xác của đơn để khách hàng đỡ nhầm lẫn; nội dung chuyển khoản gồm số bàn |
| BR-UC7-05 | Doanh thu chỉ được tính khi đơn ở trạng thái “Đã xác nhận thanh toán”, tức sau khi chủ quán xác nhận đã nhận tiền |
| BR-UC7-06 | Khách hàng được tạo thêm đơn mới bất cứ lúc nào sau khi gửi đơn; mỗi đơn là một đơn riêng và bắt đầu ở trạng thái “Chưa xác nhận thanh toán” |
| BR-UC7-07 | Hệ thống không tự xác minh giao dịch chuyển khoản; chủ quán tự kiểm tra tiền vào tài khoản rồi xác nhận |
| BR-UC7-08 | “Ghi chú” không bắt buộc, tối đa 200 ký tự, áp dụng cho cả đơn |
| BR-UC7-09 | Hệ thống không lưu minh chứng chuyển khoản; lời nhắc chỉ để khách tự giữ lại |

*Bảng 25. Business rules của use case “Đặt món”*

### **Xem menu**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_7.1</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Xem menu</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là khách hàng, tôi muốn quét mã QR tại bàn để xem menu</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Khách hàng</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Khách hàng quét mã QR tại bàn bằng điện thoại</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Bàn có mã QR còn hiệu lực</p>
<p>Khách hàng truy cập vào hệ thống</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Menu được hiển thị trên trình duyệt của khách hàng</p>
<p>Hệ thống nhận biết số bàn của khách hàng</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td><p>1. Khách hàng quét mã QR tại bàn bằng điện thoại</p>
<p>2. Hệ thống kiểm tra mã QR hợp lệ</p>
<p>3. Hệ thống hiển thị menu gồm hình ảnh minh họa, tên món, giá và khu vực “Món đề cử”</p>
<p>4. Khách hàng xem menu</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>N/A</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td><p>2a. Mã QR không hợp lệ hoặc bàn đã bị xóa</p>
<p>2a1. Hệ thống hiển thị thông báo “Mã QR không hợp lệ”.</p>
<p>UC kết thúc.</p>
<p>3a. Hệ thống truy xuất dữ liệu menu không thành công</p>
<p>3a1. Hệ thống hiển thị thông báo “Có lỗi xảy ra, vui lòng thử lại!”.</p>
<p>UC kết thúc.</p>
<p>3b. Menu chưa có món nào đang hiển thị</p>
<p>3b1. Hệ thống hiển thị thông báo “Menu chưa có món nào”.</p>
<p>UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Món đang ẩn hoặc đã xóa không hiển thị cho khách hàng</p></td>
</tr>
</tbody>
</table>

*Bảng 26. Đặc tả use case “Xem menu”*

**Sơ đồ Activity Diagram**

<img src="media/image22.png" style="width:5.60439in;height:5.56248in" />

*Hình 24. Sơ đồ activity diagram “Xem menu”*

### **Tạo đơn**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<tbody>
<tr>
<td><p>Use case ID</p></td>
<td><p>UC_7.2</p></td>
</tr>
<tr>
<td><p>Use case name</p></td>
<td><p>Tạo đơn</p></td>
</tr>
<tr>
<td><p>Description</p></td>
<td><p>Là khách hàng, tôi muốn chọn món, số lượng và phương thức thanh toán</p></td>
</tr>
<tr>
<td><p>Actors</p></td>
<td><p>Khách hàng</p></td>
</tr>
<tr>
<td><p>Triggers</p></td>
<td><p>Khách hàng chọn món trên menu</p></td>
</tr>
<tr>
<td><p>Pre-conditions</p></td>
<td><p>Khách hàng đã quét mã QR</p></td>
</tr>
<tr>
<td><p>Post-conditions</p></td>
<td><p>Đơn được tạo và lưu gồm số bàn, món, số lượng, ghi chú, thời gian, phương thức thanh toán và trạng thái “Chưa xác nhận thanh toán”</p>
<p>Bàn chuyển sang trạng thái “Đang phục vụ”</p>
<p>Chủ quán nhận được thông báo đơn mới</p>
<p>Nếu chọn chuyển khoản: khách hàng đã được hiển thị mã QR kèm số tiền để chuyển khoản</p>
<p>Nếu chọn tiền mặt: khách hàng biết sẽ trả tiền khi nhận món tại bàn</p></td>
</tr>
<tr>
<td><p>Main flow</p></td>
<td style="text-align: left;"><p>1. Khách hàng chọn món trên menu<br />
2. Khách hàng chọn số lượng cho từng món<br />
3. Khách hàng nhấn “Tiếp tục”<br />
4. Hệ thống kiểm tra đơn có ít nhất một món với số lượng lớn hơn 0<br />
5. Khách hàng nhập “Ghi chú” cho đơn (nếu cần)<br />
6. Hệ thống tính và hiển thị tổng tiền của đơn<br />
7. Hệ thống hiển thị hai phương thức thanh toán “Chuyển khoản” và “Tiền mặt”<br />
8. Khách hàng chọn phương thức thanh toán “Chuyển khoản”<br />
9. Hệ thống ghi nhận phương thức thanh toán đã chọn<br />
10. Hệ thống hiển thị mã QR ngân hàng kèm số tiền của đơn và lời nhắc “Sau khi chuyển khoản, nhấn Hoàn tất. Vui lòng chụp lại giao dịch để đối chiếu khi cần thiết”<br />
11. Khách hàng mở ứng dụng ngân hàng, quét mã QR và chuyển khoản<br />
12. Khách hàng nhấn “Hoàn tất”<br />
13. Hệ thống tạo đơn gồm số bàn, món, số lượng, ghi chú, thời gian và phương thức thanh toán<br />
14. Hệ thống lưu đơn với trạng thái “Chưa xác nhận thanh toán”<br />
15. Hệ thống đồng thời chuyển bàn sang trạng thái “Đang phục vụ”, thông báo đơn mới cho chủ quán và hiển thị thông báo “Đặt món thành công”</p></td>
</tr>
<tr>
<td><p>Alternative flows</p></td>
<td><p>8a. Khách hàng chọn phương thức thanh toán “Tiền mặt”</p>
<p>8a1. Hệ thống ghi nhận phương thức thanh toán đã chọn.</p>
<p>8a2. Hệ thống hiển thị thông báo “Chờ thu tiền sau khi bưng nước ra”.</p>
<p>8a3. Khách hàng nhấn “Hoàn tất”.</p>
<p>UC tiếp tục bước 13.</p></td>
</tr>
<tr>
<td><p>Exception flows</p></td>
<td style="text-align: left;"><p>4a. Khách hàng chưa chọn món nào hoặc số lượng không hợp lệ<br />
4a1. Hệ thống hiển thị thông báo “Vui lòng chọn ít nhất một món”.<br />
UC quay lại bước 1.<br />
14a. Hệ thống lưu đơn không thành công<br />
14a1. Hệ thống hiển thị thông báo “Đặt món không thành công, vui lòng thử lại!”.<br />
UC kết thúc.</p></td>
</tr>
<tr>
<td><p>Business rules</p></td>
<td><p>BR01. Mỗi đơn gắn với một bàn do mã QR xác định</p>
<p>BR02. Tổng tiền bằng tổng (giá x số lượng) theo giá tại thời điểm đặt</p>
<p>BR03. Mã QR ngân hàng kèm số tiền chính xác của đơn để khách hàng đỡ nhầm lẫn; nội dung chuyển khoản gồm số bàn</p>
<p>BR04. Doanh thu chỉ được tính khi đơn ở trạng thái “Đã xác nhận thanh toán”, tức sau khi chủ quán xác nhận đã nhận tiền</p>
<p>BR05. Khách hàng được tạo thêm đơn mới bất cứ lúc nào sau khi gửi đơn; mỗi đơn là một đơn riêng và bắt đầu ở trạng thái “Chưa xác nhận thanh toán”</p>
<p>BR06. Hệ thống không tự xác minh giao dịch chuyển khoản; chủ quán tự kiểm tra tiền vào tài khoản rồi xác nhận</p>
<p>BR07. “Ghi chú” không bắt buộc, tối đa 200 ký tự, áp dụng cho cả đơn</p>
<p>BR08. Hệ thống không lưu minh chứng chuyển khoản; lời nhắc chỉ để khách tự giữ lại</p></td>
</tr>
</tbody>
</table>

*Bảng 27. Đặc tả use case “Tạo đơn”*

**Sơ đồ Activity Diagram**

<img src="media/image23.png" style="width:4.58971in;height:8.08848in" />

*Hình 25. Sơ đồ activity diagram “Tạo đơn”*

