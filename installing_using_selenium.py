from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui as pag
import time
username = 'u'
password = 'p'
licznik = 0
pag.FAILSAFE = True
while_var = True
url = 'https://instaling.pl'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

login_button = browser.find_element(By.XPATH, '//*[@id="navbar"]/a[2]/div[1]')
login_button.click()

username_field = browser.find_element(By.XPATH, '//*[@id="log_email"]')
username_field.send_keys(username)

password_field = browser.find_element(By.XPATH, '//*[@id="log_password"]')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

try:
    start_new_session = browser.find_element(By.XPATH,'//*[@id="student_panel"]/p[1]/a')
    start_new_session.click()

except:
    finish_session = browser.find_element(By.XPATH,'//*[@id="student_panel"]/p[1]/a')
    finish_session.click()

try:
    start_session = browser.find_element(By.XPATH,'//*[@id="start_session_button"]')
    start_session.click()
except:
    continue_session = browser.find_element(By.XPATH,'//*[@id="continue_session_button"]')
    continue_session.click()
    
end_check = browser.find_element(By.XPATH,'//*[@id="return_mainpage"]/h4')
end_display = end_check.is_displayed()

try:
    while while_var:
        
        #click check
        
        time.sleep(0.1)
        pag.click(956, 399)

        # Zebranie tekstu
        text_gather = WebDriverWait(browser, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="word"]')))
        text = text_gather.text
        print(text)
        
        #click next
        time.sleep(0.1)
        pag.click(956, 399)

        # Wpisanie tekstu
        enter_sentence = browser.find_element(By.XPATH,'//*[@id="answer"]')
        enter_sentence.clear()
        enter_sentence.send_keys(text)

finally:
    browser.close()
