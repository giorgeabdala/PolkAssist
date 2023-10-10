from crawler_functions import PageFunctions, ScraperFunctions


def main():    
    """
    Scraping module LEARN
    """
    url_learn = "https://wiki.polkadot.network/docs/learn-index"
    xpath_hrefs_learn = '//*[@id="__docusaurus_skipToContent_fallback"]/div/aside/div/div'
    xpath_buttons = "//div[@class='menu__list-item-collapsible']//a[@class='menu__link menu__link--sublist']"
    
    try:
        driver = PageFunctions.get_driver()
        PageFunctions.open_page(driver, url_learn)
        PageFunctions.open_sidebar(driver, url_learn, xpath_buttons)
        
        hrefs_learn = ScraperFunctions.sidebar_href_list(driver, xpath_hrefs_learn)
        ScraperFunctions.write_list(hrefs_learn, "./test/crawler/urls/learn-index.txt")
        
        driver.close()
    except Exception as e:
        print(e)
        driver.close()

    """
    Scraping modules BUILD/MAINTAIN
    """
    url_list = ["https://wiki.polkadot.network/docs/build-index", 
                "https://wiki.polkadot.network/docs/maintain-index"]
    
    xpath_hrefs_build = '//*[@id="__docusaurus_skipToContent_fallback"]/div/aside/div/div'
    xpath_buttons = "//div[@class='menu__list-item-collapsible']//a[@class='menu__link menu__link--sublist menu__link--sublist-caret']"
    
    for url in url_list:
        short_url = url.replace('https://wiki.polkadot.network/docs/', "")
        try:
            driver = PageFunctions.get_driver()
            PageFunctions.open_page(driver, url)
            PageFunctions.open_sidebar(driver, url, xpath_buttons)
            
            hrefs_build = ScraperFunctions.sidebar_href_list(driver, xpath_hrefs_build)
            ScraperFunctions.write_list(hrefs_build, f"./test/crawler/urls/{short_url}.txt")
            
            driver.close()
        except Exception as e:
            print(e)
            driver.close()


if __name__ == "__main__":
    main()
