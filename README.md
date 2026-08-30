این ریو برای تست n8n می باشد.

## نحوه راه‌اندازی

- پیش‌نیازها: نصب Python نسخه 3.8 یا جدیدتر.

- ایجاد و فعال‌سازی محیط مجازی:
  - لینوکس/macOS:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
  - ویندوز (PowerShell):
    ```powershell
   .\venv\Scripts\Activate.ps1
    ```
  - ویندوز (Command Prompt):
    ```cmd
    venv\Scripts\activate.bat
    ```

- نصب وابستگی‌ها در صورت وجود فایل requirements.txt:
  ```bash
  pip install -r requirements.txt
  ```
  اگر فایل وجود ندارد این مرحله را نادیده بگیرید.

- نحوه اجرای و تست سریع:
  نمونه‌ای ایمن که وابستگی خاصی را مفروض نمی‌گیرد، مثلاً اجرای دستور نمونه برای مشاهده محتویات ماژول با استفاده از کتابخانه استاندارد os:
  ```bash
  python -c 'import os; print(dir(os))'
  ```
  همچنین می‌توانید از REPL پایتون نیز استفاده کنید:
  ```bash
  python
  >>> import os
  >>> dir(os)
  >>> ...
  ```

- نکات اختیاری:
  - غیرفعال‌سازی محیط مجازی:
    ```bash
    deactivate
    ```
  - و اضافه کردن دستورالعمل‌های بیشتر در صورت توسعه پروژه.
