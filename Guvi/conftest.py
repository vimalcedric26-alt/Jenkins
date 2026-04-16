import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def setup():
    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-gpu")

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.get("https://www.guvi.in")

    wait = WebDriverWait(driver, 10)

    yield driver, wait

    driver.quit()