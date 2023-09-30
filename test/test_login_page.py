# Open browser
# selenium 4

import pytest
import time
from page_objects.login_page import LoginPage
from page_objects.logged_in_succesfully import LoggedInSuccesfullyPage



class TestPositiveScenarious:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("qa.rakamin.jubelio@gmail.com", "Jubelio123!")
        logged_in_page = LoggedInSuccesfullyPage(driver)
        time.sleep(3)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Dashboard", "Header is not expected"
        assert logged_in_page.is_profile_button_displayed(), "Profile should be displayed"
