import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def setup():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    options = webdriver.FirefoxOptions()

    options.add_argument("--headless")



    driver = webdriver.Firefox()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)


    yield driver, wait

    driver.quit()