import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-geolocation")

    driver = webdriver.Firefox()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)


    yield driver, wait

    driver.quit()