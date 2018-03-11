#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(800, 800))  
#display.start()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location="/usr/bin/google-chrome"
options.executable_path="/usr/bin/chromedriver"
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1200x600')
driver = webdriver.Chrome(
    "/usr/bin/chromedriver",
    chrome_options=options,
    service_args=['--verbose'],
    service_log_path="{}/chromedriver.log".format("./"))

driver.get("http://localhost")
print driver.title

driver.close()
driver.quit()