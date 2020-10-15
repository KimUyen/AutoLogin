from selenium import webdriver
import argparse
import random
import time 

def Authorization_for_broadband(username, password, task):
    waiting_minutes = random.randrange(0, 20, 1)
    time.sleep(60*waiting_minutes)
    driver = webdriver.Chrome(".\chromedriver.exe")

    driver.get('https://***')
    driver.find_element_by_id('psnCode').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    if task == 'login':
        x_path = '//button[@class="btn btn-success pull-left"]'
    elif task == 'logout':
        x_path = '//button[@class="btn btn-warning pull-left"]'
    
    driver.find_element_by_xpath(x_path).click()
    driver.close
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='auto login to ***')
    parser.add_argument('--username', required=True,
                        help='staff code')
    parser.add_argument('--password', required=True,
                        help='password')
    parser.add_argument('--task', required=True,
                        help='login or logout')
    args = parser.parse_args()

    Authorization_for_broadband(args.username, args.password, args.task)