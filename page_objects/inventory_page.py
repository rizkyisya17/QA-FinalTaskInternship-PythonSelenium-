from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class InventoryPage(BasePage):

    _url = "https://app.jubelio.com/home/inventory"
    __header_locator = (By.TAG_NAME, "h1")
    __profile_button_locator = (By.ID, "user_menu")
    __penyesuaian_persediaan_locator = (By.LINK_TEXT, "Penyesuaian Persediaan")
    __button_penyesuaian = (By.XPATH, "//button[@class='ladda-button btn btn-primary m-l-xs']")
    __button_pilih_barang = (By.XPATH, "//span[@class='text-muted']")
    __button_selected_barang = (By.XPATH, "//div[@class='selectivity-result-item'][@data-item-id='289']") # 0001-Naruto
    #__input_tambah_barang_locator = (By.XPATH, "(//div[@class='text-right'])[7]")
    #__input_tambah_barang_locator = (By.XPATH, "//div[@class='pika-single is-hidden is-bound']")
    __input_tambah_barang_locator = (By.XPATH, "(//div[@class='react-grid-Cell__value'])[2]")
    #__input_tambah_barang_locator2 = (By.XPATH, "//div[@class='rdg-editor-container']")
    __input_tambah_barang = (By.XPATH, "//input[@class=' editor-main']")
    #__button_simpan = (By.XPATH, "//button[@class='ladda-button btn btn-primary std-btn-width']//span[@class='ladda-label' and .//text()='Simpan']")
    __button_simpan = (By.XPATH, "(//button[@class='ladda-button btn btn-primary std-btn-width'])[2]")
    __alert_berhasil_simpan = (By.XPATH, "//*[@id='root']/div/div[1]/li")
    #__alert_berhasil_simpan = (By.TAG_NAME, "li")
    #__alert_berhasil_simpan = (By.XPATH, "(//div[@class='app-alert alert alert-success alert-dismissable']//text())[3]")[0]
    

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url 

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
    
    def is_profile_button_displayed(self) -> bool:
        return super()._is_displayed(self.__profile_button_locator)
    
    def is_penyesuaian_button_displayed(self) -> bool:
        return super()._is_displayed(self.__penyesuaian_persediaan_locator)
    
    def get_alert(self):
        return super()._get_text(self.__alert_berhasil_simpan,2)
    
    def atur_persediaan(self, jumlah):
        super()._click(self.__button_penyesuaian)
        super()._doubleclick(self.__button_pilih_barang)
        super()._click(self.__button_selected_barang)
        super()._click(self.__input_tambah_barang_locator)
        super()._doubleclick(self.__input_tambah_barang_locator)
        super()._type(self.__input_tambah_barang, jumlah)
        super()._click(self.__button_simpan)