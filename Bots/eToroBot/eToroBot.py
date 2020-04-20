import pickle
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC ##wait function: wait to load  web page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def LoadCookies():
    cookies = pickle.load(open("cookies1.pkl", "rb"))
    for cookie in cookies:
      driver.add_cookie(cookie)

def SaveCookies():
    pickle.dump( driver.get_cookies() , open("cookies1.pkl","wb"))


def get_text_excluding_children(driver, element):
    return driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)

def LogInEToro():
  LOGIN_BUTTON = '//button[@type="submit" and @value="Login"]'
  #<button automation-id="login-sts-btn-fb" class="sign-up-button sign-up-social-button facebook-button ng-scope" ng-if="loginCtrl.showFacebookConnect" ng-click="loginCtrl.loginWithSocialProvider('facebook')"><span>Facebook</span></button>
  #<span>Facebook</span>
  #/html/body/ui-layout/div/div/div[1]/login/login-sts/div/div/div/form/div/div[7]/div/button[1]
  print ("Getting gateway URL...")
  driver.get("https://www.etoro.com/login")

  time.sleep(10)
  print("trying to find a login button");
  button = driver.find_elements_by_xpath('/html/body/ui-layout/div/div/div[1]/login/login-sts/div/div/div/form/div/div[7]/div/button[1]')
  button.click()

print ("Loading Firefox...")
driver = webdriver.Firefox()

print ("Maximizing firefox...")
driver.maximize_window()

wait = WebDriverWait(driver, 10)


LogInEToro()
