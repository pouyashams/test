# معرفی کوتاه به پایتون (برای مبتدی‌ها)

پایتون یک زبان برنامه‌نویسی سطح بالا، خوانا و همه‌منظوره است که برای یادگیری آسان و توسعهٔ سریع کاربرد دارد. پایتون هم در زمینهٔ توسعهٔ وب، هم علم داده، اتوماسیون، اسکریپت‌نویسی، و هم تولید نرم‌افزارهای عمومی بسیار محبوب است.

چه کارهایی می‌توان با پایتون انجام داد؟
- ساخت وب‌سایت و API (با فریم‌ورک‌هایی مثل Django و Flask)
- پردازش داده و یادگیری ماشین (با کتابخانه‌هایی مثل pandas و scikit-learn)
- خودکارسازی کارهای تکراری و اسکریپت‌نویسی
- ساخت ابزارهای خط فرمان و برنامه‌های دسکتاپ

نحوهٔ نصب (کلی)
- به وب‌سایت رسمی پایتون مراجعه کنید: https://www.python.org
- یا از مدیر بستهٔ سیستم خود استفاده کنید:
  - روی Ubuntu/Debian: `sudo apt install python3`
  - روی macOS (با Homebrew): `brew install python` یا از بسته رسمی استفاده کنید
  - روی Windows: از نصب‌کنندهٔ رسمی استفاده کنید یا از Chocolatey: `choco install python`
- برای نصب بسته‌ها از `pip` استفاده می‌شود: `pip install package-name` (در برخی سیستم‌ها دستور `pip3` یا اجرای pip در محیط مجازی رایج است).

اجرای یک اسکریپت ساده
- فایل Python را با پسوند `.py` ذخیره کنید، مثلاً `hello.py`، سپس اجرا کنید:
  - `python hello.py` یا در سیستم‌هایی که هم Python 2 و هم 3 نصب است: `python3 hello.py`.

انواع دادهٔ پایه و ساختارهای کنترلی (مختصر)
- متغیرها: نیازی به تعریف نوع صریح ندارند، نمونه: `x = 10`
- عددها: `int`, `float`
- رشته‌ها: `str`، مثال: `name = "Ali"`
- لیست‌ها: `list`، مثال: `nums = [1, 2, 3]`
- تاپل‌ها: `tuple`، مثال: `t = (1, 2)`
- فرهنگ‌نامه‌ها: `dict`، مثال: `d = {"key": "value"}`
- مجموعه‌ها: `set`
- بولی: `True` / `False`

کنترل جریان:
- شرط‌ها: `if`, `elif`, `else`
- حلقه‌ها: `for`, `while`
- توابع: با `def` تعریف می‌شوند

نمونهٔ کد بسیار ساده

```python
# چاپ متن
print("سلام دنیا")

# تابع ساده
def greet(name):
    return f"سلام، {name}!"

print(greet("نواف"))

# حلقه و لیست
numbers = [1, 2, 3, 4]
sum_ = 0
for n in numbers:
    sum_ += n
print("مجموع:", sum_)
```

محیط‌های مجازی (virtual environments)
- استفاده از محیط مجازی باعث جدا ماندن بسته‌ها بین پروژه‌ها می‌شود.
- ایجاد و فعال‌سازی با venv:
  - ایجاد: `python -m venv venv` (اگر لازم است از `python3 -m venv venv` استفاده کنید)
  - فعال‌سازی در macOS/Linux: `source venv/bin/activate`
  - فعال‌سازی در Windows (PowerShell): `venv\Scripts\Activate.ps1`
  - فعال‌سازی در Windows (Command Prompt): `venv\Scripts\activate`
  - پس از فعال‌سازی، از `pip install` برای نصب بسته‌ها استفاده کنید.

نحوهٔ راه‌اندازی پروژه

این بخش مراحل گام‌به‌گام برای آماده‌سازی و اجرای این مخزن را توضیح می‌دهد تا کسی که پروژه را کلون می‌کند بتواند سریع آن را اجرا کند.

پیش‌نیاز
- Python 3 نصب شده روی سیستم (برای بررسی: `python --version` یا `python3 --version`).

کلون کردن مخزن

```bash
git clone https://github.com/pouyashams/test.git
cd test
```

ایجاد و فعال‌سازی محیط مجازی

```bash
# ایجاد محیط مجازی
python -m venv venv
# یا اگر روی سیستم‌تان python به نسخهٔ 2 اشاره می‌کند:
# python3 -m venv venv

# فعال‌سازی در macOS / Linux:
source venv/bin/activate

# فعال‌سازی در Windows (PowerShell):
venv\Scripts\Activate.ps1

# فعال‌سازی در Windows (Command Prompt):
venv\Scripts\activate
```

به‌روزرسانی pip

```bash
python -m pip install --upgrade pip
# یا در صورت نیاز: python3 -m pip install --upgrade pip
```

نصب وابستگی‌ها
- در این مخزن فایلی مانند requirements.txt وجود ندارد و وابستگی خارجی مشخص نشده است. اگر پروژه‌ای نیاز به بسته‌های خارجی داشت، می‌توانید آن‌ها را با `pip install package-name` نصب کنید یا یک فایل requirements.txt ایجاد و سپس با `pip install -r requirements.txt` نصب کنید.
- اگر بعداً requirements.txt اضافه شد، دستور زیر وابستگی‌ها را نصب می‌کند:

```bash
pip install -r requirements.txt
```

چگونه کدها را اجرا یا امتحان کنیم
- اگر فایل utils_math.py در ریشهٔ مخزن موجود است، می‌توانید آن را به صورت مستقیم در مفسر پایتون وارد و امتحان کنید:

```bash
# نمایش محتوای ماژول و عملکردهای آن
python -c "import utils_math; print(dir(utils_math))"
# اگر سیستم شما از python3 استفاده می‌کند:
# python3 -c "import utils_math; print(dir(utils_math))"

# یا باز کردن مفسر پایتون و وارد کردن ماژول:
python
>>> import utils_math
>>> dir(utils_math)
```

- اگر utils_math.py اسکریپتی قابل اجرا دارد، ممکن است بتوانید آن را مستقیم اجرا کنید:

```bash
python utils_math.py
# یا
python3 utils_math.py
```

- اگر فایل utils_math.py در مسیر دیگری قرار دارد یا نام متفاوت است، نام صحیح فایل را بررسی کنید یا از دستورls / dir برای دیدن فایل‌های موجود استفاده کنید.

دلیل این بخش
- اضافه کردن این راهنمای گام‌به‌گام باعث می‌شود خوانندگان مبتدی بدانند چگونه محیط را آماده کنند و چگونه فایل‌های این پروژه را اجرا یا تست کنند.

منابع برای یادگیری بیشتر
- مستندات رسمی: https://docs.python.org/3/
- آموزش‌ها و دوره‌های مبتدی (مثل "Automate the Boring Stuff with Python")
- سایت‌های تعاملی: w3schools، freeCodeCamp، Codecademy
- ویدئوها و دوره‌های آموزشی در پلتفرم‌هایی مثل YouTube و Coursera

پایان
- این متن یک معرفی ساده و مقدماتی است؛ برای یادگیری واقعی بهتر است پروژه‌های کوچک انجام دهید و از منابع بالا استفاده کنید.
