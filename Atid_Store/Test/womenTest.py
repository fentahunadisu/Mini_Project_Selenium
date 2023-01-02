from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from Atid_Store.BaseTest.womenLocation import *
import pytest

def test_women_buy_product():
    driver = webdriver.Chrome()
    driver.get(womenLink1)
    driver.maximize_window()
    driver.find_element(By.XPATH,womenLink2).click()
    sleep(3)
    driver.find_element(By.XPATH, womenLink3).click()
    sleep(3)
    driver.find_element(By.XPATH, womenLink4).click()
    sleep(3)
    product_name = driver.find_element(By.XPATH, womenLink5).text
    assert product_name == 'Basic Gray Jeans'
    driver.find_element(By.XPATH, womenLink6).click()
    sleep(10)
    coupon_field = driver.find_element(By.XPATH,womenLink7)
    sleep(12)
    coupon_field.click()
    coupon_field.send_keys("123fent")
    sleep(12)
    driver.find_element(By.XPATH, womenLink8).click()
    sleep(3)
