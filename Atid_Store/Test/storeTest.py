from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from Atid_Store.BaseTest.storeLocation import *
import pytest

def test_store_buy_product():
    driver = webdriver.Chrome()
    driver.get(storeLink1)
    driver.maximize_window()
    driver.find_element(By.XPATH,storeLink2).click()
    sleep(2)
    driver.find_element(By.XPATH,storeLink3).click()
    sleep(2)
    driver.find_element(By.XPATH, storeLink4).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, storeLink5).text
    assert product_name == "Anchor Bracelet"
    driver.find_element(By.XPATH, storeLink6).click()
    sleep(10)
    coupon_field = driver.find_element(By.XPATH,storeLink7)
    sleep(12)
    coupon_field.click()
    coupon_field.send_keys("123fent")
    sleep(12)
    driver.find_element(By.XPATH, storeLink8).click()
    sleep(3)