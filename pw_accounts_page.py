from playwright.sync_api import Page 

class PWAccountsPage:
    url = 'https://parabank.parasoft.com/parabank/overview.htm'

    def __init__(self, page: Page):
        self.page = page 
        self.account_links = page.locator('#accountTable tbody tr td a')

    def open(self):
        self.page.goto(self.url)