import time
import pdfkit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url=raw_input("Enter the url without quotes\n")
print(url)
phantomjs_path="/usr/local/bin/phantomjs"

driver = webdriver.PhantomJS(executable_path=phantomjs_path)
driver.set_window_size(1366, 768) # optional
driver.get(url)   # Go to the specified url
time.sleep(3)

raw_html = driver.page_source		#returns html code of the complete page

file_name = url.split('/')[-1]+'.pdf'
pdfkit.from_string(raw_html,file_name)