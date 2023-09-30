import pytest
from page_objects.login_page import LoginPage
import time



class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("email, password, expected_error_message", 
                             [("ngawur","testes12","Format Email tidak valid."), 
                              ("ngaco@gmail.com","tes","Password harus di antara 6 dan 30."),
                              ("siapbelajar@gmail.com", "helpbutuhkerja","Password atau email anda salah.")])
    def test_negative_login1(self, driver, email, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(email, password)
        #assert login_page.get_error_message() == expected_error_message, "Error message is not displayed, but it should"
        assert login_page.get_alert() == expected_error_message, "Alert message is not displayed, but it should"
        time.sleep(1)
        

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("email, password, expected_error_message", 
                             [("nganggur","job",["Format Email tidak valid.", "Password harus di antara 6 dan 30."])])
    def test_negative_login2(self, driver, email, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(email, password)
        #assert login_page.get_error_message() == expected_error_message, "Error message is not displayed, but it should"
        assert login_page.get_alert_baris1() == expected_error_message[0], "Alert message is not displayed, but it should"
        assert login_page.get_alert_baris2() == expected_error_message[1], "Alert message is not displayed, but it should"
        time.sleep(1)
        
        
