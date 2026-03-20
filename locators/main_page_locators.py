from selenium.webdriver.common.by import By

class MainPageLocators:

    # локаторы для кнопок заказа
    order_button_top = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    order_button_bottom = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')

    # Блок FAQ
    faq_area = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")
    