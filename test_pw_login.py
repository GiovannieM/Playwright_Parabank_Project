from playwright.sync_api import Page, expect 
from pw_login_page import PWLoginPage
from pw_accounts_page import PWAccountsPage 

user = 'timtom'
passwrd = 'whatspasswrd'

def test_pw_successful_login(page: Page):
    login = PWLoginPage(page)
    login.open()
    login.login(user, passwrd)
    expect(login.logout_link).to_be_visible()

def test_pw_accounts_table_has_rows(page: Page):
    login = PWLoginPage(page)
    login.open()
    login.login(user, passwrd)

    accounts = PWAccountsPage(page)
    accounts.open()
    # '.first' is the first matching element
    expect(accounts.account_links.first).to_be_visible() ## similiar to assert 
