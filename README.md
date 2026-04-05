# 🎬 Movie Theater Management - API Testing Module

Dự án này tập trung vào việc xây dựng và kiểm thử hệ thống xác thực (Authentication) cho ứng dụng quản lý rạp chiếu phim bằng **Flask** và **Pytest**.

## 🛠️ Mã nguồn & Cài đặt

Dự án đã được thiết lập đầy đủ môi trường kiểm thử với cơ sở dữ liệu SQLite (in-memory) để đảm bảo tốc độ và tính cô lập khi test.

### 1. Kích hoạt môi trường ảo

Trước tiên, bạn cần mở Terminal tại thư mục dự án và chạy lệnh:

- **Trên macOS/Linux:**
  ```bash
  source env/bin/activate
  ```
- **Trên window:**
  ```bash
  .\env\Scripts\activate
  ```

### 2. Cài đặt thư viện

    ```
    pip install -r requirements.txt
    ```

### 3. Cách chạy kiểm thử

    ```python -m pytest -v```

###

## 📝 Tóm tắt các kịch bản kiểm thử (Test Cases)

Hệ thống đã hoàn thành **16 kiểm thử tự động** bao gồm các luồng chính (Happy Path) và các luồng xử lý lỗi (Edge Cases).

### 1. Luồng Đăng ký (Signup)

| Trạng thái | Kịch bản kiểm thử       | Mô tả logic                                                             |
| :--------: | :---------------------- | :---------------------------------------------------------------------- |
|     ✅     | **Đăng ký thành công**  | Tạo tài liệu người dùng mới vào database khi dữ liệu hợp lệ.            |
|     ❌     | **Thiếu Email/SĐT**     | Hệ thống trả về lỗi 400 nếu các trường bắt buộc bị trống.               |
|     ❌     | **Email đã tồn tại**    | Ngăn chặn việc đăng ký trùng lặp để bảo vệ tính duy nhất của tài khoản. |
|     ❌     | **SĐT đã tồn tại**      | Đảm bảo mỗi số điện thoại chỉ gắn liền với một định danh duy nhất.      |
|     ❌     | **Mật khẩu không khớp** | Kiểm tra tính chính xác giữa mật khẩu và trường xác nhận.               |
|     ❌     | **Mật khẩu quá ngắn**   | Ràng buộc bảo mật: Mật khẩu phải có độ dài từ 8 ký tự trở lên.          |
|     ✅     | **Mật khẩu vừa đủ**     | Kiểm tra giá trị biên (boundary check) với độ dài đúng 8 ký tự.         |

### 2. Luồng Đăng nhập (Login)

- ✅ **Đăng nhập thành công**: Xác thực thông tin và trả về mã **Token** trong Header/Body.
- ❌ **Sai mật khẩu**: Kiểm tra cơ chế so sánh giữa mật khẩu nhập vào và mã Hash trong DB.
- ❌ **Thiếu Token**: Đảm bảo các route bảo mật yêu cầu Header `Auth` hợp lệ.
- ❌ **Tài khoản không tồn tại**: Trả về lỗi cụ thể nếu Email/SĐT chưa được đăng ký.
- ❌ **Để trống định danh**: Yêu cầu người dùng phải nhập Email hoặc Số điện thoại.
- ❌ **Để trống mật khẩu**: Ngăn chặn truy cập nếu thiếu thông tin xác thực.

### 3. Luồng Quên & Đổi mật khẩu (Forgot Password)

- ✅ **Đổi mật khẩu thành công**: Truyền đúng thông tin cá nhân -> Đổi Pass -> Đăng nhập lại bằng Pass mới OK.
- ❌ **Thông tin cá nhân sai**: Kiểm tra chéo các trường `address`, `city`, `country`... nếu không khớp sẽ từ chối cấp quyền đổi Pass.
- ✅ **Gán mật khẩu mặc định**: Nếu người dùng không nhập mật khẩu mới, hệ thống tự động gán giá trị mặc định là `"123456789"`.
- ❌ **Truy cập trái phép**: Ngăn chặn việc gọi trực tiếp API `/new-password` khi chưa vượt qua bước xác thực tại `/forgot-password`.

---

_Ghi chú: Tất cả các trường hợp trên đều trả về dữ liệu định dạng **JSON** thông qua `jsonify` để hỗ trợ tốt nhất cho phía Frontend._
