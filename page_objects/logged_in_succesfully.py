from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class LoggedInSuccesfullyPage(BasePage):

    _url = "https://app.jubelio.com/home"
    __tp_url = "https://app.jubelio.com/home/inventory"
    __header_locator = (By.TAG_NAME, "h1")
    __profile_button_locator = (By.ID, "user_menu")
    

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def teleport_url(self):
        super()._open_url(self.__tp_url)  

    @property
    def expected_url(self) -> str:
        return self._url 

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
    
    def is_profile_button_displayed(self) -> bool:
        return super()._is_displayed(self.__profile_button_locator)