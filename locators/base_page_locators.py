from selenium.webdriver.common.by import By

class BasePageLocators:

    # локаторы логотипов
    yandex_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    scooter_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    # кнопка "да все привыкли" для принятия cookie-файлов
    cookie_accept_button = (By.ID, "rcc-confirm-button")
    