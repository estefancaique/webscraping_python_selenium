# YouTube Video: https://www.youtube.com/watch?v=eDrFWRi13DY
import os
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

# Old way of doing things that works with Firefox
# driver = webdriver.Firefox()
# driver.get("http:google.com")

chromedriver =(r"C:\Users\estefan\.wdm\drivers\chromedriver\win32\84.0.4147.30\chromedriver.exe")
driver = webdriver.Chrome(chromedriver)
driver.get("http:google.com")