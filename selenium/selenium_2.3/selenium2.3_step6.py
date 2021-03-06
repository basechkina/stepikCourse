import math

from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    startLink = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector("#input_value").text
    y = calc(x_element)

    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)

    browser.quit()

# не забываем оставить пустую строку в конце файла