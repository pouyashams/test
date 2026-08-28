این ریو برای تست n8n می باشد.

نحوه راه اندازی پروژه:
1) پیش‌نیازها:
   - داشتن Python 3 روی سیستم.
2) دریافت کد:
   - کلون کردن یا دانلود مخزن و ورود به پوشه پروژه.
     مثال: git clone <repo-url> && cd <repo-name>
3) ایجاد و فعال‌سازی محیط مجازی:
   - ایجاد: python -m venv venv
   - فعال‌سازی در لینوکس/مک: source venv/bin/activate
   - فعال‌سازی در ویندوز: venv\Scripts\activate
4) نصب وابستگی‌ها (در صورت وجود فایل requirements.txt):
   - pip install -r requirements.txt
   - اگر فایل requirements.txt موجود نباشد می‌توانید این مرحله را نادیده بگیرید یا وابستگی‌ها را دستی نصب کنید.
5) اجرای تست سریع برای اطمینان از در دسترس بودن ماژول utils_math:
   - اجرای سریع: python -c "import utils_math; print(dir(utils_math))"
   - یا باز کردن REPL با python و سپس وارد کردن: import utils_math
توضیح کوتاه:
   در حال حاضر پروژه فاقد اسکریپت اجرایی مشخص است. برای بررسی اولیه پیشنهاد می‌شود از ماژول utils_math استفاده کنید.
