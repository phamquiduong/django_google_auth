# Ứng dụng Django lấy refresh token của Google Auth2

# Tạo google app và lấy client secret
Link tham khảo: https://developers.google.com/identity/protocols/oauth2

Thêm Authorized redirect URIs đường dẫn `http://localhost/google/oauth2callback`

# Các bước cài đặt server
## Cài đặt python3
Truy cập http://python.org/ để tải bản python mới nhất.

Với hệ điều hành Ubuntu (linux) dùng lệnh
```bash
sudo apt install python3 pip3
```

## Sử dụng python3
```bash
# Với hệ điều hành Windows, sử dụng lệnh `python` và `pip`
# Với hệ điều hành MacOS/Linux, sử dụng lệnh `python3` và `pip3`
```

## Chỉnh sửa các env
```bash
# Chỉnh sửa các env trong file core/env.py
# Mình hơi lười nên chưa làm cái load_dotenv
```

## Cài đặt thư viện hỗ trợ
Chạy lệnh
```bash
pip install -r requirements.txt
```

## Vào thư mục source code
```bash
cd src/
```

## Khởi tạo database
```bash
python manage.py migrate
```

## Tạo tài khoản admin
```bash
python manage.py createsuperuser
# Và điền username, email (option), password
```

## Chạy server
```bash
python manage.py runserver 0.0.0.0:80
```

## Truy cập đường dẫn để thử xác thực với google
```bash
localhost/google/auth
# Nó trả về success là đã thành công rồi.
# Check refresh token trong database sqllite bảng google_auth_user
```

# Chúc các bạn thành công!