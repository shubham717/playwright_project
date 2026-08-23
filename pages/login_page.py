from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.email_input = "[data-test='email']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-submit']"
        self.error_message = "[data-test='login-error']"

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/auth/login")

    def login(self, email_str, password_str):
        self.page.fill(self.email_input, email_str)
        self.page.fill(self.password_input, password_str)
        self.page.click(self.login_button)
        
    def get_error_text(self):
        """Returns the text of the error message if login fails."""
        return self.page.locator(self.error_message).text_content()
        

