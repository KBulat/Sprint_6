import allure

from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
   
    @allure.step("Принять cookies")
    def click_accept_cookies(self):
        self.click_on_element(BasePageLocators.cookie_accept_button)

    @allure.step("Кликнуть по кнопке 'Заказать' вверху страницы")
    def click_upper_order_button(self):
        self.click_on_element(MainPageLocators.order_button_top)

    @allure.step("Кликнуть по кнопке 'Заказать' внизу страницы")
    def click_lower_order_button(self):
        self.scroll_to_element(MainPageLocators.order_button_bottom)
        self.click_on_element(MainPageLocators.order_button_bottom)

    @allure.step("Кликнуть на вопрос номер {question_number}")   
    def click_faq_question(self, question_number):
        index = question_number - 1
        element = self.driver.find_element(By.ID, f"accordion__heading-{index}")
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст ответа в FAQ")
    def get_faq_answer_text(self, question_number):
        index = question_number - 1
        return self.find_visible_element((By.ID, f"accordion__panel-{index}")).text
