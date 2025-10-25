import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    usuarioTxt = driver.find_element(By.ID,"user-name")
    claveTxt = driver.find_element(By.ID,"password")
    loginBtn = driver.find_element(By.ID,"login-button")

    usuarioTxt.send_keys("standard_user")
    claveTxt.send_keys("secret_sace")
    loginBtn.click()

    driver.quit()