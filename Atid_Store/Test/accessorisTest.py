from time import sleep

from Atid_Store.BaseTest.accessorisLocation import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def accessorise_buy_product():
    driver = webdriver.Chrome()
    driver.get(accessoriseLink1)
    driver.maximize_window()
    driver.find_element(By.XPATH, accessoriseLink2).click()
    sleep(3)
    driver.find_element(By.XPATH, accessoriseLink3).click()
    sleep(3)
    driver.find_element(By.XPATH, accessoriseLink4).click()
    sleep(3)
    product_name = driver.find_element(By.XPATH, accessoriseLink5).text
    assert product_name == 'Bright Red Bag'
    driver.find_element(By.XPATH, accessoriseLink6).click()
    sleep(10)
    coupon_field = driver.find_element(By.XPATH, accessoriseLink7)
    sleep(12)
    coupon_field.click()
    coupon_field.send_keys("123fent")
    sleep(12)
    driver.find_element(By.XPATH, accessoriseLink8).click()
    sleep(3)
