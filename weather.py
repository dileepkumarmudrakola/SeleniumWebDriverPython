from selenium import webdriver 
import time 
from selenium.webdriver.chrome.options import Options
import pyodbc
from datetime import datetime


WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
  
# set webdriver path here it may vary 
# ,options=chrome_options
# brower = webdriver.Chrome(executable_path ='C:/Users/dilee/Downloads/chromedriver_win32/chromedriver.exe') 
brower = webdriver.Chrome(executable_path ='F:/DILEEP/Weather/SeleniumWebDriverPython/chromedriver.exe') 
 
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
db_con='DRIVER={SQL Server Native Client 11.0};SERVER=SURESHRAJ;DATABASE=Weather;UID=sa;PWD=user@123; MARS_Connection=yes;'
Weather_Data_Con=pyodbc.connect(db_con)


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

for i in range(0,len(Data[0])):
	current_date=datetime.now().strftime("%Y-%m-%d")
	sql="INSERT into Weather_Data (Date, Hour, Temp, Wind_Speed, Wind_Gust) VALUES \
	('"+current_date+"', '"+Data[0][i]+"', '"+Data[3][i]+"', '"+Data[5][i]+"', '"+Data[6][i]+"')"
	Weather_Data_Con.execute(sql)

Weather_Data_Con.commit()
Weather_Data_Con.close()