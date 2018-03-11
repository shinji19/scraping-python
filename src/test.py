from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1200x600')

service = Service(executable_path='/usr/local/bin/chromedriver')
service.start()

driver = webdriver.Remote(service.service_url, desired_capabilities=options.to_capabilities())

driver.get("http://localhost")

driver.close()
driver.quit()
