import os, csv
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By


def setup_driver(url: str):
	driver = Chrome( os.getcwd() + "/src/chromedriver" )
	driver.get(url)
	# Dive into iframe section
	frame = driver.find_element_by_xpath('/html/body/iframe')
	driver.switch_to.frame(frame)
	return(driver)
		
		
def build_traffic_data(driver: None):

	year_html_dict = { 2019: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl02"]', 2018: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl03"]'}
		
	try:
		for year in year_html_dict:
			# Ensure no years selected to start
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]').click() # Open dropdown
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]').click() # Select all
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]').click() # deselect all
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]').click() # Close dropdown
			
			# Years dropdown, make sure to select all
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]').click() # Open dropdown
			driver.find_element_by_xpath(year_html_dict[year]).click() #Select year
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]').click() # Close dropdown
			
			# Regions drop down
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]').click() # Open dropdown
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl00"]').click() #Select all
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]').click() # Close dropdown
			
			# Parks drop down - this MUST come after Regions dropdown
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]'))).click() # Open dropdown
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl11_divDropDown_ctl00"]').click() #Select all
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]').click() # Close dropdown
			
			# Generate report
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl04_ctl00"]').click() # Report
			
			driver.implicitly_wait(45)
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonLink"]').click() # Open save dropdown
			driver.find_element_by_xpath('//*[@id="ReportViewer_ctl05_ctl04_ctl00_Menu"]/div[2]/a').click() # Save as csv
					
			driver.quit()
	except:
		driver.quit()
	
driver = setup_driver(url = "https://irma.nps.gov/STATS/SSRSReports/National%20Reports/Query%20Builder%20for%20Traffic%20Counts%20(1985%20-%20Last%20Calendar%20Year)")

build_traffic_data(driver)