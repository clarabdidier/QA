from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/")
print("Acessou o site DemoQA.")

time.sleep(2)

forms_menu = driver.find_element(By.XPATH, "//h5[text()='Forms']")
forms_menu.click()
print("Navegou para a seção de Formulários.")

time.sleep(2)

practice_form = driver.find_element(By.XPATH, "//span[text()='Practice Form']")
practice_form.click()
print("Clicou em 'Practice Form'.")

time.sleep(2)

first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("John")
print("Preencheu o campo 'First Name'.")

last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Doe")
print("Preencheu o campo 'Last Name'.")

email = driver.find_element(By.ID, "userEmail")
email.send_keys("john.doe@example.com")
print("Preencheu o campo 'Email'.")

gender = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
gender.click()
print("Selecionou o gênero.")

mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys("1234567890")
print("Preencheu o campo 'Mobile'.")

driver.execute_script("""
    var iframe = document.getElementById('google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0');
    if (iframe) {
        iframe.remove();
    }
""")
print("Iframe de anúncio removido.")

try:
    hobbies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']"))
    )
    hobbies.click()
    print("Clicou no campo de hobbies.")
except Exception as e:
    print(f"Erro ao tentar clicar em hobbies: {e}")

upload_element = driver.find_element(By.ID, "uploadPicture")
upload_element.send_keys(os.path.abspath("arquivo.txt"))
print("Fez upload do arquivo .txt.")

address = driver.find_element(By.ID, "currentAddress")
address.send_keys("123 Main St, Springfield")
print("Preencheu o campo 'Address'.")

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()
print("Submeteu o formulário.")

time.sleep(2)

close_button = driver.find_element(By.ID, "closeLargeModal")
close_button.click()
print("Fechou o popup.")

time.sleep(2)
driver.quit()
print("Navegador fechado.")
