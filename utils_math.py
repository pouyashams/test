def add(a, b):
    return a + b

class Adder:
    """کلاسی ساده برای جمع دو عدد."""

    def add(self, a, b):
        """دو عدد a و b را گرفته و حاصل جمع را برمی‌گرداند."""
        return a + b

    def fibonacci(self, n):
        """عدد nام دنباله فیبوناچی را برمی‌گرداند.

        قرارداد: fibonacci(0) = 0 و fibonacci(1) = 1

        ورودی باید یک عدد صحیح غیرمنفی باشد؛ در غیر این صورت ValueError پرتاب می‌شود.
        پیاده‌سازی به صورت تکراری و با پیچیدگی زمانی O(n) و فضای O(1) انجام شده است.
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("n باید یک عدد صحیح غیرمنفی باشد")
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
