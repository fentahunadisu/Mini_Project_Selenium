from time import sleep

from Atid_Store.BaseTest.menLocation import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_men_buy_product():
    driver = webdriver.Chrome()
    driver.get(men_link1)
    driver.maximize_window()
    driver.find_element(By.XPATH, men_link2).click()
    sleep(10)
    driver.find_element(By.XPATH, men_link3).click()
    sleep(10)
    driver.find_element(By.XPATH, men_link4).click()
    sleep(10)
    product_name = driver.find_element(By.XPATH, men_link5).text
    assert product_name == 'ATID Blue Shoes'
    driver.find_element(By.XPATH, men_link6).click()
    sleep(10)
    coupon_field = driver.find_element(By.XPATH,men_link7)
    sleep(12)
    coupon_field.click()
    coupon_field.send_keys("123fent")
    sleep(12)
    driver.find_element(By.XPATH, men_link8).click()
    sleep(3)
