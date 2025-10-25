import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # Localizar elementos
    usuarioTxt = driver.find_element(By.ID,"user-name")
    claveTxt = driver.find_element(By.ID,"password")
    loginBtn = driver.find_element(By.ID,"login-button")

    usuarioTxt.send_keys("standard_user")
    claveTxt.send_keys("secret_sauce")
    loginBtn.click()

    titulo_productos = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Products']"))
        )
        
    assert titulo_productos.text == "Products", "El título de la página no es 'Products'. Login fallido."
    print("Login exitoso - La validación de título correcta")

    driver.quit()