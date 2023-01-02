from time import sleep

from Facebook.BaseTest.login_location import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_log_in():
    driver = webdriver.Chrome()
    driver.get(loginLink1 )
    driver.maximize_window()
    email_field = driver.find_element(By.XPATH, loginLink2)
    sleep(12)
    email_field.click()
    email_field.send_keys("fentahunadisu16@gmail.com")
    sleep(12)
    password_field = driver.find_element(By.XPATH, loginLink3)
    sleep(12)
    password_field.click()
    password_field.send_keys("0587374134")
    sleep(12)
    driver.find_element(By.XPATH, loginLink4).click()
    sleep(3)

def test_login_rongEmail():
    driver = webdriver.Chrome()
    driver.get(loginLink1 )
    driver.maximize_window()
    email_field = driver.find_element(By.XPATH, loginLink2)
    sleep(12)
    email_field.click()
    email_field.send_keys("entahunadisu16@gmail.com")
    sleep(12)
    password_field = driver.find_element(By.XPATH, loginLink3)
    sleep(12)
    password_field.click()
    password_field.send_keys("587374134")
    sleep(12)
    driver.find_element(By.XPATH, loginLink4).click()
    sleep(3)

def test_login_rong_nill():
    driver = webdriver.Chrome()
    driver.get(loginLink1 )
    driver.maximize_window()
    email_field = driver.find_element(By.XPATH, loginLink2)
    sleep(12)
    email_field.click()
    email_field.send_keys("")
    sleep(12)
    password_field = driver.find_element(By.XPATH, loginLink3)
    sleep(12)
    password_field.click()
    password_field.send_keys("")
    sleep(12)
    driver.find_element(By.XPATH, loginLink4).click()
    sleep(3)


def test_login_without_email():
    driver = webdriver.Chrome()
    driver.get(loginLink1 )
    driver.maximize_window()
    email_field = driver.find_element(By.XPATH, loginLink2)
    sleep(12)
    email_field.click()
    email_field.send_keys("")
    sleep(12)
    password_field = driver.find_element(By.XPATH, loginLink3)
    sleep(12)
    password_field.click()
    password_field.send_keys("587374134")
    sleep(12)
    driver.find_element(By.XPATH, loginLink4).click()
    sleep(3)

def test_login_without_password():
    driver = webdriver.Chrome()
    driver.get(loginLink1 )
    driver.maximize_window()
    email_field = driver.find_element(By.XPATH, loginLink2)
    sleep(12)
    email_field.click()
    email_field.send_keys("entahunadisu16@gmail.com")
    sleep(12)
    password_field = driver.find_element(By.XPATH, loginLink3)
    sleep(12)
    password_field.click()
    password_field.send_keys("")
    sleep(12)
    driver.find_element(By.XPATH, loginLink4).click()
    sleep(3)
