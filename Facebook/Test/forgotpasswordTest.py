from time import sleep

from Facebook.BaseTest.forgotpassword_l0ocation import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_forgotPassword():
    driver = webdriver.Chrome()
    driver.get(forgotPasswordLink1 )
    driver.maximize_window()
    driver.find_element(By.XPATH, forgotPasswordLink2).click()
    sleep(12)
    email = driver.find_element(By.XPATH, forgotPasswordLink3)
    sleep(12)
    email.click()
    email.send_keys("fentahunadisu16@gmail.com")
    sleep(12)
    driver.find_element(By.XPATH, forgotPasswordLink4).click()
    sleep(30)