# Open browser
# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)

# Go to webpage
driver.get("https://app.jubelio.com/login")
time.sleep(2)

# Type username student into Username field
email_locator = driver.find_element(By.XPATH, "//input[@name='email']")
email_locator.send_keys("qa.rakamin.jubelio@gmail.com")

# Type password Password123 into Password field
password_locator = driver.find_element(By.XPATH, "//input[@name='password']")
#password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Jubelio123!")

# Puch Submit button
#submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button_locator.click()
time.sleep(3)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
print(actual_url)
assert actual_url == "https://app.jubelio.com/home"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Dashboard"

# Verify button Log out is displayed on the new page
log_out_button_locator = driver.find_element(By.ID, "user_menu")
assert log_out_button_locator.is_displayed()
