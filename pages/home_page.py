from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import conftest


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//span[@class='title']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_e_exibido(self.title_page)