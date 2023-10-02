from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://wiki.polkadot.network/docs/learn-index"

driver = webdriver.Firefox()
driver.get(url)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__docusaurus_skipToContent_fallback"]/div/aside/div/div/nav/ul/li[3]/ul/li[7]/ul/li[4]')))

# Capture the rendered HTML content after the element is present
page_source = driver.page_source

driver.close()

with open("output.html", "wb") as file:
    file.write(page_source.encode('utf-8'))
    print("HTML file saved as 'output.html'")
