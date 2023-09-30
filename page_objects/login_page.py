from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver




class LoginPage(BasePage):

    __url = "https://app.jubelio.com/login"
    __email_field = (By.XPATH, "//input[@name='email']")
    __password_field = (By.XPATH, "//input[@name='password']")
    __submit_button = (By.XPATH, "//button[@type='submit']")
    __error_message = (By.XPATH, "//span[@class='help-block']")
    __alerts = (By.XPATH, "//div[@class='app-alert alert alert-danger alert-dismissable']")
    #__alerts_message = (By.TAG_NAME, "li")
    #__alerts_message = (By.XPATH, "//*[@id='root']/div/div[1]/li")
    __alerts_message = (By.XPATH, "//div[@class='app-alert alert alert-danger alert-dismissable']//li")
    __alerts_message2_email = (By.XPATH, "(//div[@class='app-alert alert alert-danger alert-dismissable']//following::li[1])[1]")
    __alerts_message2_password = (By.XPATH, "(//div[@class='app-alert alert alert-danger alert-dismissable']//following::li[2])[1]")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, email: str, password: str):
        super()._type(self.__email_field, email)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)
        

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, 1)
    
    def get_alert(self):
        return super()._get_text(self.__alerts_message,2)
    
    def get_alert_baris1(self):
        return super()._get_text(self.__alerts_message2_email,2)
    
    def get_alert_baris2(self):
        return super()._get_text(self.__alerts_message2_password,2)
        
        
        