import allure
import pytest

from locators.main_page_locators import MainPageLocators
from data import URLs, AccordionData
from pages.main_page import MainPage


class TestMainPage:
    
    @allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном'")
    @allure.description("При клике на вопрос должен открываться соответствующий текст ответа")
    @pytest.mark.parametrize("question_number, expected_answer", AccordionData.Data)
    def test_click_question_shows_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.click_accept_cookies()
        main_page.scroll_to_element(MainPageLocators.faq_area)
        main_page.click_faq_question(question_number)
        actual_answer = main_page.get_faq_answer_text(question_number)

        assert actual_answer == expected_answer

    @allure.title("Проверка перехода на главную страницу по клику на логотип 'Самокат'")
    def test_click_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookies()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == URLs.main_page

    @allure.title("Проверка перехода на главную страницу по клику на логотип 'Яндекс'")
    def test_click_yandex_logo_opens_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_next_tab()

        assert main_page.is_dzen_opened()
