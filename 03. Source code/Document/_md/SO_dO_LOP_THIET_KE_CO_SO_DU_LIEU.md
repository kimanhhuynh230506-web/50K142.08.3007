# THIẾT KẾ SƠ ĐỒ LỚP

## Sơ đồ lớp

<img src="media/image1.png" style="width:6.5in;height:4.40117in" />

*Hình 27. Sơ đồ lớp hệ thống quản lý bán hàng Cà phê 458*

# THIẾT KẾ CƠ SỞ DỮ LIỆU

## Thiết kế logic cơ sở dữ liệu

### **Chuyển sơ đồ thành các bảng**

- ChuQuan (**tenDangNhap**, matKhau)

- Ban (**maBan**, tenDangNhap (FK), soBan, trangThai, maQR, daXoa)

- Mon (**maMon**, tenMon, giaBan, hinhAnh, trangThai, daXoa)

- DonHang (**maDonHang**, maBan (FK), thoiGianDat, phuongThucThanhToan, trangThai, ghiChu, thoiGianGiaoDich, daXoa)

- ChiTietDon (**maDonHang (FK), maMon (FK)**, tenMon, gia, soLuong)

### **Chuẩn hóa các bảng**

- ChuQuan (**tenDangNhap**, matKhau)

- Ban (**maBan**, tenDangNhap (FK), soBan, trangThai, maQR, daXoa)

- Mon (**maMon**, tenMon, giaBan, hinhAnh, trangThai, daXoa)

- DonHang (**maDonHang**, maBan (FK), thoiGianDat, phuongThucThanhToan, trangThai, ghiChu, thoiGianGiaoDich, daXoa)

- ChiTietDon (**maDonHang (FK), maMon (FK)**, tenMon, gia, soLuong)

### **Sơ đồ quan hệ**

<img src="media/image2.png" style="width:6.5in;height:2.99701in" />

*Hình 28. Sơ đồ quan hệ cơ sở dữ liệu*

## Thiết kế vật lý cơ sở dữ liệu

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 23%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>STT</strong></th>
<th style="text-align: center;"><strong>Tên cột</strong></th>
<th style="text-align: center;"><strong>Kiểu dữ liệu</strong></th>
<th style="text-align: center;"><strong>Ràng buộc</strong></th>
<th style="text-align: center;"><strong>Ghi chú</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>ChuQuan</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">tenDangNhap</td>
<td style="text-align: center;">Varchar(50)</td>
<td style="text-align: center;">PK</td>
<td style="text-align: center;">Chỉ gồm ký tự không dấu</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">matKhau</td>
<td style="text-align: center;">Varchar(100)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="5" style="text-align: center;"><strong>Ban</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">maBan</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">PK, IDENTITY</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">tenDangNhap</td>
<td style="text-align: center;">Varchar(50)</td>
<td style="text-align: center;">FK</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">soBan</td>
<td style="text-align: center;">Varchar(10)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">trangThai</td>
<td style="text-align: center;">Nvarchar(20)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;">“Trống” hoặc “Đang phục vụ”</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">maQR</td>
<td style="text-align: center;">Varchar(255)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;">Nội dung mã QR riêng của bàn</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">daXoa</td>
<td style="text-align: center;">Bit</td>
<td style="text-align: center;">NOT NULL, DEFAULT 0</td>
<td style="text-align: center;">1: bàn đã xóa</td>
</tr>
<tr>
<td colspan="5" style="text-align: center;"><strong>Mon</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">maMon</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">PK, IDENTITY</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">tenMon</td>
<td style="text-align: center;">Nvarchar(50)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">giaBan</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">NOT NULL, CHECK (giaBan &gt; 0)</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">hinhAnh</td>
<td style="text-align: center;">Varchar(255)</td>
<td style="text-align: center;">NULL</td>
<td style="text-align: center;">Để trống thì dùng hình mặc định</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">trangThai</td>
<td style="text-align: center;">Nvarchar(20)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;">“Hiển thị” hoặc “Ẩn”</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">daXoa</td>
<td style="text-align: center;">Bit</td>
<td style="text-align: center;">NOT NULL, DEFAULT 0</td>
<td style="text-align: center;">1: món đã xóa</td>
</tr>
<tr>
<td colspan="5" style="text-align: center;"><strong>DonHang</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">maDonHang</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">PK, IDENTITY</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">maBan</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">FK</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">thoiGianDat</td>
<td style="text-align: center;">Datetime</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">phuongThucThanhToan</td>
<td style="text-align: center;">Nvarchar(20)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;">“Chuyển khoản” hoặc “Tiền mặt”</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">trangThai</td>
<td style="text-align: center;">Nvarchar(30)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;">“Chưa xác nhận thanh toán” hoặc “Đã xác nhận thanh toán”</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">ghiChu</td>
<td style="text-align: center;">Nvarchar(200)</td>
<td style="text-align: center;">NULL</td>
<td style="text-align: center;">Tối đa 200 ký tự</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">thoiGianGiaoDich</td>
<td style="text-align: center;">Datetime</td>
<td style="text-align: center;">NULL</td>
<td style="text-align: center;">Ghi nhận khi chủ quán xác nhận đã nhận tiền</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;">daXoa</td>
<td style="text-align: center;">Bit</td>
<td style="text-align: center;">NOT NULL, DEFAULT 0</td>
<td style="text-align: center;">1: đơn đã xóa</td>
</tr>
<tr>
<td colspan="5" style="text-align: center;"><strong>ChiTietDon</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">maDonHang</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">PK, FK</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">maMon</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">PK, FK</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">tenMon</td>
<td style="text-align: center;">Nvarchar(50)</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;">Tên món tại thời điểm đặt</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">gia</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">NOT NULL</td>
<td style="text-align: center;">Giá món tại thời điểm đặt</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">soLuong</td>
<td style="text-align: center;">Int</td>
<td style="text-align: center;">NOT NULL, CHECK (soLuong &gt; 0)</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

*Bảng 32. Thiết kế vật lý cơ sở dữ liệu*

## Ước lượng dung lượng lưu trữ

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Tên cột / chỉ tiêu</strong></th>
<th style="text-align: center;"><strong>Dung lượng (byte)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: center;"><strong>Bảng ChuQuan</strong></td>
</tr>
<tr>
<td style="text-align: center;">tenDangNhap</td>
<td style="text-align: center;">50</td>
</tr>
<tr>
<td style="text-align: center;">matKhau</td>
<td style="text-align: center;">100</td>
</tr>
<tr>
<td style="text-align: center;">Tổng</td>
<td style="text-align: center;">150</td>
</tr>
<tr>
<td style="text-align: center;">Overhead</td>
<td style="text-align: center;">30%</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ cho 1 bản ghi</td>
<td style="text-align: center;">195</td>
</tr>
<tr>
<td style="text-align: center;">Số lượng bản ghi khởi tạo ban đầu</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ ban đầu</td>
<td style="text-align: center;">195</td>
</tr>
<tr>
<td style="text-align: center;">Ước lượng dữ liệu gia tăng/tháng</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: center;">Dung lượng lưu trữ sau 1 năm</td>
<td style="text-align: center;">195</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><strong>Bảng Ban</strong></td>
</tr>
<tr>
<td style="text-align: center;">maBan</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">tenDangNhap</td>
<td style="text-align: center;">50</td>
</tr>
<tr>
<td style="text-align: center;">soBan</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">trangThai</td>
<td style="text-align: center;">40</td>
</tr>
<tr>
<td style="text-align: center;">maQR</td>
<td style="text-align: center;">255</td>
</tr>
<tr>
<td style="text-align: center;">daXoa</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">Tổng</td>
<td style="text-align: center;">360</td>
</tr>
<tr>
<td style="text-align: center;">Overhead</td>
<td style="text-align: center;">30%</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ cho 1 bản ghi</td>
<td style="text-align: center;">468</td>
</tr>
<tr>
<td style="text-align: center;">Số lượng bản ghi khởi tạo ban đầu</td>
<td style="text-align: center;">20</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ ban đầu</td>
<td style="text-align: center;">9360</td>
</tr>
<tr>
<td style="text-align: center;">Ước lượng dữ liệu gia tăng/tháng</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">Dung lượng lưu trữ sau 1 năm</td>
<td style="text-align: center;">14976</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><strong>Bảng Mon</strong></td>
</tr>
<tr>
<td style="text-align: center;">maMon</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">tenMon</td>
<td style="text-align: center;">100</td>
</tr>
<tr>
<td style="text-align: center;">giaBan</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">hinhAnh</td>
<td style="text-align: center;">255</td>
</tr>
<tr>
<td style="text-align: center;">trangThai</td>
<td style="text-align: center;">40</td>
</tr>
<tr>
<td style="text-align: center;">daXoa</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">Tổng</td>
<td style="text-align: center;">404</td>
</tr>
<tr>
<td style="text-align: center;">Overhead</td>
<td style="text-align: center;">30%</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ cho 1 bản ghi</td>
<td style="text-align: center;">525</td>
</tr>
<tr>
<td style="text-align: center;">Số lượng bản ghi khởi tạo ban đầu</td>
<td style="text-align: center;">50</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ ban đầu</td>
<td style="text-align: center;">26250</td>
</tr>
<tr>
<td style="text-align: center;">Ước lượng dữ liệu gia tăng/tháng</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">Dung lượng lưu trữ sau 1 năm</td>
<td style="text-align: center;">45150</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><strong>Bảng DonHang</strong></td>
</tr>
<tr>
<td style="text-align: center;">maDonHang</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">maBan</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">thoiGianDat</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">phuongThucThanhToan</td>
<td style="text-align: center;">40</td>
</tr>
<tr>
<td style="text-align: center;">trangThai</td>
<td style="text-align: center;">60</td>
</tr>
<tr>
<td style="text-align: center;">ghiChu</td>
<td style="text-align: center;">400</td>
</tr>
<tr>
<td style="text-align: center;">thoiGianGiaoDich</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">daXoa</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">Tổng</td>
<td style="text-align: center;">525</td>
</tr>
<tr>
<td style="text-align: center;">Overhead</td>
<td style="text-align: center;">30%</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ cho 1 bản ghi</td>
<td style="text-align: center;">682</td>
</tr>
<tr>
<td style="text-align: center;">Số lượng bản ghi khởi tạo ban đầu</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ ban đầu</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: center;">Ước lượng dữ liệu gia tăng/tháng</td>
<td style="text-align: center;">1800</td>
</tr>
<tr>
<td style="text-align: center;">Dung lượng lưu trữ sau 1 năm</td>
<td style="text-align: center;">14731200</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><strong>Bảng ChiTietDon</strong></td>
</tr>
<tr>
<td style="text-align: center;">maDonHang</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">maMon</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">tenMon</td>
<td style="text-align: center;">100</td>
</tr>
<tr>
<td style="text-align: center;">gia</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">soLuong</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">Tổng</td>
<td style="text-align: center;">116</td>
</tr>
<tr>
<td style="text-align: center;">Overhead</td>
<td style="text-align: center;">30%</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ cho 1 bản ghi</td>
<td style="text-align: center;">151</td>
</tr>
<tr>
<td style="text-align: center;">Số lượng bản ghi khởi tạo ban đầu</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: center;">Tổng dung lượng lưu trữ ban đầu</td>
<td style="text-align: center;">0</td>
</tr>
<tr>
<td style="text-align: center;">Ước lượng dữ liệu gia tăng/tháng</td>
<td style="text-align: center;">5400</td>
</tr>
<tr>
<td style="text-align: center;">Dung lượng lưu trữ sau 1 năm</td>
<td style="text-align: center;">9784800</td>
</tr>
</tbody>
</table>

*Bảng 33. Ước lượng dung lượng lưu trữ*
