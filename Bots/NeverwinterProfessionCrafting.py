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

def LoadNewTask ():
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, 0);")
    print ("LoadNewTask...")
    try:
          print ("Trying to click on Leadership button...")
          element = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-url="/professions-tasks/Leadership"]')))
          element.click()
    except:
          print ("Fail!")
          return

    while 1:
      ##HERE NAVIGATE BUTTONS...
      try:
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5);")
          print ("Trying to laod Leadership_Tier1_4_Protect...")
          element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@data-url="/professions-tasks/Leadership/Leadership_Tier1_4_Protect"]')))
          element.click()
          element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@onclick="client.professionStartAssignment(\'Leadership_Tier1_4_Protect\')"]')))
          element.click()
          print ("Loaded")
          return
      except:
          print ("Fail!")
          pass

      try:
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.3);")
          print ("Trying to laod Leadership_Tier1_6_Protect...")
          element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@data-url="/professions-tasks/Leadership/Leadership_Tier1_6_Survey"]')))
          element.click()
          try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@onclick="client.professionStartAssignment(\'Leadership_Tier1_6_Survey\')"]')))
            element.click()
          except:
            try:
              #<button data-url="/professions-tasks/Leadership/Leadership_Tier1_5_Explore">
              print ("Trying click on Start Task...")
              element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@data-url="/professions-tasks/Leadership/Leadership_Tier1_5_Explore"]')))
              element.click()
              element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@onclick="client.professionStartAssignment(\'Leadership_Tier1_5_Explore\')"]')))
              element.click()
            except:
              print ("Fail to  load /Leadership_Tier1_5_Explore!")

      except:
          print ("Fail!")
          pass

      try:
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          print ("Try to click ->")
          #<a class="paginate_enabled_next" tabindex="0" role="button" id="tasklist_next" aria-controls="tasklist">Next</a>
          element = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="paginate_enabled_next"]')))
          element.click()
          pass
      except:
          print ("Fail to click ->")
          return

def Check_And_Update_Tasks():
	print ("In function..")
	#<a class="nav-button mainNav professions nav-professions selected">
	while 1:
		for i in range(5):
			'''
			print "--------" + str(i+1) + "--------"
			driver.execute_script("window.scrollTo(0, 0);")
			try:
			      print "Trying to click on professions button..."
			      element = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-url="/professions" and @class="tab subNav overview professions-overview"]')))
			      element.click()
			      print "Click on proffesions button."
			except:
			      print "Fail!"
			try:
			    print "Trying to click on professions button..."
			    #<button data-url-silent="/professions/finish-now/0"><span class="currency-icon astral"></span> Finish Now</button>
			    element = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-url="/professions" and @class="tab subNav overview professions-overview selected"]')))
			    element.click()
			    print "Click on proffesions button."
			except:
			    print "Fail!"


			##refresh page
			#driver.refresh()

			##if slot != "Finish Now"
			##then LoadNewTaks()
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.2);")
			try:
			    wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@data-url-silent="/professions/finish-now/'+str(i)+'"]')))
			    print "slot " + str(i) + " :busy!"
			    continue
			except:
			    print "slot " + str(i) + " :not busy!"
			    pass
			try:
				element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@data-url-silent="/professions/collect-reward/'+str(i)+'"]')))
				element.click()
				print "slot " + str(i) + " :click on collect result!"
				#<button onclick="client.professionTaskCollectRewards('535')" data-url="back"></button>
				element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(@onclick,"client.professionTaskCollectRewards")]')))
				element.click()
			except:
				print "Click on collect result fail!"
				pass

			LoadNewTask()


			##get timer element

			##get_text_excluding_children
			'''
			try:
			  timer = driver.find_element_by_xpath('//*[@id="update-content-professions-overview-0"]/span/div/div/ul/li['+str(i+1)+']/span/div/div[4]/div[3]/div[2]')
			  print ("------")
			  print (get_text_excluding_children(driver, timer))
			except:
			  print ("Unable to alocate...")
		print ("Sleep 15 seconds.")
		time.sleep(15)##every 15 seconds check and update proffesions

def test():
  print ("Getting gateway URL...")
  driver.get("https://gateway.playneverwinter.com/")

  '''
  //*[@id="content_login"]
  //*[@id="update-content-professions-overview-0"]/span/div/div/ul/li[1]/span/div/div[4]/div[3]/div[2]
  //*[@id="update-content-professions-overview-0"]/span/div/div/ul/li[2]/span/div/div[4]/div[3]/div[2]
  //*[@id="update-content-professions-overview-0"]/span/div/div/ul/li[3]/span/div/div[4]/div[3]/div[2]
  '''

  button = driver.find_element_by_xpath('//*[@id="form"]')


def LogInNeverwinter():
  LOGIN_BUTTON = '//input[@type="submit" and @value="Login"]'

  print ("Getting gateway URL...")
  driver.get("https://gateway.playneverwinter.com/")
  #assert "Python" in driver.title

  print ("Finding username text edin control...")
  elem = driver.find_element_by_name("user")
  elem.send_keys("yourEmail")

  print ("Finding password text edit control...")
  elem = driver.find_element_by_name("pass")
  elem.send_keys("yourPassword")


  button = driver.find_element_by_xpath(LOGIN_BUTTON)
  button.click()

  ##try to load cookis
  '''
  try:
      print "Trying to load cookies..."
      LoadCookies()
      print "Cookies loaded..."
  except:
  '''
  print ("Fail to load cookies...")
  ##input browser code
  browser_code = raw_input("Enter browser code: ")
  elem = driver.find_element_by_id("onetimecode-code")
  elem.send_keys(browser_code)
  ##click submit button
  button = driver.find_element_by_xpath('//button[@type="button" and @class="modal-button onetimecode-submit"]')
  button.click()

  ##trying to save cookies
  try:
	  print ("Trying to save cookies...")
	  SaveCookies()
  except:
	  print ("Fail to save cookies...")

  ##click hero button
  try:
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'Player_Trickster')))
    element.click()
  except:
    pass

  ##click proffesions button
  #<a class="nav-button mainNav professions nav-professions" data-url="#char(MagicMattock@vylshebnamotika)/professions">
  try:
    print ("Fail!")
    print ("Click on first Proffesion button second chance...")
    element = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-url="#char(MagicMattock@vylshebnamotika)/professions"]')))
    element.click()
  except:
    pass

  Check_And_Update_Tasks()

print ("Loading Firefox...")
driver = webdriver.Firefox()

print ("Maximizing firefox...")
driver.maximize_window()

wait = WebDriverWait(driver, 10)


LogInNeverwinter()
