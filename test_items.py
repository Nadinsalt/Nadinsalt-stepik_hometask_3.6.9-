from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_button_Add_to_basket_exists_on_the_page(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/") 
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert button is not None, 'button not found'
    
