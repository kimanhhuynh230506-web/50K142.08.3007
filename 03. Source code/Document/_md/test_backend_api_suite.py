"""
Test Suite tự động hóa kiểm thử 23 API Back-End Hệ thống Quản lý Cà phê 458
Áp dụng: pytest + httpx (Async hoặc Sync)
Chạy lệnh: pytest Document/_md/test_backend_api_suite.py -v -s
Hoặc copy vào thư mục Back-End/tests/test_api.py
"""

import os
import pytest
import httpx

# Cấu hình địa chỉ Backend API (Mặc định chạy ở cổng 8000)
BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api/v1")
ADMIN_USER = os.getenv("OWNER_USERNAME", "admin_cafe458")
ADMIN_PASS = os.getenv("OWNER_PASSWORD", "MatKhauChuQuan458!")

client = httpx.Client(base_url=BASE_URL, timeout=10.0)

# Biến dùng chung qua các bước kiểm thử luồng tích hợp E2E
state = {
    "token": None,
    "ma_ban": None,
    "so_ban": "99",
    "ma_qr": None,
    "ma_mon": None,
    "ma_don_hang": None,
}


# ==============================================================================
# 1. KIỂM THỬ PHÂN HỆ XÁC THỰC (API-AUTH-01, 02, 03)
# ==============================================================================

class TestAuth:
    def test_tc_auth_01_01_login_success(self):
        """TC-AUTH-01-01: Đăng nhập thành công với tài khoản chủ quán chuẩn."""
        res = client.post("/auth/login", json={"ten_dang_nhap": ADMIN_USER, "mat_khau": ADMIN_PASS})
        assert res.status_code == 200, f"Đăng nhập thất bại: {res.text}"
        data = res.json()
        assert "token" in data
        assert data.get("ten_dang_nhap") == ADMIN_USER
        state["token"] = data["token"]

    def test_tc_auth_01_02_login_empty_username(self):
        """TC-AUTH-01-02: Để trống tên đăng nhập -> 422."""
        res = client.post("/auth/login", json={"ten_dang_nhap": "", "mat_khau": ADMIN_PASS})
        assert res.status_code == 422
        err = res.json().get("error", {})
        assert "Không được để trống!" in err.get("message", "")

    def test_tc_auth_01_03_login_empty_password(self):
        """TC-AUTH-01-03: Để trống mật khẩu -> 422."""
        res = client.post("/auth/login", json={"ten_dang_nhap": ADMIN_USER, "mat_khau": ""})
        assert res.status_code == 422
        err = res.json().get("error", {})
        assert "Không được để trống!" in err.get("message", "")

    def test_tc_auth_01_04_login_wrong_password(self):
        """TC-AUTH-01-05: Sai mật khẩu -> 401."""
        res = client.post("/auth/login", json={"ten_dang_nhap": ADMIN_USER, "mat_khau": "WrongPassword!"})
        assert res.status_code == 401
        err = res.json().get("error", {})
        assert "Đăng nhập không thành công!" in err.get("message", "")

    def test_tc_auth_02_02_logout_unauthorized(self):
        """TC-AUTH-02-02: Logout không truyền token -> 401."""
        res = client.post("/auth/logout")
        assert res.status_code == 401

    def test_tc_auth_03_04_change_password_mismatch(self):
        """TC-AUTH-03-04: Mật khẩu mới và nhập lại không khớp -> 400."""
        headers = {"Authorization": f"Bearer {state['token']}"}
        res = client.put(
            "/auth/password",
            headers=headers,
            json={
                "mat_khau_cu": ADMIN_PASS,
                "mat_khau_moi": "NewPass458@1",
                "nhap_lai_mat_khau_moi": "NewPass458@2",
            },
        )
        assert res.status_code == 400
        err = res.json().get("error", {})
        assert "không giống nhau" in err.get("message", "")


# ==============================================================================
# 2. KIỂM THỬ PHÂN HỆ QUẢN LÝ BÀN ĂN (API-TAB-01 -> 05)
# ==============================================================================

class TestTables:
    @property
    def auth_headers(self):
        return {"Authorization": f"Bearer {state['token']}"}

    def test_tc_tab_02_01_create_table_success(self):
        """TC-TAB-02-01: Thêm bàn mới số 99 thành công, sinh mã QR."""
        res = client.post("/admin/tables", headers=self.auth_headers, json={"so_ban": state["so_ban"]})
        assert res.status_code in (200, 201), f"Tạo bàn lỗi: {res.text}"
        data = res.json()
        assert data.get("so_ban") == state["so_ban"]
        assert data.get("trang_thai") == "Trống"
        assert "ma_qr" in data
        state["ma_ban"] = data.get("ma_ban")
        state["ma_qr"] = data.get("ma_qr")

    def test_tc_tab_02_03_create_duplicate_table(self):
        """TC-TAB-02-03: Trùng số bàn -> 422."""
        res = client.post("/admin/tables", headers=self.auth_headers, json={"so_ban": state["so_ban"]})
        assert res.status_code == 422
        err = res.json().get("error", {})
        assert "Số bàn đã tồn tại!" in err.get("message", "")

    def test_tc_tab_01_01_get_tables_list(self):
        """TC-TAB-01-01: Lấy danh sách bàn."""
        res = client.get("/admin/tables", headers=self.auth_headers)
        assert res.status_code == 200
        tables = res.json()
        assert isinstance(tables, list)
        found = any(str(t.get("so_ban")) == state["so_ban"] for t in tables)
        assert found, "Không tìm thấy bàn vừa tạo trong danh sách bàn"

    def test_tc_tab_03_01_get_qr_image(self):
        """TC-TAB-03-01: Tải ảnh mã QR của bàn dạng image/png."""
        res = client.get(f"/admin/tables/{state['ma_ban']}/qr-image", headers=self.auth_headers)
        assert res.status_code == 200
        assert res.headers.get("content-type") == "image/png"
        assert len(res.content) > 100


# ==============================================================================
# 3. KIỂM THỬ PHÂN HỆ QUẢN LÝ MENU (API-MENU-01 -> 04)
# ==============================================================================

class TestMenu:
    @property
    def auth_headers(self):
        return {"Authorization": f"Bearer {state['token']}"}

    def test_tc_menu_02_01_create_item(self):
        """TC-MENU-02-01: Thêm món mới vào menu."""
        payload = {
            "ten_mon": "Cà phê muối Test QA",
            "gia_ban": 32000,
            "hinh_anh": None,
        }
        res = client.post("/admin/menu", headers=self.auth_headers, json=payload)
        assert res.status_code in (200, 201), f"Thêm món lỗi: {res.text}"
        data = res.json()
        assert data.get("ten_mon") == payload["ten_mon"]
        assert data.get("trang_thai") == "Hiển thị"
        state["ma_mon"] = data.get("ma_mon")

    def test_tc_menu_02_05_create_duplicate_name(self):
        """TC-MENU-02-05: Tên món trùng lặp -> 422."""
        payload = {"ten_mon": "  cà phê muối test qa  ", "gia_ban": 30000}
        res = client.post("/admin/menu", headers=self.auth_headers, json=payload)
        assert res.status_code == 422
        err = res.json().get("error", {})
        assert "Tên món đã tồn tại!" in err.get("message", "")

    def test_tc_menu_02_06_create_invalid_price(self):
        """TC-MENU-02-06: Giá bán <= 0 -> 422."""
        payload = {"ten_mon": "Món Giá Sai", "gia_ban": 0}
        res = client.post("/admin/menu", headers=self.auth_headers, json=payload)
        assert res.status_code == 422
        err = res.json().get("error", {})
        assert "Giá bán phải là số lớn hơn 0!" in err.get("message", "")

    def test_tc_menu_01_01_get_menu_admin(self):
        """TC-MENU-01-01: Lấy danh sách menu cho chủ quán."""
        res = client.get("/admin/menu", headers=self.auth_headers)
        assert res.status_code == 200
        items = res.json()
        assert isinstance(items, list)
        found = any(m.get("ma_mon") == state["ma_mon"] for m in items)
        assert found, "Không thấy món vừa tạo trong danh sách menu của admin"

    def test_tc_menu_03_01_update_item(self):
        """TC-MENU-03-01: Cập nhật thông tin món."""
        payload = {"ten_mon": "Cà phê muối Test QA Đặc Biệt", "gia_ban": 35000, "trang_thai": "Hiển thị"}
        res = client.put(f"/admin/menu/{state['ma_mon']}", headers=self.auth_headers, json=payload)
        assert res.status_code == 200


# ==============================================================================
# 4. KIỂM THỬ PHÂN HỆ KHÁCH HÀNG ĐẶT MÓN (API-CUST-01 -> 03)
# ==============================================================================

class TestCustomerOrderFlow:
    def test_tc_cust_01_01_get_customer_menu(self):
        """TC-CUST-01-01: Khách quét QR hợp lệ xem menu và thông tin bàn."""
        res = client.get(f"/customer/menu?qr_token={state['ma_qr']}")
        assert res.status_code == 200, f"Quét QR lỗi: {res.text}"
        data = res.json()
        assert "ban" in data
        assert str(data["ban"].get("so_ban")) == state["so_ban"]
        assert "menu" in data

    def test_tc_cust_01_02_invalid_qr(self):
        """TC-CUST-01-02: Quét mã QR sai -> 404 Mã QR không hợp lệ."""
        res = client.get("/customer/menu?qr_token=invalid_qr_token_123456")
        assert res.status_code == 404
        err = res.json().get("error", {})
        assert "Mã QR không hợp lệ" in err.get("message", "")

    def test_tc_cust_02_01_preview_order(self):
        """TC-CUST-02-01: Tính trước đơn hàng và sinh thông tin VietQR."""
        payload = {
            "qr_token": state["ma_qr"],
            "items": [{"ma_mon": state["ma_mon"], "so_luong": 2}],
            "phuong_thuc_thanh_toan": "Chuyển khoản",
        }
        res = client.post("/customer/orders/preview", json=payload)
        assert res.status_code == 200
        data = res.json()
        assert data.get("tong_tien") == 70000  # 35k * 2
        assert "vietqr_url" in data or "bank_info" in data

    def test_tc_cust_03_01_create_order(self):
        """TC-CUST-03-01: Khách đặt món thành công, bàn chuyển sang Đang phục vụ."""
        payload = {
            "qr_token": state["ma_qr"],
            "items": [{"ma_mon": state["ma_mon"], "so_luong": 2}],
            "phuong_thuc_thanh_toan": "Chuyển khoản",
            "ghi_chu": "Ít ngọt, nhiều đá",
        }
        res = client.post("/customer/orders", json=payload)
        assert res.status_code in (200, 201), f"Đặt món thất bại: {res.text}"
        data = res.json()
        assert "ma_don_hang" in data
        assert data.get("trang_thai") == "Chưa xác nhận thanh toán"
        state["ma_don_hang"] = data.get("ma_don_hang")

        # Kiểm tra trạng thái bàn đã tự động chuyển sang "Đang phục vụ"
        headers = {"Authorization": f"Bearer {state['token']}"}
        res_tab = client.get("/admin/tables", headers=headers)
        target_tab = next((t for t in res_tab.json() if t.get("ma_ban") == state["ma_ban"]), None)
        assert target_tab is not None
        assert target_tab.get("trang_thai") == "Đang phục vụ", "Bàn chưa chuyển sang Đang phục vụ sau khi đặt món!"


# ==============================================================================
# 5. KIỂM THỬ PHÂN HỆ QUẢN LÝ GỌI MÓN & THÔNG BÁO (API-ORD-01 -> 04, API-NOTIF-01)
# ==============================================================================

class TestAdminOrders:
    @property
    def auth_headers(self):
        return {"Authorization": f"Bearer {state['token']}"}

    def test_tc_notif_01_01_polling(self):
        """TC-NOTIF-01-01: Polling kiểm tra đơn mới và số đơn chưa xác nhận."""
        res = client.get("/admin/notifications/unread-orders", headers=self.auth_headers)
        assert res.status_code == 200
        data = res.json()
        assert data.get("unread_count", 0) >= 1

    def test_tc_ord_01_01_get_orders_list(self):
        """TC-ORD-01-01: Lấy danh sách đơn ngày hôm nay."""
        res = client.get("/admin/orders", headers=self.auth_headers)
        assert res.status_code == 200
        orders = res.json()
        assert isinstance(orders, list)
        found = any(o.get("ma_don_hang") == state["ma_don_hang"] for o in orders)
        assert found, "Không tìm thấy đơn hàng vừa đặt trong danh sách hôm nay"

    def test_tc_ord_02_01_get_order_detail(self):
        """TC-ORD-02-01: Xem chi tiết đơn hàng."""
        res = client.get(f"/admin/orders/{state['ma_don_hang']}", headers=self.auth_headers)
        assert res.status_code == 200
        data = res.json()
        assert data.get("ma_don_hang") == state["ma_don_hang"]
        assert "items" in data
        assert len(data["items"]) >= 1

    def test_tc_ord_03_01_confirm_payment(self):
        """TC-ORD-03-01: Xác nhận đã nhận tiền."""
        res = client.patch(f"/admin/orders/{state['ma_don_hang']}/confirm-payment", headers=self.auth_headers)
        assert res.status_code == 200
        # Gọi lại xem trạng thái đơn
        res_chk = client.get(f"/admin/orders/{state['ma_don_hang']}", headers=self.auth_headers)
        assert res_chk.json().get("trang_thai") == "Đã xác nhận thanh toán"

    def test_tc_ord_03_02_confirm_payment_duplicate(self):
        """TC-ORD-03-02: Không cho phép xác nhận 2 lần (BR-UC2-01)."""
        res = client.patch(f"/admin/orders/{state['ma_don_hang']}/confirm-payment", headers=self.auth_headers)
        assert res.status_code in (400, 422), "Hệ thống phải từ chối khi xác nhận lần 2"


# ==============================================================================
# 6. KIỂM THỬ PHÂN HỆ BÁO CÁO DOANH THU (API-REP-01, 02)
# ==============================================================================

class TestReports:
    @property
    def auth_headers(self):
        return {"Authorization": f"Bearer {state['token']}"}

    def test_tc_rep_01_01_get_revenue_by_day(self):
        """TC-REP-01-01: Lấy tổng doanh thu theo ngày."""
        res = client.get("/admin/reports/revenue?period=day", headers=self.auth_headers)
        assert res.status_code == 200
        data = res.json()
        assert "items" in data

    def test_tc_rep_02_01_get_report_details_merged(self):
        """TC-REP-02-01: Endpoint gộp chi tiết doanh thu theo PTTT và thống kê bán hàng."""
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        res = client.get(f"/admin/reports/details?period=day&date={today}", headers=self.auth_headers)
        assert res.status_code == 200
        data = res.json()
        assert "revenue_by_payment_method" in data
        assert "sales_statistics" in data
        stats = data["sales_statistics"]
        assert "tong_so_ly" in stats
        assert "items" in stats


# ==============================================================================
# 7. CLEANUP & KIỂM THỬ XÓA MỀM & QUY TẮC RÀNG BUỘC
# ==============================================================================

class TestCleanupAndBusinessRules:
    @property
    def auth_headers(self):
        return {"Authorization": f"Bearer {state['token']}"}

    def test_tc_tab_04_02_delete_table_in_use_rejected(self):
        """TC-TAB-04-02: Bàn đang phục vụ tuyệt đối không được xóa (BR-UC4-08) -> 400."""
        res = client.delete(f"/admin/tables/{state['ma_ban']}", headers=self.auth_headers)
        assert res.status_code in (400, 422), "Phải chặn xóa bàn đang ở trạng thái Đang phục vụ!"
        err = res.json().get("error", {})
        assert "Chỉ được xóa bàn ở trạng thái Trống" in err.get("message", "")

    def test_tc_tab_05_01_empty_table(self):
        """TC-TAB-05-01: Chuyển bàn đang phục vụ về Trống."""
        res = client.patch(f"/admin/tables/{state['ma_ban']}/empty", headers=self.auth_headers)
        assert res.status_code == 200

    def test_tc_tab_04_01_delete_empty_table_success(self):
        """TC-TAB-04-01: Xóa bàn khi đã Trống thành công (xóa mềm)."""
        res = client.delete(f"/admin/tables/{state['ma_ban']}", headers=self.auth_headers)
        assert res.status_code == 200

    def test_tc_menu_04_01_delete_menu_item(self):
        """TC-MENU-04-01: Xóa mềm món ăn thành công."""
        res = client.delete(f"/admin/menu/{state['ma_mon']}", headers=self.auth_headers)
        assert res.status_code == 200

    def test_tc_ord_04_01_delete_order(self):
        """TC-ORD-04-01: Xóa mềm đơn hàng thành công."""
        res = client.delete(f"/admin/orders/{state['ma_don_hang']}", headers=self.auth_headers)
        assert res.status_code == 200
