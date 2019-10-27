from os import environ
from selenium import webdriver


def login():
    with webdriver.Chrome() as driver:
        driver.get(environ['login_url'])
        driver.find_element_by_id(
            environ['username_id']
        ).send_keys(environ['username'])
        driver.find_element_by_id(
            environ['password_id']
        ).send_keys(environ['password'])
        driver.find_element_by_id(
            environ['submit_btn_id']
        ).click()


if __name__ == '__main__':
    login()