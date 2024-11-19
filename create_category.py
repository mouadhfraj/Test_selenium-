from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # Update with your path
driver.maximize_window()

  # Étape 1 : Connexion au panneau d'administration
driver.get("http://mage2rock.magento.com/admin")  # Remplacez par votre URL Magento
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
driver.find_element(By.ID, "username").send_keys("rockadmin")  # Remplacez par vos identifiants
driver.find_element(By.ID, "login").send_keys("Admin@123456")
driver.find_element(By.XPATH, "//button[contains(@class, 'action-login') and span[text()='Sign in']]").click()

    # Assertion : Vérifier la connexion réussie
assert "Dashboard" in driver.title, "Connexion échouée"

# Wait for the Admin Dashboard to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']")))

# Navigate to Categories
driver.get("http://your-magento-site/admin/catalog/category")  # Update with the Categories URL

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Add Subcategory']")))

# Click on the "Add Subcategory" button
add_category_button = driver.find_element(By.XPATH, "//button[@title='Add Subcategory']")
add_category_button.click()

# Wait for the category creation page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "category_name")))  # Ensure the category name field is loaded

# Fill out the category details
category_name = driver.find_element(By.ID, "category_name")  # Category Name field
category_name.send_keys("New Category Name")  # Replace with the category name you want to create

category_url_key = driver.find_element(By.ID, "category_url_key")  # URL Key field
category_url_key.send_keys("new-category")  # Replace with the URL key

# Optional: Set the category to be visible in the store
visible_in_store = driver.find_element(By.XPATH, "//input[@value='1'][@name='category[is_active]']")
visible_in_store.click()  # Ensure the category is active

# Save the category
save_button = driver.find_element(By.XPATH, "//button[@title='Save Category']")
save_button.click()

# Wait for the category to be saved
time.sleep(3)

# Verify the success message (optional)
success_message = driver.find_element(By.XPATH, "//div[@class='message-success success message']")
assert "You saved the category." in success_message.text

# Close the browser
driver.quit()
