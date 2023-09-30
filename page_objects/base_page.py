from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)
    
    def _action(self, driver: WebDriver, action: ActionChains):
        self._actionchain = action 

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _doubleclick(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self.actionChains = ActionChains(self._driver)
        self.actionChains.double_click(self._find(locator)).perform()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    def fullscreen(self):
        return self._driver.fullscreen_window()
    
    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        
    def _open_url(self, url:str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text
    
    def _get_elements(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator)
    

    