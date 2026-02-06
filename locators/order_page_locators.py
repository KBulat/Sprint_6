from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Форма «Для кого самокат»
    name_input = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    surname_input = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    address_input = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    metro_input = (By.CLASS_NAME, "select-search__input")
    telephone_input = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    
    # Кнопка «Далее»
    next_button = (By.XPATH, ".//button[text()='Далее']")

    # Форма «Про аренду»
    delivery_input = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    date_picker = (By.CLASS_NAME, "react-datepicker")
    delivery_date_select = (By.XPATH, "//div[@aria-label='Choose среда, 25-е февраля 2026 г.']")
    rent_input = (By.XPATH, "//div[text()='* Срок аренды']")
    rent_dropdown_menu = (By.CLASS_NAME, "Dropdown-menu")
    scooter_black = (By.ID, "black")
    scooter_grey = (By.ID, "grey")
    comment_for_courier = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Хотите оформить заказ?
    yes_button = (By.XPATH, './/button[text()="Да"]')
    no_button = (By.XPATH, './/button[text()="Нет"]')

    # Заказ оформлен
    order_confirmed = (By.XPATH, './/div[text()="Заказ оформлен"]')
    order_status_button = (By.XPATH, './/div[text()="Посмотреть статус"]')
