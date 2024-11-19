from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
driver.maximize_window()

try:
     # Étape 1 : Connexion au panneau d'administration
    driver.get("http://mage2rock.magento.com/admin")  # Remplacez par votre URL Magento
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
    driver.find_element(By.ID, "username").send_keys("rockadmin")  # Remplacez par vos identifiants
    driver.find_element(By.ID, "login").send_keys("Admin@123456")
    driver.find_element(By.XPATH, "//button[contains(@class, 'action-login') and span[text()='Sign in']]").click()

    # Assertion : Vérifier la connexion réussie
    assert "Dashboard" in driver.title, "Connexion échouée"
    
    # Step 2: Navigate to the product list
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Products']"))).click()

    # Step 3: Search for the product to delete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fulltext"))).clear()
    driver.find_element(By.ID, "fulltext").send_keys("Produit Test")# Replace with product name or SKU
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[1]/div[5]/button').click()

    # Step 4: Select the product and click delete
   
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//label[@class="data-grid-checkbox-cell-inner"]/input[1]'))
).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ' //*[@id="container"]/div/div[2]/div[2]/div[1]/div/button'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[1]/div/div/ul/li[1]/span'))).click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[span[text()="OK"]]'))
).click()


    
    # Step 6: Verify the product was deleted
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-success')]"))
    )
    assert " record(s) have been deleted." in success_message.text, "The product was not deleted successfully."

    print("Test Passed: The product was deleted successfully.")

finally:
    # Close the browser
    driver.quit()