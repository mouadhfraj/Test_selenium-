from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialiser le WebDriver
driver = webdriver.Chrome()  # Utilisez le driver approprié pour votre navigateur
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

    # Étape 2 : Aller dans Produits
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Products']"))).click()

    # Assertion : Vérifier que la page des produits est affichée
    page_heading = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Products']")))
    assert page_heading.is_displayed(), "La page Produits n'est pas affichée"

    # Étape 3 : Ajouter un produit
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add Product']"))).click()

    # Remplir les informations du produit
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "product[name]"))  # Replace with actual name attribute
).send_keys("Produit Test")

# Select the second element by name and send keys
    driver.find_element(By.NAME, "product[sku]").send_keys("TEST123")  # Replace with actual name attribute

# Select the third element by name and send keys
    driver.find_element(By.NAME, "product[price]").send_keys("99.99")  # Replace with actual name attribute

# Select the fourth element by name and send keys
    driver.find_element(By.NAME, "product[quantity_and_stock_status][qty]").send_keys("10")  
    # Sauvegarder le produit
    driver.find_element(By.XPATH, "//button[@title='Save']").click()

    # Étape 4 : Vérifier que le produit a été ajouté avec succès
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-success')]"))
    )
    assert "You saved the product." in success_message.text, "Le produit n'a pas été enregistré avec succès"

    print("Test réussi : le produit a été ajouté correctement.")

finally:
    # Fermer le navigateur
    driver.quit()