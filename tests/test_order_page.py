import allure
import pytest

from locators.main_page_locators import MainPageLocators
from data import URLs, OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Позитивный сценарий оформления заказа самоката")
    @allure.description("Проверка успешного оформления заказа через разные кнопки")   
    @pytest.mark.parametrize("button, order_data", [
            (MainPageLocators.order_button_top, OrderData.USER_1),
            (MainPageLocators.order_button_bottom, OrderData.USER_2),
        ])
    def test_order_creation_from_both_buttons(self, driver, button, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_accept_cookies()
        main_page.scroll_to_element(button)
        main_page.click_on_element(button)
        order_page.wait_for_page_load(URLs.order_page)
        order_page.complete_order(order_data)
        is_confirmed = order_page.check_order_completion()

        assert is_confirmed
