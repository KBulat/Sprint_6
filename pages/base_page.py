import allure

from data import URLs
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем страницу {url}")
    def get_url(self, url):
        self.driver.get(url)
    
    @allure.step("Узнать адрес текущей страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Найти элемент {locator}")
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Дождаться кликабельности элемента {locator}")
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))
             
    @allure.step("Кликнуть по элементу")
    def click_on_element(self, locator):
        self.find_visible_element(locator).click()
    
    @allure.step("Ввод данных в поле")
    def send_keys_to_field(self, locator, text):
        self.find_visible_element(locator).send_keys(text)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_visible_element(locator).text
    
    @allure.step("Проскроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Кликнуть на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.find_visible_element(BasePageLocators.yandex_logo).click()

    @allure.step('Кликнуть на логотип "Самокат"')
    def click_scooter_logo(self):
        self.find_visible_element(BasePageLocators.scooter_logo).click()
    
    @allure.step("Перейти на следующую вкладку")
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Проверить, что открыт сайт Дзен")
    def is_dzen_opened(self):
        try:
            self.wait.until(EC.url_contains(URLs.dzen_page))
            return True
        except Exception:
            return False
