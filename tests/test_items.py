def test_busket_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(link)
    button = browser.find_elements_by_css_selector("#add_to_basket_form button[type='submit']")

    assert len(button) > 0, "Корзина не найдена!"