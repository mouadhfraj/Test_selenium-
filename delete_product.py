import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Suppression d'un produit dans Magento")
@allure.description("Test pour supprimer un produit via l'interface d'administration Magento.")
def test_delete_product():
    # Configuration du WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Exécution en mode headless (facultatif pour CI/CD)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        with allure.step("Connexion à l'interface d'administration"):
            driver.get("http://mage2rock.magento.com/admin")  # Remplacez par votre URL Magento
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("rockadmin")
            driver.find_element(By.ID, "login").send_keys("Admin@123456")
            driver.find_element(By.XPATH, "//button[contains(@class, 'action-login') and span[text()='Sign in']]").click()

            # Vérification de la connexion
            assert "Dashboard" in driver.title, "Connexion échouée"
            allure.attach(driver.get_screenshot_as_png(), name="Dashboard", attachment_type=allure.attachment_type.PNG)

        with allure.step("Navigation vers la liste des produits"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Products']"))).click()

        with allure.step("Recherche du produit à supprimer"):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fulltext"))).clear()
            driver.find_element(By.ID, "fulltext").send_keys("Produit Test")  # Remplacez avec le nom/SKU du produit
            driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[1]/div[5]/button').click()

        with allure.step("Sélection du produit et suppression"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//label[@class="data-grid-checkbox-cell-inner"]/input[1]'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[1]/div/button'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[1]/div/div/ul/li[1]/span'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[span[text()="OK"]]'))
            ).click()

        with allure.step("Vérification que le produit a été supprimé"):
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-success')]"))
            )
            assert "record(s) have been deleted." in success_message.text, "Le produit n'a pas été supprimé avec succès"
            allure.attach(driver.get_screenshot_as_png(), name="Produit Supprimé", attachment_type=allure.attachment_type.PNG)

        print("Test réussi : Le produit a été supprimé avec succès.")

    finally:
        driver.quit()
