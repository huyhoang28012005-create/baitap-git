import unittest
from unittest.mock import patch, Mock
import requests
from datetime import datetime

# Bài 1: Hàm tính thuế
def calculate_tax(income):
    if income < 5000: 
        return 0
    elif income < 10000: 
        return income * 0.1
    else: 
        return income * 0.2

class TestCalculateTax(unittest.TestCase):
    def test_calculate_tax(self):
        self.assertEqual(calculate_tax(4000), 0)
        self.assertEqual(calculate_tax(7000), 700.0)
        self.assertEqual(calculate_tax(12000), 2400.0)

# Bài 2: Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))

# Bài 3: Lớp User
class User:
    def __init__(self, username):
        self.username = username
    def is_admin(self):
        return self.username == "admin"

class TestUser(unittest.TestCase):
    def test_user_is_admin(self):
        self.assertTrue(User('admin').is_admin())
        self.assertFalse(User('guest').is_admin())

# Bài 4: Hàm gửi email (Mocking)
def send_welcome_email(email):
    print(f"Sending email to {email}")

class TestSendWelcomeEmail(unittest.TestCase):
    @patch('builtins.print')
    def test_send_welcome_email(self, mock_print):
        send_welcome_email("test@example.com")
        mock_print.assert_called_with("Sending email to test@example.com")

# Bài 5: Hàm gọi API (Mocking)
def fetch_user():
    response = requests.get("https://api.example.com/user")
    return response.json()

class TestFetchUser(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_user(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "name": "Test User"}
        mock_get.return_value = mock_response

        result = fetch_user()
        self.assertEqual(result, {"id": 1, "name": "Test User"})
        mock_get.assert_called_once_with("https://api.example.com/user")

# Bài 6: Hàm kiểm tra ngày cuối tuần (Mocking)
def is_weekend():
    today = datetime.now().weekday()
    return today >= 5

class TestIsWeekend(unittest.TestCase):
    # Patch datetime tại module hiện tại (nơi script đang chạy)
    @patch(f"{__name__}.datetime")
    def test_is_weekend(self, mock_datetime):
        mock_datetime.now.return_value.weekday.return_value = 4
        self.assertFalse(is_weekend())
        mock_datetime.now.return_value.weekday.return_value = 5
        self.assertTrue(is_weekend())

# Bài 7: Hàm kiểm tra độ mạnh mật khẩu
def is_strong(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)

class TestIsStrong(unittest.TestCase):
    def test_is_strong(self):
        self.assertTrue(is_strong("Password123"))
        self.assertFalse(is_strong("Pass123"))
        self.assertFalse(is_strong("Password"))

# Bài 8: Hàm làm sạch chuỗi input
def clean_input(s):
    return s.strip().lower().replace(" ", "_")

class TestCleanInput(unittest.TestCase):
    def test_clean_input(self):
        self.assertEqual(clean_input("  HELLO World  "), "hello_world")
        self.assertEqual(clean_input("NoSpacesHere"), "nospaceshere")
        self.assertEqual(clean_input("Multiple   Spaces"), "multiple___spaces")

# Bài 9: Hàm chia số an toàn
def safe_divide(a, b):
    if b == 0: 
        return None
    return a / b

class TestSafeDivide(unittest.TestCase):
    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5.0)
        self.assertEqual(safe_divide(-4, 2), -2.0)
        self.assertIsNone(safe_divide(5, 0))

if __name__ == '__main__':
    unittest.main()