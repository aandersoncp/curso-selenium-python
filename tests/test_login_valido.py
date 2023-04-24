import pytest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.login_page import LoginPage
import conftest
import time

@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.login
#@pytest.mark.smoke
class TestCT02:

    def test_ct02_login_valido(self):
        home_page = HomePage()
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.verificar_login_com_sucesso()
