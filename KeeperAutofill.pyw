from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def launchBrowser() : #Wrapping Selenium tasks in a function prevents Selenium from closing the browser automatically
    o = webdriver.ChromeOptions()
    o.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data') #User data path so it launches your same profile
    o.add_argument('disable-infobars')
    o.add_experimental_option("detach", True)
    o.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=o)
    driver.maximize_window() #Start window 'maximized'
    driver.get('https://keepersecurity.eu/vault/#') #Navigate to default Keeper Vault Login Page
    #Username Input
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by.By.XPATH, '//*[@id="username-selector"]/div[1]/textarea'))) #Waits until the username textbox is available on screen
    element.click()
    element.clear() #Clear any existing text that may have been autofilled
    element.send_keys('example@email.com') #Sends your username to the websites username textbox
    driver.find_element(by.By.XPATH, '//*[@id="login"]/div[1]/div/button[1]').click() #Find the 'Next" button and clicks it
    #Password Input
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by.By.XPATH, '//*[@id="login"]/div[1]/div/div[3]/div/div/div/div/input'))) #Waits until the password textbox is available on screen
    element.click()
    element.clear() #Clear any existing text that may have been autofilled
    element.send_keys('Password') #Sends password to the websites password textbox
    driver.find_element(by.By.XPATH, '//*[@id="login"]/div[1]/div/button[1]').click() #Find the 'Login" button and clicks it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((by.By.XPATH, '//*[@id="header-main"]/nav/ul/li'))) #Waits until you are logged in before redirecting to a new webpage
    driver.get('https://www.youtube.com/feed/subscriptions') #Navigate to desired website after logging in for me it is YouTube
    
launchBrowser() #Executes function

