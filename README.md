این ریو برای تست n8n می باشد.
## نحوه راه‌اندازی پروژه پایتون

### پیش‌نیازها (نسخهٔ پایتون توصیه‌شده)
- Python 3.8 تا 3.11 (توصیه: 3.11.x)

### ایجاد و فعال‌سازی محیط مجازی (virtual environment)
- Linux/macOS:
  - python3 -m venv venv
  - source venv/bin/activate
- Windows:
  - py -3 -m venv venv
  - .\\venv\\Scripts\\activate

### نصب وابستگی‌ها
- pip install --upgrade pip
- اگر فایل requirements.txt وجود دارد:
  - pip install -r requirements.txt
- اگر فایل requirements.txt وجود ندارد:
  - pip install <نام-کتابخانه-ها>

### نحوه اجرای اسکریپت/نمونه‌ها
- اجرای مستقیم utils_math.py:
  - python utils_math.py
- یا استفاده در REPL:
  - python
  - from utils_math import *
  - # اکنون می‌توانید توابع موجود را استفاده کنید
  - مثال: اگر تابعی با نام add وجود داشته باشد: print(add(2, 3))

### نکات اختیاری برای غیرفعال‌سازی محیط مجازی
- deactivate