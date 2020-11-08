from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Перейти на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    # Решаем капчу
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Отправляем ответ
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
