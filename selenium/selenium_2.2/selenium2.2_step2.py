from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = int(browser.find_element_by_css_selector("#num1").text)
    y_value = int(browser.find_element_by_css_selector("#num2").text)
    res = str(x_value + y_value)

    Select(browser.find_element_by_tag_name("select")).select_by_value(res)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)

    browser.quit()

# пустая строка
