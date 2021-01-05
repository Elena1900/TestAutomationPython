def test_busket_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(link)
    assert browser.find_element_by_xpath('//form[@id="add_to_basket_form"]/button[@type = "submit"]')