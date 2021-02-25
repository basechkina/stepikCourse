from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element_by_css_selector("#treasure")
    x_value = img.get_attribute("valuex")
    y = calc(x_value)

    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)
    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    robot_checkbox.click()
    robots_rule = browser.find_element_by_css_selector("#robotsRule")
    robots_rule.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)

    browser.quit()

# не забываем оставить пустую строку в конце файла