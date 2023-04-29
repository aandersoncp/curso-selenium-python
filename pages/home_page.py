from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import conftest
from tests import test_adicionar_item_carrinho


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//span[@class='title']")
        self.item = (By.XPATH, "//button[contains(@data-test,'add-to-cart-sauce-labs-backpack')]")
        self.cart = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.item_carrinho = (By.XPATH, "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_e_exibido(self.title_page)

    def adcionar_item_carrinho(self):
        self.encontrar_elemento(self.item).click()

    def ir_para_carrinho(self):
        self.encontrar_elemento(self.cart).click()

    def verificar_item_no_carrinho(self):
        self.verificar_se_elemento_e_exibido(self.item_carrinho)
