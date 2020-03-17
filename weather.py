from selenium import webdriver 
import time 
from selenium.webdriver.chrome.options import Options


WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
  
# set webdriver path here it may vary 
# ,options=chrome_options
brower = webdriver.Chrome(executable_path ='C:/Users/dilee/Downloads/chromedriver_win32/chromedriver.exe') 
  
website_URL ="https://www.meteoblue.com/en/weather/week/jakarta_indonesia_1642911"
brower.get(website_URL) 
print(brower.title)

brower.find_element_by_id("gdpr_form").click()

time.sleep(10)

brower.find_element_by_class_name("additional_parameters_toggle").click()

time.sleep(10)
# After how many seconds you want to refresh the webpage 
# Few website count view if you stay there 
# for a particular time 
# you have to figure that out 
# brower.close()


table_id=brower.find_element_by_class_name("hourlywind")
rows = table_id.find_elements_by_tag_name("tr")
Data=[]
for row in rows:
    # Get the columns (all the column 2)
    temp=[]
    for eachtd in row.find_elements_by_tag_name("td"):
    	temp.append((eachtd.text).strip())
    Data.append(temp)
print(Data)
    # col = row.find_elements_by_tag_name("td")[1] #note: index start from 0, 1 is col 2
    # print(col.text)#prints text from the element
