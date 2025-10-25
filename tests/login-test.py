import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@pytest.fixture(scope="function")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) 
    yield driver
    
    driver.quit()

def test_login(driver_setup):
    driver = driver_setup
    base_page = BasePage(driver)
    base_page.go_to_url("https://www.saucedemo.com/")

    # Localizar elementos
    usuarioTxt = base_page._find_element(By.ID,"user-name")
    claveTxt = base_page._find_element(By.ID,"password")
    loginBtn = base_page._find_element(By.ID,"login-button")

    usuarioTxt.send_keys("standard_user")
    claveTxt.send_keys("secret_sauce")
    loginBtn.click()

    titulo_productos = base_page._get_element_text(By.XPATH, "//span[text()='Products']")
        
    assert titulo_productos == "Products", "El título de la página no es 'Products'. Login fallido."
    print("Login exitoso - La validación de título correcta")