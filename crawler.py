import time
import re
import random  
import prettytable as pt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import TIMEOUT, url
from extractor import get_next_page_url, product_extractor

def get_soup_from_url(url):
    """Return a BeautifulSoup object from the given URL."""

    options = Options()
    # avoid bot detection  - https://stackoverflow.com/questions/49565042/way-to-change-google-chrome-user-agent-in-selenium/49565254#49565254
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17")
    options.add_argument("--start-maximized")  # Maximize the browser window
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("prefs", 
                                    {"profile.default_content_setting_values.notifications": 2 
                                    }) 

    driver = webdriver.Chrome(
        # WEB_DRIVER_LOCATION, 
        options=options)
    driver.get(url)

    # Timeout needed for Web page to render (read more about it)
    time.sleep(TIMEOUT)
    html = driver.page_source

    # Get the source of the page and create a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_soup_from_driver(driver):
    """Return a BeautifulSoup object from the given driver."""
    html = driver.page_source

    # Get the source of the page and create a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_urlList():
    user_agent_list = ['Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5;',
    'Mozilla/4.0 (compatible; Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729); Windows NT 5.1; Trident/4.0)',
    'Mozilla/4.0 (compatible; Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727); Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 2.0.50727; .NET CLR 1.1.4322; InfoPath.2)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; InfoPath.2; .NET CLR 2.0.50727; Alexa Toolbar)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; InfoPath.2)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17']

    options = Options()
    # avoid bot detection  - https://stackoverflow.com/questions/49565042/way-to-change-google-chrome-user-agent-in-selenium/49565254#49565254
    options.add_argument("--user-agent={}".format(random.choice(user_agent_list)))
    options.add_argument("--start-maximized")  # Maximize the browser window
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--cookie=lwa-context=9872941c399f7d905fe29b64a28c533d; session-id=136-4085273-4202024; ubid-main=132-1087777-9092235; sp-cdn="L5Z9:CA"; x-main="yoLGt6tY2Av179LTUtE1B5i0mc3NoEkYCuq9NUs?IrOpfx447fUI@3NOG@j8yx73"; at-main=Atza|IwEBIDJVhPoDUtx-YjlDA48o5m2WQVmwarVBK9N1_sxeXoMZ_PrzJSm7Wh3VXmVUNir7xDSSNijJbg6BIrm0NobFfF1Kd898nZCHaWRhZFAI59IFu5hGxWGXSi-DyXe9MgymkiwgymPEErPtRokjY_U9vEUKIqhF-6ihd4eCZ6ocYWanMOxit6gFb4kv9_07p80dbW7E2UupHcmSSXowXgqtG70yo7g_NBqaeyT4NQOHi31Ogw; sess-at-main="gAG1urrtNUraAE0iBhe6StwiU2cAxc1vN+lUlrcfbjw="; sst-main=Sst1|PQGvR6pn3EMISk7_KeNZhnCMCfikkXSlYGM2tVdEIgqgZ5rV0wyOOZButl2JEXdREqui-evjq4BIJnHWIvYwCNzwBavOFnUJrNNmK4-hSjOKxED4p4Ky_Ca5QtRF4sSzd7NlniB6-JPwdPQJ2xeqtaX_KnYQJbZTQ5A7XjN89PQTyg3qlqjSHko7xYjuLnBd5qKpV6AmlRyrMMq8B2-AhpDT5rckNRMW5MlTLRBoWJr2utSDcw-ynNh8uV46_jaYnP9NyBvVoO4uyXvnHt5RtDINsywpiG_BC3Y2ohTHi2PbgEQ; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; session-token=Bq3AZZtlXHZ8a8V3Pqtn4l0ObZLszxPa1hhMFWsUGuJizpvF+cjTIjJijvDfBEPIe/gqkzTNTjDQ688gfBQ4fi21qcW/L5U9DZogHIOvkJCafJLBay/CRdaGORbhDuFam9RPK9t+gFRpmslV7xpJF9AsX9DR/ElNrt4SjqccFRgbeJj/tIwla3FsCLJbscdi8Xw9fVM0VoQhI2zOoqL/snvk9rEhy9JEdDDS5pC8TaQaBIaiVv3mecHeDVoUM1HA56iu/44GwR7j1fLX22uE8x2HJHyK2tFNF9I2w6SZmfX6ifw918Ky7ekuMjel0x5PYdvxAtSlZAmRxBu5sThp0xm9CaWlEzLygqm7OFD3c7JSU7lskfZYxg==')
    options.add_argument("--accept-encoding=gzip, deflate, br")  
    options.add_argument("--accept-language=en-US,en;q=0.9")
    options.add_argument("--cache-control=no-cache")
    options.add_argument("--content-type=text/plain;charset=UTF-8")
    options.add_experimental_option("prefs", 
                                    {"profile.default_content_setting_values.notifications": 2 
                                    }) 

    driver = webdriver.Chrome(
        # WEB_DRIVER_LOCATION, 
        options=options)

    # get soup from driver
    driver.get(url)
    soup = get_soup_from_driver(driver)
    next_page_link = get_next_page_url(soup)

    urlList = []
    urlList.append(url)

    # get all the urls
    try: 
        while next_page_link: 
            print(next_page_link)
            urlList.append(next_page_link)

            # Timeout needed for Web page to render
            time.sleep(random.randrange(2,TIMEOUT))

            soup = get_soup_from_url(next_page_link)
            next_page_link = get_next_page_url(soup)
        
    except Exception:
        print("No more pages")
    finally:
        return urlList


def crawl_start(urlList):
    rows = []
    for e in urlList:
        time.sleep(random.randrange(2,5))
        soup = get_soup_from_url(e)
        ProductListElement = soup.find_all('div', {'cel_widget_id': re.compile('MAIN-SEARCH_RESULTS-\d+'),'class': 'template=SEARCH_RESULTS'})
        for item in ProductListElement:
        # get the product information
            title, url, price, solder, review, review_number, image_url, crawl_time = product_extractor(item)
            rows.append([title, url, price, solder, review, review_number, image_url, crawl_time])
    return rows


if __name__ == '__main__':
    # single page test code
    tb = pt.PrettyTable() 
    tb.field_names = ["Title", "URL", "Price", "Solder", "Review", "Review Number", "Image URL", "Crawl Time"] 
    soup = get_soup_from_url(url)
    next_url = get_next_page_url(soup)
    print(next_url)
    ProductListElement = soup.find_all('div', {'cel_widget_id': re.compile('MAIN-SEARCH_RESULTS-\d+'),'class': 'template=SEARCH_RESULTS'})
    for item in ProductListElement:
    # get the product information
        title, url, price, solder, review, review_number, image_url, crawl_time = product_extractor(item)
        tb.add_row([title, url, price, solder, review, review_number, image_url, crawl_time]) 
    # print(title, url, price, solder, review, review_number, image_url)
    print(tb)
