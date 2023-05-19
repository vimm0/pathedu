from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Initialize the webdriver for Firefox
driver = webdriver.Firefox()

# Open the WhatsApp Web interface
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code and log in
input("Press Enter after scanning the QR code and logging in…")

# Open the file containing the phone numbers
line = '+9779861359718'
# Strip any whitespace from the line
line = line.strip()
# Navigate to the WhatsApp Web search page
driver.get("https://web.whatsapp.com/send?phone=" + line)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_3q4NP']")))
# Check if the phone number is registered on WhatsApp
if driver.find_elements_by_xpath("//div[@class='_3q4NP']"):
    print(f"{line} - Registered on WhatsApp")
else:
    print(f"{line} - Not registered on WhatsApp")
# Click the back button to close the chat window
back_button = driver.find_element_by_xpath("//span[@data-icon='back']")
back_button.click()
time.sleep(1) # wait for the back button to take effect

# Close the webdriver
driver.quit()