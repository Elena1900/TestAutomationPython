from selenium.webdriver.common.by import By


class MainPageLocators():
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")


class BasketPageLocators():
    GO_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn-group")
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")    