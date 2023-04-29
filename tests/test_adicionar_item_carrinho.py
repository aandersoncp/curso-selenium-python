import pytest
from pages import login_page
from pages import home_page
import conftest
import time

@pytest.mark.usefixtures("setup_teardown")
class TestAdicionarItemCarrinho:

    def teste_adicionar_item_carrinho(self):
        loginPage = login_page.LoginPage()
        homePage = home_page.HomePage()
        loginPage.fazer_login("standard_user", "secret_sauce")

        homePage.adcionar_item_carrinho()
        homePage.ir_para_carrinho()

        #time.sleep(10)



