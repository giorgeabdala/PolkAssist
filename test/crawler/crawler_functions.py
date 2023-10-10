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
    def open_sidebar(driver, url, xpath_buttons):
        driver.get(url)
        
        while True:
            buttons = driver.find_elements(By.XPATH, xpath_buttons)

            for button in buttons:
                button.click()
                time.sleep(1)

            new_buttons = driver.find_elements(By.XPATH, xpath_buttons)

            if len(new_buttons) == len(buttons):
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
