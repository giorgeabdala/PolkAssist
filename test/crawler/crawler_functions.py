import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class PageFunctions:
    @staticmethod
    def get_driver():
        driver = webdriver.Firefox()
        return driver

    @staticmethod
    def open_page(driver, url_main):
        driver.get(url_main)
        driver.maximize_window()
        driver.implicitly_wait(10)

    @staticmethod
    def open_sidebar_learn(driver, url):
        learn_buttons = "//div[@class='menu__list-item-collapsible']//a[@class='menu__link menu__link--sublist']"

        driver.get(url)
        
        while True:
            buttons = driver.find_elements(By.XPATH, learn_buttons)

            for button in buttons:
                button.click()
                time.sleep(1)

            new_buttons = driver.find_elements(By.XPATH, learn_buttons)

            if len(new_buttons) == len(buttons):
                break
        
        print("### SIDEBAR OPENED. ###\n")

    @staticmethod
    def open_sidebar_build(driver, url):
        build_buttons = "//div[@class='menu__list-item-collapsible']//a[@class='menu__link menu__link--sublist menu__link--sublist-caret']"

        driver.get(url)
        
        while True:
            buttons2 = driver.find_elements(By.XPATH, build_buttons)

            for button2 in buttons2:
                button2.click()
                time.sleep(1)

            new_buttons2 = driver.find_elements(By.XPATH, build_buttons)

            if len(new_buttons2) > len(buttons2):
                break
        
        print("### SIDEBAR OPENED. ###\n")


class ScraperFunctions:
    @staticmethod
    def sidebar_href_list(driver, xpath):
        sidebar = driver.find_element(By.XPATH, xpath)
        links = sidebar.find_elements(By.TAG_NAME, 'a')
        hrefs = [link.get_attribute('href') for link in links]
        hrefs = set(hrefs)
        print(len(hrefs), "LINKS COLLECTED.")
        return hrefs

    @staticmethod
    def write_list(hrefs, path):
        with open(path, 'w') as file:
            for item in hrefs:
                file.write(str(item) + '\n')
            print("DATA WRITTEN SUCCESSFULLY.")
