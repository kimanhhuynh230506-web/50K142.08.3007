# BỘ TEST CASE KIỂM THỬ BACK-END API — HỆ THỐNG QUẢN LÝ CÀ PHÊ 458

> **Tài liệu kiểm thử chất lượng phần mềm (QA Test Specification)**  
> **Áp dụng cho:** 23 RESTful API theo danh mục chuẩn `Back-End/Danh sách API.csv`  
> **Căn cứ tài liệu:** `Document/_md/UC_*.md`, `Document/_md/NFR_phi_chuc_nang.md`, `Document/.Agent/03_data_model.md`, `Document/.Agent/05_quyet_dinh_va_audit.md`  
> **Quy ước mã lỗi:** Chuẩn JSON `QĐ-21`: `{"error": {"code": "...", "message": "<thông báo nguyên văn>", "field": "<tên trường hoặc null>"}}`  
> **Môi trường khuyến nghị:** CSDL thử nghiệm độc lập (PostgreSQL/Supabase test), không chạy trên CSDL thật (`QĐ-08`).

---

## 1. MA TRẬN TỔNG HỢP VÀ ĐỘ BAO PHỦ 23 API (TRACEABILITY MATRIX)

| STT | Mã API | Method | Endpoint chuẩn | Phân hệ | Actor | Nguồn Use Case & Business Rules | Tổng số TC |
|:---:|:---|:---:|:---|:---|:---:|:---|:---:|
| 1 | `API-AUTH-01` | POST | `/api/v1/auth/login` | Xác thực (Auth) | Public | UC_1 \| BR-UC1-01, QĐ-01, QĐ-20 | 6 |
| 2 | `API-AUTH-02` | POST | `/api/v1/auth/logout` | Xác thực (Auth) | Chủ quán | UC_8 \| QĐ-01, QĐ-21 | 3 |
| 3 | `API-AUTH-03` | PUT | `/api/v1/auth/password` | Xác thực (Auth) | Chủ quán | UC_6 \| BR-UC6-01, 02, 03 | 6 |
| 4 | `API-CUST-01` | GET | `/api/v1/customer/menu` | Khách hàng (Customer) | Public (QR) | UC_7.1 \| BR-UC7-01, QĐ-18, QĐ-19 | 5 |
| 5 | `API-CUST-02` | POST | `/api/v1/customer/orders/preview` | Khách hàng (Customer) | Public (QR) | UC_7.2 \| BR-UC7-03, 04, QĐ-12, QĐ-22 | 5 |
| 6 | `API-CUST-03` | POST | `/api/v1/customer/orders` | Khách hàng (Customer) | Public (QR) | UC_7.2 \| BR-UC4-01, BR-UC7-03, 06, 08 | 6 |
| 7 | `API-ORD-01` | GET | `/api/v1/admin/orders` | Quản lý gọi món (Orders) | Chủ quán | UC_2.2 \| BR-UC2-04, 05, 07, QĐ-14 | 5 |
| 8 | `API-ORD-02` | GET | `/api/v1/admin/orders/{ma_don_hang}` | Quản lý gọi món (Orders) | Chủ quán | UC_2.2 \| QĐ-17, QĐ-22 | 4 |
| 9 | `API-ORD-03` | PATCH | `/api/v1/admin/orders/{ma_don_hang}/confirm-payment` | Quản lý gọi món (Orders) | Chủ quán | UC_2.1 \| BR-UC2-01, BR-UC2-02 | 4 |
| 10 | `API-ORD-04` | DELETE | `/api/v1/admin/orders/{ma_don_hang}` | Quản lý gọi món (Orders) | Chủ quán | UC_2.3 \| BR-UC2-07, 08, BR-UC2-09 | 4 |
| 11 | `API-NOTIF-01` | GET | `/api/v1/admin/notifications/unread-orders` | Thông báo (Notifications) | Chủ quán | QĐ-05, QĐ-24 | 3 |
| 12 | `API-MENU-01` | GET | `/api/v1/admin/menu` | Thực đơn (Menu) | Chủ quán | UC_3.1 \| BR-UC3-01, QĐ-19 | 4 |
| 13 | `API-MENU-02` | POST | `/api/v1/admin/menu` | Thực đơn (Menu) | Chủ quán | UC_3.2 \| BR-UC3-02, 03, 04, 05, BR06 | 7 |
| 14 | `API-MENU-03` | PUT | `/api/v1/admin/menu/{ma_mon}` | Thực đơn (Menu) | Chủ quán | UC_3.4 \| BR-UC3-03, 04, 10, 12 | 6 |
| 15 | `API-MENU-04` | DELETE | `/api/v1/admin/menu/{ma_mon}` | Thực đơn (Menu) | Chủ quán | UC_3.3 \| BR-UC3-07, 08, 09 | 4 |
| 16 | `API-MEDIA-01` | POST | `/api/v1/admin/menu/upload-image` | Tiện ích & Lưu trữ (Media) | Chủ quán | QĐ-06 \| NFR-05 | 4 |
| 17 | `API-TAB-01` | GET | `/api/v1/admin/tables` | Bàn ăn (Tables) | Chủ quán | UC_4.1 \| BR-UC4-06, NFR-04 | 4 |
| 18 | `API-TAB-02` | POST | `/api/v1/admin/tables` | Bàn ăn (Tables) | Chủ quán | UC_4.2 \| BR-UC4-03, 04, 05, 06, 07 | 6 |
| 19 | `API-TAB-03` | GET | `/api/v1/admin/tables/{ma_ban}/qr-image` | Bàn ăn (Tables) | Chủ quán | UC_4.2 (9a) \| QĐ-13 | 3 |
| 20 | `API-TAB-04` | DELETE | `/api/v1/admin/tables/{ma_ban}` | Bàn ăn (Tables) | Chủ quán | UC_4.3 \| BR-UC4-08, 09, 10 | 4 |
| 21 | `API-TAB-05` | PATCH | `/api/v1/admin/tables/{ma_ban}/empty` | Bàn ăn (Tables) | Chủ quán | UC_4.4 \| BR-UC4-02, 11 | 4 |
| 22 | `API-REP-01` | GET | `/api/v1/admin/reports/revenue` | Báo cáo Doanh thu (Reports) | Chủ quán | UC_5.1 \| BR-UC5-01, 02, 03, 04, 05 | 6 |
| 23 | `API-REP-02` | GET | `/api/v1/admin/reports/details` | Báo cáo Doanh thu (Reports) | Chủ quán | UC_5.2, 5.3 \| BR-UC5-06, 08, 09, 10, AUD-12 | 6 |
| **TỔNG** | **23 API** | | | | | | **110 Test Cases** |

---

## 2. ĐẶC TẢ CHI TIẾT TEST CASES TỪNG PHÂN HỆ

### PHÂN HỆ 1: XÁC THỰC (AUTHENTICATION)

#### 1. API-AUTH-01: Đăng nhập hệ thống (`POST /api/v1/auth/login`)
- **Mô tả:** Xác thực tên đăng nhập và mật khẩu của chủ quán, cấp JWT HS256 hạn 12h.
- **Header:** `Content-Type: application/json`

| Mã Test Case | Phân loại | Tiền điều kiện | Dữ liệu đầu vào (Payload) | Các bước thực hiện | Kết quả mong đợi (HTTP Status & Response body & DB State) | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-AUTH-01-01` | Happy Path | Có user `admin_cafe458` trong DB | `{"ten_dang_nhap": "admin_cafe458", "mat_khau": "MatKhauChuQuan458!"}` | 1. Gửi POST tới endpoint với body hợp lệ | - HTTP 200 OK<br>- Trả về: `{"token": "<jwt_string>", "ten_dang_nhap": "admin_cafe458", "token_type": "bearer", "expires_in": 43200}`<br>- Token giải mã đúng Header HS256, exp sau 12h. | High |
| `TC-AUTH-01-02` | Negative (Validation) | Không | `{"ten_dang_nhap": "", "mat_khau": "MatKhauChuQuan458!"}` | 1. Để trống tên đăng nhập | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Không được để trống!", "field": "ten_dang_nhap"}}` | High |
| `TC-AUTH-01-03` | Negative (Validation) | Không | `{"ten_dang_nhap": "admin_cafe458", "mat_khau": ""}` | 1. Để trống mật khẩu | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Không được để trống!", "field": "mat_khau"}}` | High |
| `TC-AUTH-01-04` | Negative (Auth) | User không tồn tại | `{"ten_dang_nhap": "user_khong_ton_tai", "mat_khau": "123456"}` | 1. Gửi tài khoản sai | - HTTP 401 Unauthorized<br>- Trả về: `{"error": {"code": "AUTH_FAILED", "message": "Đăng nhập không thành công!"}}` | High |
| `TC-AUTH-01-05` | Negative (Auth) | Có user `admin_cafe458` | `{"ten_dang_nhap": "admin_cafe458", "mat_khau": "MatKhauSai123"}` | 1. Gửi mật khẩu sai | - HTTP 401 Unauthorized<br>- Trả về: `{"error": {"code": "AUTH_FAILED", "message": "Đăng nhập không thành công!"}}` | High |
| `TC-AUTH-01-06` | Boundary (Trim QĐ-20) | Có user `admin_cafe458` | `{"ten_dang_nhap": "  admin_cafe458  ", "mat_khau": "MatKhauChuQuan458!"}` | 1. Nhập username kèm khoảng trắng | - HTTP 200 OK<br>- Hệ thống trim khoảng trắng đầu/cuối và đăng nhập thành công. | Medium |

---

#### 2. API-AUTH-02: Đăng xuất hệ thống (`POST /api/v1/auth/logout`)
- **Mô tả:** Kết thúc phiên làm việc của chủ quán.

| Mã Test Case | Phân loại | Tiền điều kiện | Header / Request | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-AUTH-02-01` | Happy Path | Đã đăng nhập, có token hợp lệ | `Authorization: Bearer <valid_jwt>` | 1. Gửi POST logout kèm token | - HTTP 200 OK<br>- Trả về: `{"message": "Đăng xuất thành công"}` | High |
| `TC-AUTH-02-02` | Negative (Security) | Chưa đăng nhập | Không có header `Authorization` | 1. Gửi POST logout không kèm token | - HTTP 401 Unauthorized<br>- Trả về lỗi Unauthorized theo chuẩn `QĐ-21`. | High |
| `TC-AUTH-02-03` | Negative (Security) | Token bị giả mạo / hết hạn | `Authorization: Bearer invalid_jwt_string` | 1. Gửi token sai chữ ký | - HTTP 401 Unauthorized | Medium |

---

#### 3. API-AUTH-03: Đổi mật khẩu (`PUT /api/v1/auth/password`)
- **Mô tả:** Kiểm tra mật khẩu cũ, đối chiếu mật khẩu mới và băm bcrypt cập nhật vào bảng `chu_quan`.
- **Header:** `Authorization: Bearer <valid_jwt>`

| Mã Test Case | Phân loại | Tiền điều kiện | Dữ liệu đầu vào (Payload) | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-AUTH-03-01` | Happy Path | User đang có pass `MatKhauChuQuan458!` | `{"mat_khau_cu": "MatKhauChuQuan458!", "mat_khau_moi": "NewPass458@2026", "nhap_lai_mat_khau_moi": "NewPass458@2026"}` | 1. Gửi PUT với thông tin đúng | - HTTP 200 OK<br>- Trả về: `{"message": "Đổi mật khẩu thành công!"}`<br>- DB: Mật khẩu được băm mới bằng bcrypt<br>- Đăng nhập lại bằng mật khẩu cũ trả 401, bằng mật khẩu mới trả 200. | High |
| `TC-AUTH-03-02` | Negative (Validation) | Token hợp lệ | `{"mat_khau_cu": "", "mat_khau_moi": "NewPass458@", "nhap_lai_mat_khau_moi": "NewPass458@"}` | 1. Để trống 1 trường bất kỳ | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Không được để trống!", "field": "mat_khau_cu"}}` | High |
| `TC-AUTH-03-03` | Negative (BR-UC6-02) | Token hợp lệ | `{"mat_khau_cu": "PassCuSaiRoi", "mat_khau_moi": "NewPass458@", "nhap_lai_mat_khau_moi": "NewPass458@"}` | 1. Nhập mật khẩu cũ không đúng | - HTTP 400 Bad Request<br>- Trả về: `{"error": {"code": "INVALID_OLD_PASSWORD", "message": "Mật khẩu cũ không đúng!"}}` | High |
| `TC-AUTH-03-04` | Negative (BR-UC6-03) | Token hợp lệ | `{"mat_khau_cu": "MatKhauChuQuan458!", "mat_khau_moi": "NewPass458@", "nhap_lai_mat_khau_moi": "NewPassKhacNhau"}` | 1. Nhập lại mật khẩu mới không khớp | - HTTP 400 Bad Request<br>- Trả về: `{"error": {"code": "PASSWORD_MISMATCH", "message": "Mật khẩu mới và mật khẩu nhập lại không giống nhau!"}}` | High |
| `TC-AUTH-03-05` | Negative (Security) | Không có token | Không truyền `Authorization` | 1. Gửi request đổi pass | - HTTP 401 Unauthorized | High |
| `TC-AUTH-03-06` | Boundary (Trim QĐ-20) | Token hợp lệ | `{"mat_khau_cu": "MatKhauChuQuan458!", "mat_khau_moi": "  pass123  ", "nhap_lai_mat_khau_moi": "pass123"}` | 1. Mật khẩu mới có khoảng trắng | - Trim khoảng trắng trước khi kiểm tra độ khớp và băm lưu DB. | Low |

---

### PHÂN HỆ 2: KHÁCH HÀNG (CUSTOMER)

#### 4. API-CUST-01: Xem menu và món đề cử (`GET /api/v1/customer/menu`)
- **Mô tả:** Khách quét QR xem thông tin bàn, menu hiển thị và top 3 món đề cử.
- **Query Param:** `qr_token`

| Mã Test Case | Phân loại | Tiền điều kiện | Query Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-CUST-01-01` | Happy Path | Bàn số 01 có `ma_qr = qr_ban_01`, `da_xoa = FALSE`. Menu có món hiển thị. | `?qr_token=qr_ban_01` | 1. Khách quét mã QR gửi request | - HTTP 200 OK<br>- Trả về: `{"ban": {"ma_ban": 1, "so_ban": "01"}, "mon_de_cu": [...], "menu": [...]}`<br>- `mon_de_cu`: tối đa 3 món bán chạy 30 ngày qua xếp thứ hạng 1..3 (`QĐ-18`)<br>- `menu`: chỉ chứa món có `trang_thai = 'Hiển thị'` và `da_xoa = FALSE`, xếp `ma_mon` tăng dần (`QĐ-19`). | High |
| `TC-CUST-01-02` | Negative (BR-UC7-01) | Không tồn tại token `qr_invalid` | `?qr_token=qr_invalid` | 1. Quét mã QR rác | - HTTP 404 Not Found<br>- Trả về: `{"error": {"code": "INVALID_QR", "message": "Mã QR không hợp lệ"}}` | High |
| `TC-CUST-01-03` | Negative (Soft delete) | Bàn số 02 có `da_xoa = TRUE` | `?qr_token=qr_ban_02_da_xoa` | 1. Quét QR của bàn đã bị xóa | - HTTP 404 Not Found<br>- Trả về: `{"error": {"code": "INVALID_QR", "message": "Mã QR không hợp lệ"}}` | High |
| `TC-CUST-01-04` | Boundary (Menu rỗng) | Bàn hợp lệ, tất cả món trong DB đều `Ẩn` hoặc bị xóa mềm | `?qr_token=qr_ban_01` | 1. Gọi menu khi DB rỗng món hiển thị | - HTTP 200 OK<br>- Trả về: `{"ban": {"ma_ban": 1, "so_ban": "01"}, "mon_de_cu": [], "menu": []}`<br>- FE dựa vào đây hiển thị "Menu chưa có món nào". | Medium |
| `TC-CUST-01-05` | Data Privacy | DB có món `ma_mon = 5` có `trang_thai = 'Ẩn'` | `?qr_token=qr_ban_01` | 1. Kiểm tra mảng `menu` và `mon_de_cu` | - Món `ma_mon = 5` tuyệt đối KHÔNG có trong response (`BR-UC7-01`). | High |

---

#### 5. API-CUST-02: Tính trước đơn hàng & thông tin thanh toán (`POST /api/v1/customer/orders/preview`)
- **Mô tả:** Server tự tính tổng tiền từ DB; sinh VietQR nếu chọn Chuyển khoản; không tin giá client (`QĐ-22`).

| Mã Test Case | Phân loại | Tiền điều kiện | Payload | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-CUST-02-01` | Happy Path (Chuyển khoản) | Bàn 01 (`qr_ban_01`). Món 1 giá 25k, Món 2 giá 30k. Biến môi trường VietQR đầy đủ (`QĐ-12`). | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 1, "so_luong": 2}, {"ma_mon": 2, "so_luong": 1}], "phuong_thuc_thanh_toan": "Chuyển khoản"}` | 1. Chọn 2 món, thanh toán Chuyển khoản | - HTTP 200 OK<br>- `tong_tien = 80000`<br>- `vietqr_url` chứa `img.vietqr.io` kèm số tiền 80000 và nội dung `BAN 01`<br>- `bank_info`: `{bank_name, bank_account_no, bank_account_name, noi_dung: "BAN 01"}`. | High |
| `TC-CUST-02-02` | Happy Path (Tiền mặt) | Bàn 01 hợp lệ | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 1, "so_luong": 1}], "phuong_thuc_thanh_toan": "Tiền mặt"}` | 1. Chọn Tiền mặt | - HTTP 200 OK<br>- `tong_tien = 25000`<br>- `vietqr_url: null`<br>- `message: "Chờ thu tiền sau khi bưng nước ra"`. | High |
| `TC-CUST-02-03` | Negative (Validation) | Bàn hợp lệ | `{"qr_token": "qr_ban_01", "items": [], "phuong_thuc_thanh_toan": "Tiền mặt"}` | 1. Gửi giỏ hàng rỗng | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Vui lòng chọn ít nhất một món"}}` | High |
| `TC-CUST-02-04` | Negative (Món ẩn/xóa) | Món 3 đang bị Ẩn hoặc Đã xóa | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 3, "so_luong": 1}], "phuong_thuc_thanh_toan": "Tiền mặt"}` | 1. Khách gửi món không còn bán | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "ORDER_FAILED", "message": "Đặt món không thành công, vui lòng thử lại!"}}` | High |
| `TC-CUST-02-05` | Security (Anti-tamper) | Món 1 trong DB giá 25.000đ | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 1, "so_luong": 1, "gia": 1000}], "phuong_thuc_thanh_toan": "Tiền mặt"}` | 1. Client hack sửa gửi giá 1.000đ | - HTTP 200 OK<br>- `tong_tien` phản hồi VẪN LÀ 25.000đ (Server lấy giá DB, bỏ qua giá client). | High |

---

#### 6. API-CUST-03: Tạo đơn đặt món (`POST /api/v1/customer/orders`)
- **Mô tả:** Khách nhấn Hoàn tất. Lưu transaction đa bảng: tạo `don_hang`, snapshot `chi_tiet_don`, chuyển `ban.trang_thai = 'Đang phục vụ'`.

| Mã Test Case | Phân loại | Tiền điều kiện | Payload | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-CUST-03-01` | Happy Path | Bàn 01 đang 'Trống'. Món 1 (Cà phê sữa, giá 25k). | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 1, "so_luong": 2}], "phuong_thuc_thanh_toan": "Tiền mặt", "ghi_chu": "Ít đá"}` | 1. Gửi request tạo đơn hợp lệ | - HTTP 201 Created<br>- Trả về: `{"ma_don_hang": 1, "ma_don_hien_thi": "#0101", "so_ban": "01", "tong_tien": 50000, "trang_thai": "Chưa xác nhận thanh toán", "message": "Đặt món thành công"}`<br>- DB `don_hang`: tạo dòng mới, `thoi_gian_giao_dich = NULL`, `da_xoa = FALSE`<br>- DB `ban`: `trang_thai` chuyển từ 'Trống' sang 'Đang phục vụ' (`BR-UC4-01`). | High |
| `TC-CUST-03-02` | Data Snapshot (`BR-UC3-08`) | Đơn vừa tạo thành công | Xem bảng `chi_tiet_don` | 1. Truy vấn DB `chi_tiet_don` | - Bảng `chi_tiet_don` lưu chính xác snapshot `ten_mon = "Cà phê sữa"`, `gia = 25000`, `so_luong = 2`. | High |
| `TC-CUST-03-03` | Multi-order (`BR-UC7-06`) | Bàn 01 đang 'Đang phục vụ' (đã có đơn trước) | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 2, "so_luong": 1}], "phuong_thuc_thanh_toan": "Chuyển khoản"}` | 1. Khách tại bàn gọi thêm món lần 2 | - HTTP 201 Created<br>- Tạo thêm đơn hàng riêng biệt mới với trạng thái "Chưa xác nhận thanh toán"<br>- Bàn 01 tiếp tục giữ trạng thái 'Đang phục vụ'. | High |
| `TC-CUST-03-04` | Negative (Validation) | Bàn hợp lệ | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 1, "so_luong": 0}], "phuong_thuc_thanh_toan": "Tiền mặt"}` | 1. Đặt món với số lượng 0 | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Vui lòng chọn ít nhất một món"}}` | High |
| `TC-CUST-03-05` | Boundary (`BR-UC7-08`) | Bàn hợp lệ | `{"qr_token": "qr_ban_01", "items": [{"ma_mon": 1, "so_luong": 1}], "phuong_thuc_thanh_toan": "Tiền mặt", "ghi_chu": "<chuỗi 201 ký tự>"}` | 1. Nhập ghi chú vượt 200 ký tự | - HTTP 422 Unprocessable Entity<br>- Báo lỗi độ dài ghi chú vượt quá tối đa 200 ký tự. | Medium |
| `TC-CUST-03-06` | Transaction Rollback | Mock DB lỗi khi insert chi tiết đơn | Payload hợp lệ | 1. Kích hoạt lỗi ngắt kết nối giữa chừng | - HTTP 500<br>- Trả về: `{"error": {"code": "ORDER_FAILED", "message": "Đặt món không thành công, vui lòng thử lại!"}}`<br>- DB Rollback toàn bộ: không có đơn rác trong `don_hang`, bàn không bị đổi trạng thái sai. | High |

---

### PHÂN HỆ 3: QUẢN LÝ GỌI MÓN (ORDERS)

#### 7. API-ORD-01: Lấy danh sách đơn theo ngày (`GET /api/v1/admin/orders`)
- **Mô tả:** Chủ quán xem danh sách đơn theo ngày (mặc định hôm nay), sắp xếp đơn mới nhất lên đầu, loại bỏ đơn đã xóa.
- **Header:** `Authorization: Bearer <token>`
- **Query Param:** `date` (format `YYYY-MM-DD`, mặc định hôm nay Asia/Ho_Chi_Minh - `QĐ-14`)

| Mã Test Case | Phân loại | Tiền điều kiện | Query Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-ORD-01-01` | Happy Path (Mặc định) | DB có 3 đơn tạo hôm nay (09:00, 10:15, 10:30) | Không truyền param | 1. Gọi GET không param | - HTTP 200 OK<br>- Trả về danh sách 3 đơn của ngày hôm nay<br>- Sắp xếp thứ tự thời gian giảm dần (`10:30` -> `10:15` -> `09:00`) (`BR-UC2-04`). | High |
| `TC-ORD-01-02` | Happy Path (Chọn ngày) | DB có đơn ngày `2026-11-10` | `?date=2026-11-10` | 1. Truy vấn đơn ngày 10/11/2026 | - HTTP 200 OK<br>- Chỉ trả về các đơn có `thoi_gian_dat` thuộc ngày `2026-11-10` múi giờ Việt Nam. | High |
| `TC-ORD-01-03` | Boundary (Ngày rỗng) | Ngày `2026-01-01` không có đơn | `?date=2026-01-01` | 1. Truy vấn ngày chưa có đơn | - HTTP 200 OK<br>- Trả về mảng rỗng `[]` (FE hiện "Chưa có đơn nào" - `UC_2.2 2b1`). | Medium |
| `TC-ORD-01-04` | Filter (`BR-UC2-07`) | DB có đơn `ma_don_hang = 10` có `da_xoa = TRUE` | Ngày chứa đơn 10 | 1. Lấy danh sách đơn | - Đơn 10 TUYỆT ĐỐI không có trong danh sách trả về. | High |
| `TC-ORD-01-05` | Negative (Security) | Chưa đăng nhập | Không có token | 1. Gửi request không header Auth | - HTTP 401 Unauthorized | High |

---

#### 8. API-ORD-02: Xem chi tiết một đơn hàng (`GET /api/v1/admin/orders/{ma_don_hang}`)
- **Mô tả:** Xem chi tiết mã đơn, số bàn, PTTT, ghi chú, trạng thái, danh sách món kèm số lượng và đơn giá snapshot.
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-ORD-02-01` | Happy Path | Đơn `ma_don_hang = 1` tồn tại, gồm 2 ly Cà phê sữa (giá snapshot 25k) | `/api/v1/admin/orders/1` | 1. Xem chi tiết đơn 1 | - HTTP 200 OK<br>- Trả về: `{"ma_don_hang": 1, "ma_don_hien_thi": "#0101", "so_ban": "01", "thoi_gian_dat": "...", "phuong_thuc_thanh_toan": "Tiền mặt", "trang_thai": "Chưa xác nhận thanh toán", "ghi_chu": "Ít đá", "tong_tien": 50000, "items": [{"ma_mon": 1, "ten_mon": "Cà phê sữa", "gia": 25000, "so_luong": 2, "thanh_tien": 50000}]}`. | High |
| `TC-ORD-02-02` | Negative (404) | Không tồn tại đơn 9999 | `/api/v1/admin/orders/9999` | 1. Xem mã đơn không có thực | - HTTP 404 Not Found<br>- Báo không tìm thấy đơn hàng. | High |
| `TC-ORD-02-03` | Negative (Đơn đã xóa) | Đơn 2 có `da_xoa = TRUE` | `/api/v1/admin/orders/2` | 1. Xem đơn đã xóa mềm | - HTTP 404 Not Found | High |
| `TC-ORD-02-04` | Negative (Security) | Không có token | `/api/v1/admin/orders/1` | 1. Gửi request không có token | - HTTP 401 Unauthorized | High |

---

#### 9. API-ORD-03: Xác nhận đã nhận tiền (`PATCH /api/v1/admin/orders/{ma_don_hang}/confirm-payment`)
- **Mô tả:** Chuyển đơn sang 'Đã xác nhận thanh toán', ghi nhận `thoi_gian_giao_dich = now()`.
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-ORD-03-01` | Happy Path | Đơn 1 đang ở trạng thái 'Chưa xác nhận thanh toán' | `/api/v1/admin/orders/1/confirm-payment` | 1. Chủ quán xác nhận đã nhận tiền | - HTTP 200 OK<br>- Trả về: `{"message": "Xác nhận đã nhận tiền!"}`<br>- DB `don_hang`: `trang_thai = 'Đã xác nhận thanh toán'`, `thoi_gian_giao_dich` được cập nhật thời gian hiện tại (`BR-UC2-02`). | High |
| `TC-ORD-03-02` | Idempotency / Business Rule (`BR-UC2-01`) | Đơn 1 đã ở trạng thái 'Đã xác nhận thanh toán' | `/api/v1/admin/orders/1/confirm-payment` | 1. Nhấn xác nhận lần thứ 2 | - HTTP 400 Bad Request (hoặc giữ nguyên không đổi)<br>- `thoi_gian_giao_dich` gốc không bị ghi đè, tuân thủ nguyên tắc mỗi đơn chỉ chuyển 1 lần. | High |
| `TC-ORD-03-03` | Negative (Đơn đã xóa) | Đơn 2 có `da_xoa = TRUE` | `/api/v1/admin/orders/2/confirm-payment` | 1. Xác nhận đơn đã xóa | - HTTP 404 Not Found | High |
| `TC-ORD-03-04` | Negative (Security) | Không có token | `/api/v1/admin/orders/1/confirm-payment` | 1. Gửi request không Auth | - HTTP 401 Unauthorized | High |

---

#### 10. API-ORD-04: Xóa đơn hàng (xóa mềm) (`DELETE /api/v1/admin/orders/{ma_don_hang}`)
- **Mô tả:** Đánh dấu `da_xoa = TRUE`, loại khỏi doanh thu, TUYỆT ĐỐI không đổi trạng thái bàn (`BR-UC2-09`).
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-ORD-04-01` | Happy Path | Đơn 1 thuộc bàn 01 (bàn đang 'Đang phục vụ') | `/api/v1/admin/orders/1` | 1. Gửi DELETE đơn 1 | - HTTP 200 OK<br>- Trả về: `{"message": "Đã xóa đơn"}`<br>- DB `don_hang`: `da_xoa = TRUE` (`BR-UC2-08`). | High |
| `TC-ORD-04-02` | Business Rule Critical (`BR-UC2-09`) | Vừa xóa đơn 1 của bàn 01 | Kiểm tra bảng `ban` | 1. Truy vấn bàn 01 trong DB | - Bàn 01 VẪN GIỮ NGUYÊN trạng thái `'Đang phục vụ'`, KHÔNG bị chuyển về 'Trống'. | High |
| `TC-ORD-04-03` | Negative (Đã xóa trước đó) | Đơn 1 đã có `da_xoa = TRUE` | `/api/v1/admin/orders/1` | 1. Gửi lệnh xóa lại | - HTTP 404 Not Found | Medium |
| `TC-ORD-04-04` | Negative (Security) | Không có token | `/api/v1/admin/orders/1` | 1. Gửi request không Auth | - HTTP 401 Unauthorized | High |

---

### PHÂN HỆ 4: THÔNG BÁO (NOTIFICATIONS)

#### 11. API-NOTIF-01: Polling kiểm tra đơn mới & đếm đơn chưa xác nhận (`GET /api/v1/admin/notifications/unread-orders`)
- **Mô tả:** Phục vụ FE polling 5s/lần cập nhật chuông và badge thẻ Đơn hàng (`QĐ-05`, `QĐ-24`).
- **Header:** `Authorization: Bearer <token>`
- **Query Param:** `after_id` (optional)

| Mã Test Case | Phân loại | Tiền điều kiện | Query Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-NOTIF-01-01` | Happy Path (Đếm tổng) | DB có 2 đơn `Chưa xác nhận thanh toán` trên toàn bộ hệ thống | Không param | 1. Gọi polling định kỳ | - HTTP 200 OK<br>- Trả về: `{"unread_count": 2, "has_new": false, "latest_order_id": 10}`. | High |
| `TC-NOTIF-01-02` | Happy Path (Có đơn mới) | FE đang giữ `after_id = 10`. Vừa có khách tạo đơn mới `ma_don_hang = 11`. | `?after_id=10` | 1. Polling kèm after_id | - HTTP 200 OK<br>- Trả về: `{"unread_count": 3, "has_new": true, "latest_order_id": 11}`<br>- FE dựa vào `has_new: true` để kích hoạt hiệu ứng chuông/toast. | High |
| `TC-NOTIF-01-03` | Negative (Security) | Không có token | Không param | 1. Request không Auth | - HTTP 401 Unauthorized | High |

---

### PHÂN HỆ 5: THỰC ĐƠN (MENU) & MEDIA

#### 12. API-MENU-01: Lấy danh sách món cho chủ quán (`GET /api/v1/admin/menu`)
- **Mô tả:** Lấy danh sách tất cả món (cả Hiển thị và Ẩn) để chủ quán quản trị, xếp món mới lên đầu (`QĐ-19`).
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Query Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-MENU-01-01` | Happy Path | DB có món 1 ('Hiển thị'), món 2 ('Ẩn'), món 3 (`da_xoa = TRUE`) | Không param | 1. Chủ quán vào màn hình Menu | - HTTP 200 OK<br>- Trả về danh sách gồm món 1 và món 2 (cả Hiển thị và Ẩn)<br>- Sắp xếp `ma_mon DESC` (món mới nhất lên đầu)<br>- Món 3 (đã xóa) KHÔNG xuất hiện (`BR-UC3-09`). | High |
| `TC-MENU-01-02` | Boundary (Menu rỗng) | DB chưa có món nào | Không param | 1. Menu chưa có món | - HTTP 200 OK<br>- Trả về `[]` (FE hiện "Menu chưa có món nào" - `UC_3.1 2b1`). | Medium |
| `TC-MENU-01-03` | Field Check | Món có ảnh và món không có ảnh | Không param | 1. Kiểm tra trường ảnh | - Món có ảnh trả URL đầy đủ từ Supabase Storage; món không ảnh trả `hinh_anh: null` (`QĐ-06`). | Medium |
| `TC-MENU-01-04` | Negative (Security) | Không có token | Không param | 1. Request không Auth | - HTTP 401 Unauthorized | High |

---

#### 13. API-MENU-02: Thêm món mới (`POST /api/v1/admin/menu`)
- **Mô tả:** Tạo món mới. Tên món duy nhất (không phân biệt hoa/thường), giá > 0, mặc định 'Hiển thị' (`BR06`).
- **Header:** `Authorization: Bearer <token>`, `Content-Type: application/json`

| Mã Test Case | Phân loại | Tiền điều kiện | Payload | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-MENU-02-01` | Happy Path | Tên món chưa tồn tại | `{"ten_mon": "Trà vải dưa lưới", "gia_ban": 35000, "hinh_anh": "menu-images/tra_vai.png"}` | 1. Thêm món hợp lệ | - HTTP 201 Created<br>- Trả về: `{"ma_mon": 10, "ten_mon": "Trà vải dưa lưới", "gia_ban": 35000, "trang_thai": "Hiển thị", "da_xoa": false, "message": "Thêm món thành công"}`<br>- Món mới mặc định ở trạng thái 'Hiển thị' (`BR06`). | High |
| `TC-MENU-02-02` | Happy Path (Không ảnh) | Tên món hợp lệ | `{"ten_mon": "Trà ô long sữa", "gia_ban": 30000}` | 1. Thêm món không ảnh | - HTTP 201 Created<br>- `hinh_anh: null` (`BR-UC3-05`). | Medium |
| `TC-MENU-02-03` | Negative (BR-UC3-02) | Token hợp lệ | `{"ten_mon": "", "gia_ban": 30000}` | 1. Để trống tên món | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Không được để trống!", "field": "ten_mon"}}` | High |
| `TC-MENU-02-04` | Negative (BR-UC3-02) | Token hợp lệ | `{"ten_mon": "Cà phê đen", "gia_ban": null}` | 1. Để trống giá bán | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Không được để trống!", "field": "gia_ban"}}` | High |
| `TC-MENU-02-05` | Negative (BR-UC3-03, QĐ-20) | Đã có món "Cà phê đen" | `{"ten_mon": "  cà phê đen  ", "gia_ban": 20000}` | 1. Nhập tên trùng (khác hoa thường và khoảng trắng) | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "DUPLICATE_NAME", "message": "Tên món đã tồn tại!", "field": "ten_mon"}}` | High |
| `TC-MENU-02-06` | Negative (BR-UC3-04) | Tên hợp lệ | `{"ten_mon": "Nước suối", "gia_ban": 0}` | 1. Nhập giá bán = 0 hoặc âm (-5000) | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "INVALID_PRICE", "message": "Giá bán phải là số lớn hơn 0!", "field": "gia_ban"}}` | High |
| `TC-MENU-02-07` | Business Rule (Tái sử dụng tên món đã xóa) | Món "Trà sen" cũ đã bị xóa mềm (`da_xoa = TRUE`) | `{"ten_mon": "Trà sen", "gia_ban": 32000}` | 1. Thêm món có tên trùng món đã xóa | - HTTP 201 Created<br>- Thành công vì quy tắc trùng tên chỉ áp dụng cho món chưa xóa (`BR-UC3-03`). | Medium |

---

#### 14. API-MENU-03: Cập nhật thông tin món (`PUT /api/v1/admin/menu/{ma_mon}`)
- **Mô tả:** Cập nhật tên, giá, ảnh, trạng thái. Giữ nguyên snapshot đơn cũ (`BR-UC3-10`).
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path & Payload | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-MENU-03-01` | Happy Path | Món 1 đang có giá 25.000đ | Path: `/1`<br>Payload: `{"ten_mon": "Cà phê sữa Sài Gòn", "gia_ban": 28000, "trang_thai": "Hiển thị"}` | 1. Cập nhật tên và giá món | - HTTP 200 OK<br>- Trả về thông tin cập nhật kèm message: "Cập nhật món thành công"<br>- DB cập nhật tên mới và giá 28.000đ. | High |
| `TC-MENU-03-02` | Snapshot Integrity (`BR-UC3-10`) | Đơn cũ số 1 có món 1 lúc đặt là 25.000đ | Kiểm tra đơn 1 sau khi cập nhật món 1 lên 28.000đ | 1. Xem lại chi tiết đơn 1 | - Đơn 1 VẪN GIỮ NGUYÊN giá 25.000đ trong `chi_tiet_don`, không bị tăng theo giá mới. | High |
| `TC-MENU-03-03` | Negative (Trùng tên) | Đang có món 2 tên "Bạc xỉu" | Path: `/1`<br>Payload: `{"ten_mon": "Bạc xỉu", "gia_ban": 28000}` | 1. Đổi tên món 1 trùng tên món 2 | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "DUPLICATE_NAME", "message": "Tên món đã tồn tại!", "field": "ten_mon"}}` | High |
| `TC-MENU-03-04` | Negative (Giá sai) | Món 1 tồn tại | Path: `/1`<br>Payload: `{"ten_mon": "Cà phê", "gia_ban": -1000}` | 1. Nhập giá âm | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "INVALID_PRICE", "message": "Giá bán phải là số lớn hơn 0!"}}` | High |
| `TC-MENU-03-05` | Happy Path (Đổi trạng thái) | Món 1 đang 'Hiển thị' | Path: `/1`<br>Payload: `{"trang_thai": "Ẩn"}` | 1. Ẩn món khỏi menu khách | - HTTP 200 OK<br>- DB: `trang_thai = 'Ẩn'`<br>- Khách quét QR menu không còn thấy món 1. | High |
| `TC-MENU-03-06` | Negative (404) | Món 999 không tồn tại | Path: `/999`<br>Payload: `{"ten_mon": "Món ảo", "gia_ban": 20000}` | 1. Sửa món không tồn tại | - HTTP 404 Not Found | High |

---

#### 15. API-MENU-04: Xóa món khỏi thực đơn (xóa mềm) (`DELETE /api/v1/admin/menu/{ma_mon}`)
- **Mô tả:** Đánh dấu `da_xoa = TRUE`. Món không còn hiện cho khách và admin menu (`BR-UC3-07`, `BR-UC3-09`).
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-MENU-04-01` | Happy Path | Món 1 tồn tại và chưa bị xóa | `/api/v1/admin/menu/1` | 1. Chủ quán nhấn xóa món 1 | - HTTP 200 OK<br>- Trả về: `{"message": "Đã xóa món thành công"}`<br>- DB: `da_xoa = TRUE`. | High |
| `TC-MENU-04-02` | Verify UI Filter (`BR-UC3-09`) | Món 1 vừa bị xóa mềm | Gọi API-MENU-01 và API-CUST-01 | 1. Lấy danh sách menu của chủ quán và khách | - Món 1 KHÔNG còn xuất hiện ở cả 2 API. | High |
| `TC-MENU-04-03` | History Integrity (`BR-UC3-08`) | Đơn cũ có chứa món 1 | Gọi API-ORD-02 xem đơn cũ | 1. Xem chi tiết đơn cũ có món 1 | - Tên món và giá snapshot trong đơn cũ VẪN HIỂN THỊ ĐẦY ĐỦ, không bị mất hay null. | High |
| `TC-MENU-04-04` | Negative (404) | Món 1 đã có `da_xoa = TRUE` | `/api/v1/admin/menu/1` | 1. Gửi lệnh xóa lần 2 | - HTTP 404 Not Found | Medium |

---

#### 16. API-MEDIA-01: Tải lên hình ảnh món ăn (`POST /api/v1/admin/menu/upload-image`)
- **Mô tả:** Tải ảnh lên Supabase Storage bucket `menu-images` qua BE, chỉ chấp nhận jpg/png/webp <= 2MB (`QĐ-06`).
- **Header:** `Authorization: Bearer <token>`, `Content-Type: multipart/form-data`

| Mã Test Case | Phân loại | Tiền điều kiện | File đính kèm | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-MEDIA-01-01` | Happy Path | Token hợp lệ | File `coffee.png` (dung lượng 500 KB) | 1. Upload ảnh PNG hợp lệ | - HTTP 200 OK<br>- Trả về: `{"image_path": "menu-images/<uuid>.png", "image_url": "https://...supabase.co/.../coffee.png"}`. | High |
| `TC-MEDIA-01-02` | Negative (Dung lượng) | Token hợp lệ | File `large_image.jpg` (dung lượng 2.5 MB) | 1. Upload file vượt quá 2MB | - HTTP 400 Bad Request<br>- Trả về lỗi: dung lượng ảnh vượt quá giới hạn cho phép (tối đa 2MB). | High |
| `TC-MEDIA-01-03` | Negative (Định dạng) | Token hợp lệ | File `script.exe` hoặc `doc.pdf` | 1. Upload file sai định dạng ảnh | - HTTP 400 Bad Request<br>- Trả về lỗi: chỉ chấp nhận định dạng jpg, png, webp. | High |
| `TC-MEDIA-01-04` | Negative (Security) | Không có token | File `coffee.png` hợp lệ | 1. Gửi upload không Auth | - HTTP 401 Unauthorized | High |

---

### PHÂN HỆ 6: BÀN ĂN (TABLES)

#### 17. API-TAB-01: Lấy sơ đồ trạng thái bàn (`GET /api/v1/admin/tables`)
- **Mô tả:** Lấy danh sách tất cả các bàn kèm trạng thái 'Trống' hoặc 'Đang phục vụ', sắp xếp `so_ban ASC`.
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Query Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-TAB-01-01` | Happy Path | DB có bàn 01 ('Trống'), bàn 02 ('Đang phục vụ'), bàn 03 (`da_xoa = TRUE`) | Không param | 1. Vào màn hình Bàn | - HTTP 200 OK<br>- Trả về danh sách bàn 01 và 02 kèm trạng thái chuẩn<br>- Bàn 03 đã xóa KHÔNG xuất hiện<br>- Sắp xếp thứ tự tăng dần theo số bàn (`so_ban ASC`). | High |
| `TC-TAB-01-02` | Boundary (Chưa có bàn) | DB chưa có bàn nào | Không param | 1. Hệ thống mới tạo chưa có bàn | - HTTP 200 OK<br>- Trả về `[]` (FE hiện "Chưa có bàn nào" - `UC_4.1 2b1`). | Medium |
| `TC-TAB-01-03` | Schema Check | Bàn hợp lệ | Không param | 1. Kiểm tra cấu trúc item | - Mỗi item có đủ `{ma_ban, so_ban, trang_thai, ma_qr}`. | Medium |
| `TC-TAB-01-04` | Negative (Security) | Không có token | Không param | 1. Gửi request không Auth | - HTTP 401 Unauthorized | High |

---

#### 18. API-TAB-02: Thêm bàn mới (`POST /api/v1/admin/tables`)
- **Mô tả:** Tạo bàn mới trạng thái 'Trống', tự sinh mã QR an toàn 16 ký tự, tạo cùng lúc bàn và mã QR (`BR-UC4-05`, `BR-UC4-07`).
- **Header:** `Authorization: Bearer <token>`, `Content-Type: application/json`

| Mã Test Case | Phân loại | Tiền điều kiện | Payload | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-TAB-02-01` | Happy Path | Số bàn "05" chưa tồn tại | `{"so_ban": "05"}` | 1. Nhập số bàn "05" nhấn Lưu | - HTTP 201 Created<br>- Trả về: `{"ma_ban": 5, "so_ban": "05", "trang_thai": "Trống", "ma_qr": "<16_chars>", "qr_download_url": "/api/v1/admin/tables/5/qr-image", "message": "Thêm bàn thành công"}`<br>- Bàn mới mặc định ở trạng thái 'Trống' (`BR-UC4-06`). | High |
| `TC-TAB-02-02` | Negative (BR-UC4-03) | Token hợp lệ | `{"so_ban": ""}` | 1. Để trống số bàn | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "VALIDATION_ERROR", "message": "Không được để trống!", "field": "so_ban"}}` | High |
| `TC-TAB-02-03` | Negative (BR-UC4-04) | Đã có bàn số "05" đang hoạt động | `{"so_ban": "05"}` | 1. Thêm số bàn bị trùng | - HTTP 422 Unprocessable Entity<br>- Trả về: `{"error": {"code": "DUPLICATE_TABLE", "message": "Số bàn đã tồn tại!", "field": "so_ban"}}` | High |
| `TC-TAB-02-04` | String Match (QĐ-20) | Đã có bàn số "03" | `{"so_ban": "3"}` | 1. Thêm bàn "3" (so khớp nguyên chuỗi) | - HTTP 201 Created<br>- Hệ thống coi "3" và "03" là 2 chuỗi khác nhau, cho phép tạo thành công. | Medium |
| `TC-TAB-02-05` | Soft-delete Re-add | Bàn "04" cũ đã bị xóa mềm (`da_xoa = TRUE`) | `{"so_ban": "04"}` | 1. Thêm lại số bàn "04" | - HTTP 201 Created<br>- Cho phép tạo thành công vì bàn cũ đã xóa không tính (`BR-UC4-04`). | Medium |
| `TC-TAB-02-06` | QR Safety (QĐ-13) | Vừa tạo bàn thành công | Kiểm tra mã QR sinh ra | 1. Giải mã nội dung mã QR | - Nội dung mã QR nhúng URL `{FRONTEND_BASE_URL}/menu?qr={ma_qr}`<br>- Không chứa số bàn thô trên URL để tránh đoán URL bàn khác. | High |

---

#### 19. API-TAB-03: Tải file ảnh mã QR của bàn (`GET /api/v1/admin/tables/{ma_ban}/qr-image`)
- **Mô tả:** Xuất file ảnh PNG của mã QR bàn để chủ quán in ấn dán tại bàn.
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-TAB-03-01` | Happy Path | Bàn 1 (số bàn "01") tồn tại | `/api/v1/admin/tables/1/qr-image` | 1. Tải ảnh QR bàn 1 | - HTTP 200 OK<br>- `Content-Type: image/png`<br>- Header `Content-Disposition: attachment; filename="QR_Ban_01.png"`<br>- Dữ liệu nhị phân trả về đọc được bằng thư viện ảnh. | High |
| `TC-TAB-03-02` | Negative (404) | Bàn 999 không tồn tại hoặc đã xóa mềm | `/api/v1/admin/tables/999/qr-image` | 1. Tải ảnh bàn không tồn tại | - HTTP 404 Not Found | High |
| `TC-TAB-03-03` | Negative (Security) | Không có token | `/api/v1/admin/tables/1/qr-image` | 1. Request không Auth | - HTTP 401 Unauthorized | High |

---

#### 20. API-TAB-04: Xóa bàn (`DELETE /api/v1/admin/tables/{ma_ban}`)
- **Mô tả:** Chỉ được xóa bàn ở trạng thái 'Trống' (`BR-UC4-08`). Vô hiệu hóa mã QR của bàn.
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-TAB-04-01` | Happy Path | Bàn 1 đang ở trạng thái `'Trống'` | `/api/v1/admin/tables/1` | 1. Nhấn xóa bàn 1 | - HTTP 200 OK<br>- Trả về: `{"message": "Xóa bàn thành công"}`<br>- DB: `da_xoa = TRUE` (`BR-UC4-10`). | High |
| `TC-TAB-04-02` | Business Rule Critical (`BR-UC4-08`) | Bàn 2 đang ở trạng thái `'Đang phục vụ'` | `/api/v1/admin/tables/2` | 1. Cố tình gửi lệnh xóa bàn 2 | - HTTP 400 Bad Request<br>- Trả về: `{"error": {"code": "TABLE_IN_USE", "message": "Chỉ được xóa bàn ở trạng thái Trống"}}`<br>- DB không thay đổi. | High |
| `TC-TAB-04-03` | QR Invalidation Check | Bàn 1 vừa bị xóa | Quét mã QR của bàn 1 | 1. Gọi API xem menu với QR bàn 1 | - API-CUST-01 trả 404 "Mã QR không hợp lệ" (`BR-UC7-01`). | High |
| `TC-TAB-04-04` | Negative (Security) | Không có token | `/api/v1/admin/tables/1` | 1. Request không Auth | - HTTP 401 Unauthorized | High |

---

#### 21. API-TAB-05: Xác nhận bàn trống (`PATCH /api/v1/admin/tables/{ma_ban}/empty`)
- **Mô tả:** Chuyển bàn từ 'Đang phục vụ' về 'Trống' sau khi khách rời đi (`BR-UC4-02`, `BR-UC4-11`).
- **Header:** `Authorization: Bearer <token>`

| Mã Test Case | Phân loại | Tiền điều kiện | Path Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-TAB-05-01` | Happy Path | Bàn 2 đang ở trạng thái `'Đang phục vụ'` | `/api/v1/admin/tables/2/empty` | 1. Chủ quán xác nhận dọn bàn xong | - HTTP 200 OK<br>- Trả về: `{"message": "Đã đưa bàn về trạng thái Trống"}`<br>- DB `ban`: `trang_thai = 'Trống'`. | High |
| `TC-TAB-05-02` | Business Rule / Idempotency (`BR-UC4-11`) | Bàn 1 vốn đang ở trạng thái `'Trống'` | `/api/v1/admin/tables/1/empty` | 1. Gọi API xác nhận bàn trống cho bàn đã trống | - HTTP 400 Bad Request (hoặc không đổi gì)<br>- Báo lỗi hoặc từ chối vì thao tác chỉ áp dụng cho bàn đang phục vụ. | High |
| `TC-TAB-05-03` | History Integrity | Bàn 2 vừa chuyển về Trống, trước đó có 3 đơn hàng | Xem lại lịch sử các đơn của bàn 2 | 1. Gọi API danh sách đơn | - Các đơn hàng trước đó không bị ảnh hưởng trạng thái. | Medium |
| `TC-TAB-05-04` | Negative (Security) | Không có token | `/api/v1/admin/tables/2/empty` | 1. Request không Auth | - HTTP 401 Unauthorized | High |

---

### PHÂN HỆ 7: BÁO CÁO DOANH THU (REPORTS)

#### 22. API-REP-01: Lấy danh sách tổng doanh thu (`GET /api/v1/admin/reports/revenue`)
- **Mô tả:** Xem danh sách tổng doanh thu theo kỳ (ngày/tháng/năm). Chỉ tính đơn đã xác nhận và chưa xóa (`BR-UC5-01`).
- **Header:** `Authorization: Bearer <token>`
- **Query Param:** `period` (`day` \| `month` \| `year`, default `day`)

| Mã Test Case | Phân loại | Tiền điều kiện | Query Param | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-REP-01-01` | Happy Path (Theo ngày) | Có các đơn đã xác nhận trong ngày 10/11 và 11/11 | `?period=day` (hoặc không param) | 1. Xem danh sách theo ngày | - HTTP 200 OK<br>- Trả về mảng các ngày kèm tổng doanh thu gom theo ngày<br>- Sắp xếp ngày mới nhất ở trên cùng (`BR-UC5-05`). | High |
| `TC-REP-01-02` | Happy Path (Theo tháng) | Có đơn trong tháng 10/2026 và 11/2026 | `?period=month` | 1. Xem danh sách theo tháng | - HTTP 200 OK<br>- Gom doanh thu theo tháng `YYYY-MM`<br>- Tổng doanh thu tháng = tổng tất cả các ngày trong tháng (`BR-UC5-03`). | High |
| `TC-REP-01-03` | Happy Path (Theo năm) | Có đơn trong năm 2026 | `?period=year` | 1. Xem danh sách theo năm | - HTTP 200 OK<br>- Gom doanh thu theo năm `YYYY` (`BR-UC5-04`). | Medium |
| `TC-REP-01-04` | Business Rule Critical (`BR-UC5-01`) | Đơn A: 50k (Chưa xác nhận); Đơn B: 60k (Đã xác nhận nhưng bị xóa mềm); Đơn C: 70k (Đã xác nhận, chưa xóa) | `?period=day` | 1. Tính toán doanh thu ngày | - Tổng doanh thu phản hồi CHỈ LÀ 70.000đ (Đơn A và Đơn B tuyệt đối không được cộng vào doanh thu). | High |
| `TC-REP-01-05` | Boundary (Chưa có doanh thu) | Quán mới mở chưa có đơn xác nhận nào | `?period=day` | 1. Xem báo cáo khi chưa có đơn | - HTTP 200 OK<br>- Trả về: `{"items": []}` (FE hiện "Chưa có doanh thu nào" - `UC_5.1 2b1`). | Medium |
| `TC-REP-01-06` | Negative (Security) | Không có token | `?period=day` | 1. Request không Auth | - HTTP 401 Unauthorized | High |

---

#### 23. API-REP-02: Chi tiết doanh thu & Thống kê bán hàng theo kỳ (ENDPOINT GỘP) (`GET /api/v1/admin/reports/details`)
- **Mô tả:** Endpoint gộp cho màn hình U15: Lấy đồng thời doanh thu theo PTTT và thống kê số ly bán ra theo từng món.
- **Header:** `Authorization: Bearer <token>`
- **Query Params:** `period` (`day` \| `month` \| `year`), `date` (`YYYY-MM-DD` \| `YYYY-MM` \| `YYYY`)

| Mã Test Case | Phân loại | Tiền điều kiện | Query Params | Các bước thực hiện | Kết quả mong đợi | Mức ưu tiên |
|:---|:---:|:---|:---|:---|:---|:---:|
| `TC-REP-02-01` | Happy Path (Chi tiết ngày) | Ngày 11/11/2026 có 2 đơn xác nhận: Đơn 1 (Tiền mặt: 50k, 2 Cà phê sữa); Đơn 2 (Chuyển khoản: 60k, 2 Bạc xỉu) | `?period=day&date=2026-11-11` | 1. Chủ quán nhấn xem chi tiết ngày 11/11 | - HTTP 200 OK<br>- Trả về đủ 2 phần:<br>  1. `revenue_by_payment_method`: `{"tien_mat": 50000, "chuyen_khoan": 60000, "tong_doanh_thu": 110000}` (`BR-UC5-06`)<br>  2. `sales_statistics`: `{"tong_so_ly": 4, "items": [...]}` (`BR-UC5-08`). | High |
| `TC-REP-02-02` | Đồng hạng bán chạy (`BR-UC5-09`) | Trong kỳ chọn: Cà phê sữa bán 10 ly, Bạc xỉu bán 10 ly (cùng cao nhất), Trà đào bán 5 ly | `?period=day&date=2026-11-11` | 1. Kiểm tra cờ `ban_chay_nhat` | - Cả Cà phê sữa VÀ Bạc xỉu đều có cờ `ban_chay_nhat: true`<br>- Trà đào có `ban_chay_nhat: false`. | High |
| `TC-REP-02-03` | Sắp xếp số ly (`BR-UC5-10`) | Các món có số lượng bán khác nhau | `?period=day&date=2026-11-11` | 1. Kiểm tra thứ tự trong `sales_statistics.items` | - Danh sách món sắp xếp giảm dần theo số lượng bán (`so_luong DESC`). | High |
| `TC-REP-02-04` | Snapshot Name Update (`AUD-12`) | Món ban đầu tên "Trà sen" bán 5 ly. Sau đó chủ quán đổi tên thành "Trà sen Tây Hồ". | `?period=day&date=...` | 1. Xem thống kê bán hàng của kỳ cũ | - Thống kê gom nhóm theo `ma_mon` và lấy tên snapshot của đơn gần nhất trong kỳ. | Medium |
| `TC-REP-02-05` | Negative (Validation) | Token hợp lệ | `?period=tuan&date=2026-11-11` | 1. Truyền period không hợp lệ | - HTTP 422 Unprocessable Entity<br>- Báo lỗi tham số period không hợp lệ (chỉ nhận day/month/year). | Medium |
| `TC-REP-02-06` | Negative (Security) | Không có token | `?period=day&date=2026-11-11` | 1. Request không Auth | - HTTP 401 Unauthorized | High |

---

## 3. CHECKLIST KIỂM THỬ KHUYẾN NGHỊ TRƯỚC KHI TÍCH HỢP FRONT-END

Chủ quán hoặc QA/Dev cần tích chọn hoàn tất các mục sau trước khi bấm kết nối với FE:

- [ ] **1. Định dạng lỗi thống nhất (QĐ-21):** Tất cả response lỗi 4xx/500 đều tuân thủ `{ "error": { "code": "...", "message": "...", "field": "..." } }`. Không để lọt stack trace hay lỗi mặc định của framework.
- [ ] **2. Bảo mật phân quyền:** 19/23 API yêu cầu quyền Chủ quán đều chặn 401 khi thiếu Bearer token hoặc token giả mạo. Chỉ 4 API mở Public (`/auth/login`, `/customer/menu`, `/customer/orders/preview`, `/customer/orders`).
- [ ] **3. Tính toàn vẹn xóa mềm:** Xóa đơn, xóa món, xóa bàn đều là cập nhật cờ `da_xoa = TRUE`, không bao giờ dùng lệnh `DELETE FROM ...`.
- [ ] **4. Nghiệp vụ trạng thái bàn:** 
  - Khách gửi đơn thành công -> Bàn tự động sang `Đang phục vụ`.
  - Xóa đơn -> Trạng thái bàn giữ nguyên (không bị về Trống).
  - Bàn đang phục vụ -> Chặn không cho xóa bàn.
- [ ] **5. Nghiệp vụ snapshot đơn hàng:** Giá và tên món trong chi tiết đơn được snapshot lúc đặt. Sửa giá hay xóa món sau đó không làm thay đổi lịch sử đơn cũ.
- [ ] **6. Doanh thu chính xác:** Chỉ đơn `Đã xác nhận thanh toán` và `da_xoa = FALSE` mới được tính doanh thu.
- [ ] **7. Tích hợp CORS:** Backend đã bật CORS cho origin của Front-End (`http://localhost:5173`).
