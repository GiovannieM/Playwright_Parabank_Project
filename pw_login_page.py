from playwright.sync_api import Page

class PWLoginPage:
    url = 'https://parabank.parasoft.com/'

    def __init__(self, page: Page):
        self.page = page # same as 'Driver' 
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_button = page.locator("input[value='Log In']")
        self.logout_link = page.get_by_role("link", name= "Log out") # finds eleemnt as seen on page 

    def open(self):
        self.page.goto(self.url)

    def login(self, user, passwrd):
        self.username.fill(user)
        self.password.fill(passwrd)
        self.login_button.click()