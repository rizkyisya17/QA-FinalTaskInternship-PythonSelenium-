# Open browser
# selenium 4

import pytest
import time
from page_objects.login_page import LoginPage
from page_objects.logged_in_succesfully import LoggedInSuccesfullyPage
from page_objects.inventory_page import InventoryPage



class TestPositiveScenarious:

    @pytest.mark.persediaanbarang
    @pytest.mark.positive
    def test_positive_barang(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("qa.rakamin.jubelio@gmail.com", "Jubelio123!")
        logged_in_page = LoggedInSuccesfullyPage(driver)
        time.sleep(5)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Dashboard", "Header is not expected"
        assert logged_in_page.is_profile_button_displayed(), "Profile should be displayed"
        logged_in_page.teleport_url()
        inventory_page = InventoryPage(driver)
        assert inventory_page.expected_url == inventory_page.current_url, "Actual URL is not the same as expected"
        assert inventory_page.header == "Persediaan", "Header is not expected"
        inventory_page.fullscreen()
        inventory_page.atur_persediaan(5)
        print(inventory_page.get_alert())
        assert inventory_page.get_alert() == "Data berhasil disimpan.", "Text is not expected"
        time.sleep(3)



