from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome


from urllib.request import urlopen
import os
import time

def launch():

	opts = ChromeOptions()
	opts.add_experimental_option("detach", True)
		
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

	return driver

def clickbutton(driver, number):

	#button = "//div[@title='{}']".format(number)
	button = "//div[text()='{}']".format(number)
	
	errormsg = "Unable to find the button"
	searchbutton = getElementByXpathOrWait(driver, button, 3, errormsg)
	if searchbutton:
		searchbutton.click()
	else:
		return errormsg
		
	#time.sleep(0.3)

	return 1

# delay in seconds
def getElementByXpathOrWait(driver, element_xpath, delay, timeoutmsg):
	try:
		return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
	except TimeoutException:
		print("Timeout error ({} seconds). {}".format(delay, timeoutmsg))
		return None
		
def waitInSeconds(seconds):
	for i in range(1,seconds+1):
		print(i)
		time.sleep(1)

def main():

	driver = launch()
	
	driver.get('http://zzzscore.com/1to50/en/')
	
	for i in range(1, 51):
		clickbutton(driver, i)

	print("DONE")

if __name__ == "__main__":
    main()