# TỔNG QUAN (OVERVIEW)

## Mục đích của tài liệu (Purpose)

Tài liệu Đặc tả Yêu cầu Phần mềm và Thiết Kế Hệ Thống này được xây dựng nhằm trình bày các yêu cầu chức năng và yêu cầu phi chức năng của dự án Hệ thống quản lý bán hàng tại quán Cà phê 458. Tài liệu giúp nhóm thống nhất về những yêu cầu mà hệ thống cần đáp ứng trong quá trình phân tích, thiết kế, xây dựng và kiểm thử hệ thống.

Thông qua tài liệu này, các thành viên trong nhóm có thể hiểu rõ hơn về mục tiêu, phạm vi và các chức năng chính của hệ thống. Đây cũng là cơ sở để nhóm thực hiện các bước tiếp theo của dự án và đảm bảo hệ thống được xây dựng phù hợp với nhu cầu thực tế của quán.

## Tổng quan hệ thống (Business objectives)

Dự án Hệ thống quản lý bán hàng được xây dựng dựa trên tình hình hoạt động thực tế tại quán Cà phê 458, địa chỉ 458 Nguyễn Duy Trinh, phường Ngũ Hành Sơn, thành phố Đà Nẵng. Quán đã hoạt động được 8 năm dưới sự quản lý trực tiếp của cô Mai Thị Bích Nguyệt, phục vụ khách hàng từ 5 giờ sáng đến 5 giờ chiều mỗi ngày. Quán có quy mô nhỏ và hoạt động độc lập, trong đó chủ quán đảm nhận hầu hết các công việc như tiếp khách, ghi nhận order, pha chế, phục vụ, thu tiền và ghi chép sổ sách. Tuy nhiên, khi lượng khách tăng lên, cách làm thủ công này bắt đầu gây ra một số khó khăn. Chủ quán phải đi đến từng bàn để hỏi món và ghi lại bằng giấy nên mất nhiều thời gian, đồng thời dễ xảy ra nhầm lẫn. Bên cạnh đó, việc ghi nhận doanh thu bằng tiền mặt còn phụ thuộc nhiều vào việc chủ quán tự ghi nhớ và ghi chép, nên đôi khi có thể quên các khoản tiền nhỏ, làm cho việc kiểm tra doanh thu cuối ngày mất thêm thời gian.

Từ những vấn đề trên, dự án được thực hiện với mục tiêu hỗ trợ quán giảm bớt các công việc thủ công và quản lý việc bán hàng thuận tiện hơn. Hệ thống hướng đến việc cho phép khách hàng chủ động đặt món bằng cách quét mã QR, giúp giảm thời gian chủ quán phải đi lại giữa các bàn và có thể tập trung hơn vào việc pha chế, phục vụ. Đồng thời, hệ thống hỗ trợ chủ quán quản lý đơn hàng, thực đơn, thanh toán và doanh thu trên cùng một hệ thống. Các thông tin bán hàng được lưu lại để chủ quán có thể dễ dàng kiểm tra và xem lại khi cần. Qua đó, hệ thống góp phần giảm bớt sai sót trong quá trình bán hàng, giảm công việc ghi chép thủ công và giúp việc quản lý quán thuận tiện hơn.

## Phạm vi hệ thống (Scope)

### **Phạm vi tổ chức (**Organization Scope)

Cà phê 458 là quán cà phê có quy mô nhỏ, chỉ hoạt động tại một cơ sở và không chia thành các phòng ban riêng, nên hệ thống sẽ được áp dụng cho toàn bộ quán.

### **Phạm vi người dùng** (User Scope)

Hệ thống quản lý bán hàng Cà phê 458 sẽ bao gồm có hai nhóm người sử dụng chính là: chủ quán và khách hàng.

### **Phạm vi chức năng** (Functional Scope)

Dựa trên các mục tiêu đã đề ra, hệ thống tập trung vào những chức năng chính phục vụ cho việc quản lý và bán hàng tại quán Cà phê 458. Các chức năng được chia thành hai nhóm chính là chức năng dành cho chủ quán và chức năng dành cho khách hàng.

- **Chức năng dành cho Chủ quán:**

  - Đăng nhập, đổi mật khẩu, đăng xuất hệ thống

  - Tiếp nhận đơn mới, xem chi tiết đơn, cập nhật trạng thái đơn, xóa đơn, xác nhận đã nhận tiền

  - Theo dõi tình trạng bàn, thêm bàn, xóa bàn, xác nhận bàn trống

  - Quản lý thực đơn: thêm, xóa, cập nhật thông tin và giá món, ẩn hoặc hiển thị món

  - Xem doanh thu, số ly bán ra và món bán chạy theo ngày, tháng, năm

- **Chức năng dành cho Khách hàng:**

  - Quét mã QR tại bàn để truy cập hệ thống

  - Xem thực đơn, chọn món, điều chỉnh số lượng, nhập ghi chú cho đơn (nếu cần)

  - Chọn phương thức thanh toán, xem mã QR để chuyển khoản

### **Phạm vi tích hợp** (Integration Scope)

Để hỗ trợ khách hàng thanh toán bằng hình thức chuyển khoản, hệ thống sẽ kết nối với hệ thống ngân hàng để thực hiện thanh toán bằng mã QR. Mã QR được tạo dựa trên thông tin tài khoản của chủ quán và số tiền của đơn hàng, giúp khách hàng có thể quét mã và chuyển khoản đúng số tiền mà không cần nhập lại thông tin thủ công.

### **Ngoài phạm vi** (Out of Scope)

Để phù hợp với quy mô của quán và phạm vi của đồ án, một số chức năng sẽ không được phát triển trong hệ thống. Cụ thể, hệ thống chỉ được xây dựng trên nền tảng web và không phát triển ứng dụng dành cho điện thoại. Hệ thống cũng không gửi thông báo ra ngoài hệ thống (Zalo, SMS, email), thông báo đơn mới chỉ phát ngay trên hệ thống, quản lý kho và nguyên vật liệu, quản lý nhân viên và chăm sóc khách hàng như tích điểm hoặc voucher giảm giá. Hệ thống không tự xác minh giao dịch chuyển khoản, chủ quán tự kiểm tra tiền đã vào tài khoản rồi xác nhận trên hệ thống.

## Ràng buộc thiết kế (Design Constraints)

Các ràng buộc dưới đây giới hạn cách nhóm thiết kế hệ thống, xuất phát từ điều kiện thực hiện đồ án và đặc điểm vận hành của quán Cà phê 458.

### **Ràng buộc chung** (General constraints)

- Chỉ làm các chức năng trong phạm vi đã chốt.

- Ưu tiên giải pháp đơn giản, dễ làm và dễ kiểm thử.

- Quán có quy mô nhỏ, chỉ một cơ sở, khoảng 20 bàn và 50 món, do chủ quán trực tiếp quản lý; hệ thống chỉ có một tài khoản chủ quán, không phân quyền, nhưng vẫn cho phép thêm bàn và thêm món khi quán mở rộng.

- Khách hàng không cần tài khoản; mỗi bàn được nhận biết qua mã QR riêng dán tại bàn.

- Hệ thống không kết nối ngân hàng và không tích hợp thanh toán trực tuyến; mã QR chuyển khoản chỉ để khách quét, chủ quán tự kiểm tra tiền vào tài khoản rồi xác nhận trên hệ thống.

### **Ràng buộc phần cứng** (Hardware constraints)

- Khách hàng dùng điện thoại cá nhân có camera để quét mã QR tại bàn; chủ quán chủ yếu dùng điện thoại để nhận và xử lý đơn, nên giao diện phải hiển thị tốt trên màn hình nhỏ, đồng thời dùng được trên máy tính.

- Không yêu cầu thiết bị chuyên dụng như máy POS hay máy in hóa đơn; người dùng chỉ cần điện thoại hoặc máy tính có kết nối Internet. Mã QR của từng bàn được in ra giấy và dán tại bàn.

### **Ràng buộc phần mềm** (SW constraints)

- Hệ thống chạy trên nền web, truy cập bằng trình duyệt phổ biến (Chrome, Safari, Edge), không cần cài ứng dụng; khách hàng mở menu trực tiếp sau khi quét mã QR.

- Dùng hệ quản trị cơ sở dữ liệu quan hệ để lưu tài khoản chủ quán, bàn, món, đơn hàng và chi tiết đơn; dữ liệu bàn, món, đơn chỉ đánh dấu xóa, không xóa hẳn.

- Mật khẩu của chủ quán được lưu ở dạng mã hóa.

- Hệ thống tự thông báo đơn mới ngay trên giao diện của chủ quán; không gửi thông báo qua Zalo, SMS hay email.

- Mã QR chuyển khoản được tạo từ thông tin tài khoản ngân hàng của chủ quán và số tiền của đơn, nội dung chuyển khoản gồm số bàn.

# MÔ TẢ TỔNG QUAN (OVERALL DESCRIPTION)

## Yêu cầu người dùng (User requirements)

Dựa trên kết quả khảo sát và tìm hiểu thực tế tại quán Cà phê 458, các yêu cầu của hệ thống được chia thành hai nhóm chính**:** Yêu cầu nghiệp vụ và Yêu cầu của các bên liên quan**.**

### **Yêu cầu nghiệp vụ** (Business requirement)

|  |  |
|:--:|:--:|
| **ID** | **Requirement** |
| **BR-01** | Giảm thời gian chờ và thao tác thủ công trong quá trình tiếp nhận đơn hàng bằng cách cho phép khách hàng tự đặt món tại bàn. |
| **BR-02** | Hạn chế tối đa sai sót và thất thoát tài chính trong việc ghi nhận đơn hàng, tính tiền và ghi nhận, tổng hợp doanh thu. |
| **BR-03** | Hỗ trợ chủ quán quản lý tập trung toàn bộ hoạt động kinh doanh (thực đơn, đơn hàng, tình trạng bàn, doanh thu/ thống kê) trên một nền tảng duy nhất. |
| **BR-04** | Nâng cao khả năng theo dõi tình trạng phục vụ của từng bàn kịp thời để chủ quán kiểm soát chất lượng phục vụ. |
| **BR-05** | Tự động hóa quá trình tổng hợp số liệu bán hàng nhằm giảm tải thời gian cộng sổ thủ công cuối ngày. |
| **BR-06** | Nâng cao chất lượng dịch vụ thông qua trải nghiệm gọi món và thanh toán linh hoạt (tiền mặt hoặc chuyển khoản), không yêu cầu cài đặt ứng dụng. |
| **BR-07** | Đảm bảo tính bảo mật và an toàn cho dữ liệu kinh doanh của quán thông qua cơ chế kiểm soát truy cập bằng tài khoản. |

*Bảng 1. Danh sách yêu cầu nghiệp vụ*

### **Yêu cầu của các bên liên quan** (Stakeholder requirements)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>Stakeholder</strong></td>
<td style="text-align: center;"><strong>Requirement</strong></td>
</tr>
<tr>
<td rowspan="6" style="text-align: center;"><strong>Chủ quán</strong></td>
<td style="text-align: center;">Đăng nhập vào hệ thống quản lý bằng tài khoản và mật khẩu cá nhân, và đổi mật khẩu khi cần để bảo mật dữ liệu kinh doanh.</td>
</tr>
<tr>
<td style="text-align: center;">Tiếp nhận order mới kèm thông báo trên hệ thống; xem chi tiết order (mã đơn, số bàn, tên món, số lượng, giá, tổng tiền, thời gian đặt, phương thức thanh toán, ghi chú, trạng thái đơn); cập nhật trạng thái và xóa đơn.</td>
</tr>
<tr>
<td style="text-align: center;">Theo dõi và quản lý sơ đồ bàn (thêm, xóa bàn) theo 2 trạng thái: Trống, Đang phục vụ.</td>
</tr>
<tr>
<td style="text-align: center;">Xác nhận đã nhận tiền (tiền mặt hoặc chuyển khoản) để chốt đơn, tự động ghi nhận doanh thu và thời gian giao dịch.</td>
</tr>
<tr>
<td style="text-align: center;">Quản lý thực đơn: thêm món mới, xóa món cũ, cập nhật giá, bật/tắt hiển thị món.</td>
</tr>
<tr>
<td style="text-align: center;">Xem thống kê theo ngày, tháng, năm: doanh thu tổng, tiền mặt, chuyển khoản, số ly bán ra, món bán chạy nhất.</td>
</tr>
<tr>
<td rowspan="3" style="text-align: center;"><strong>Khách hàng</strong></td>
<td style="text-align: center;">Quét mã QR riêng của từng bàn (hệ thống tự nhận biết số bàn) để truy cập hệ thống gọi món mà không cần tải ứng dụng.</td>
</tr>
<tr>
<td style="text-align: center;">Xem thực đơn (kèm hình ảnh minh họa, gợi ý món đề cử), chọn món, tùy chỉnh số lượng, nhập ghi chú cho đơn.</td>
</tr>
<tr>
<td style="text-align: center;">Thanh toán bằng phương thức chuyển khoản (quét mã QR ngay sau khi đặt) hoặc thanh toán bằng tiền mặt (trả khi nhận món tại bàn)</td>
</tr>
</tbody>
</table>

*Bảng 2. Danh sách yêu cầu của các bên liên quan*

## Quy trình nghiệp vụ (Business workflow)

<img src="media/image1.png" style="width:6.5in;height:2.29931in" />

*Hình 1. Mô hình quy trình nghiệp vụ (BPMN) hệ thống quản lý Cà phê 458*

## Sơ đồ Use Case (Use case diagram)

<img src="media/image2.png" style="width:6.5in;height:5.06944in" />

*Hình 2. Sơ đồ Use Case tổng quát hệ thống quản lý bán hàng Cà phê 458*
