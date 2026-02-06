import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class OrderPage(BasePage):

    @allure.step("Заполнить поле 'Имя'")
    def fill_name_field(self, name):
        self.send_keys_to_field(OrderPageLocators.name_input, name)
    
    @allure.step("Заполнить поле 'Фамилия'")
    def fill_surname_field(self, surname):
        self.send_keys_to_field(OrderPageLocators.surname_input, surname)

    @allure.step("Заполнить поле 'Адрес'")
    def fill_address_field(self, address):
        self.send_keys_to_field(OrderPageLocators.address_input, address)

    @allure.step("Выбрать станцию метро: '{station}'")
    def select_metro_station(self, station):
        self.click_on_element(OrderPageLocators.metro_input)
        station_locator = (By.XPATH, f"//div[text()='{station}']")
        self.click_on_element(station_locator)

    @allure.step("Заполнить поле 'Телефон'")
    def fill_phone_field(self, phone_number):
        self.send_keys_to_field(OrderPageLocators.telephone_input, phone_number)
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step("Выбрать дату")       
    def select_date(self):
        self.click_on_element(OrderPageLocators.delivery_input)
        self.find_visible_element(OrderPageLocators.date_picker)
        self.click_on_element(OrderPageLocators.delivery_date_select)
    
    @allure.step("Выбрать срок аренды")
    def select_rent_duration(self, period):
        self.click_on_element(OrderPageLocators.rent_input)
        self.find_visible_element(OrderPageLocators.rent_dropdown_menu)
        option_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")
        self.click_on_element(option_locator)
    
    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color):
        color_locators = {
            "black": OrderPageLocators.scooter_black,
            "grey": OrderPageLocators.scooter_grey
        }
        self.click_on_element(color_locators[color])

    @allure.step("Написать комментарий для курьера")
    def add_comment(self, comment):
        self.send_keys_to_field(OrderPageLocators.comment_for_courier, comment)
    
    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.order_button)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.yes_button)
    
    @allure.step("Проверка успешного оформления заказа")
    def check_order_completion(self):
        return self.find_visible_element(OrderPageLocators.order_confirmed).is_displayed()
    
    @allure.step("Оформление заказа") 
    def complete_order(self, order_data):
        self.fill_name_field(order_data.get('first_name'))
        self.fill_surname_field(order_data.get('last_name'))
        self.fill_address_field(order_data.get('address'))
        self.select_metro_station(order_data.get('metro_station'))
        self.fill_phone_field(order_data.get('phone'))
        self.click_next_button()

        self.select_date()
        self.select_rent_duration(order_data.get('rental_period'))
        self.select_scooter_color(order_data.get('color'))
        self.add_comment(order_data.get('comment'))
        self.click_order_button()
        self.confirm_order()
