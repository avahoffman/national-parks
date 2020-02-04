"""
THIS CODE IS ONLY TO BE USED FOR ACADEMIC AND LEARNING PURPOSES!
"""

import os, csv
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By


def setup_driver(url: str):
    """
    Sets up a Chrome browser driver at a specified url.

    :param url: url to navigate to
    :return: selenium webdriver (Chrome)
    """
    driver = Chrome(os.getcwd() + "/src/chromedriver")
    driver.get(url)
    # Dive into iframe section
    frame = driver.find_element_by_xpath('/html/body/iframe')
    driver.switch_to.frame(frame)
    return (driver)


def wait_to_click(driver: None,
                  xpath: str,
                  delay: int = 20):
    """
    Selenium webdriver action that waits until an element is clickable.

    :param driver: selenium webdriver object
    :param xpath: html address
    :param delay: time to wait until clickable action
    :return: selenium web-element action
    """
    query = WebDriverWait(driver, delay).until(EC.element_to_be_clickable(
        (By.XPATH, xpath))).click()  # Open clickable item
    return query


def wait_to_read(driver: None,
                 button_xpath: str,
                 table_xpath: str,
                 delay: int = 20):
    """
    Selenium webdriver action that uses a clickable element to gauge whether a table can be read.

    :param driver: selenium webdriver
    :param button_xpath: clickable element address (e.g., the 'View Report' button)
    :param table_xpath: html address for the table (must be FULL path)
    :param delay: time to wait for clickable item AND table address
    :return: selenium web-element
    """
    # First wait until the report is fully loaded and button is once again clickable
    WebDriverWait(driver, delay).until(EC.element_to_be_clickable(
        (By.XPATH, button_xpath)))  # Don't click just wait
    # Then save the table object
    query = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, table_xpath)))  # read table or element
    return query


def write_html_to_csv(table: None, filename: str):
    """
    Function iterates through lines of a selenium web-element and writes to a csv

    :param table: selenium web-element
    :param filename: filename into which to write lines of 'table'
    :return: outputs to csv and also writes progress into the console
    """
    with open(filename, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        linecounter = 0
        for row in table.find_elements_by_css_selector('tr'):
            wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
            linecounter += 1
            if linecounter % 25 == 0:
                print(str(linecounter) + " lines written to " + filename)


def build_traffic_data(driver: None,
                       scan_table: bool = False,
                       download_link: bool = False):
    """
    Collects data on number of park traffic counts. Separate files are by year.

    :param driver: selenium webdriver
    :param scan_table: indicates to collect data by scanning the html table
    :param download_link: indicates to click the download link and save to csv. Although much faster than crawling
    through html, this flag is not recommended because there are often issues with exceeding download requests.
    :return: writes to .csv if scan_table or download_link is flagged
    """

    # Build dictionary of year: xpaths so that it can be iterated through
    year_html_dict = {2019: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl02"]',
                      2018: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl03"]',
                      2017: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl04"]',
                      2016: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl05"]'}

    try:
        counter = 1

        for year in year_html_dict:
            # Ensure no years selected to start
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # Select all
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # deselect all
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown
            # Years dropdown, make sure to select only one year
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(driver, year_html_dict[year])  # Select year
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown

            if counter == 1:
                # Regions drop down
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl00"]')  # Select all
                # wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl00"]')  # deselect all
                # wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl02"]')  # Select AK
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Close dropdown
                # National parks/monuments only
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_divDropDown_ctl00"]')  # Deselect all
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_divDropDown_ctl11"]')  # Select national monuments
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_divDropDown_ctl12"]')  # Select national parks
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_ddDropDownButton"]')  # Close dropdown
                # Parks drop down - this MUST come after Regions dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl11_divDropDown_ctl00"]')  # Select all
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Close dropdown
                # Other fields
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl13_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl13_divDropDown_ctl00"]')  # Select all
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl13_ddDropDownButton"]')  # Close dropdown

            # Generate report
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl00"]')  # Report

            if scan_table:
                # Need the FULL xpath for the table
                table = wait_to_read(driver,
                                     button_xpath='//*[@id="ReportViewer_ctl04_ctl00"]',
                                     table_xpath='/html/body/form/div[3]/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[4]/td[1]/table'
                                     )
                # Iterate through table items
                write_html_to_csv(table=table,
                                  filename=("data/traffic_counts_" + str(year) + ".csv"))
            if download_link:
                # Save dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Open save dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_Menu"]/div[2]/a')  # Save as csv
                wait_to_click(driver, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Close save dropdown

            counter += 1

        print("All traffic queries successful")
        driver.quit()

    except:

        print("Traffic queries interrupted")
        driver.quit()


def build_visit_data(driver: None,
                     scan_table: bool = False,
                     download_link: bool = False):
    """
    Collects data on number of park visitors of many types by month and year. Separate files are by year.

    :param driver: selenium webdriver
    :param scan_table: indicates to collect data by scanning the html table
    :param download_link: indicates to click the download link and save to csv. Although much faster than crawling
    through html, this flag is not recommended because there are often issues with exceeding download requests.
    :return: writes to .csv if scan_table or download_link is flagged
    """

    # Build dictionary of year: xpaths so that it can be iterated through
    year_html_dict = {
        2018: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl02"]',
        2017: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl03"]',
        2016: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl04"]',
        2015: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl05"]',
        2014: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl06"]',
        2013: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl07"]',
        2012: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl08"]',
        2011: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl09"]',
        2010: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl10"]',
        2009: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl11"]',
        2008: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl12"]',
        2007: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl13"]',
        2006: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl14"]',
        2005: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl15"]',
        2004: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl16"]',
        2003: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl17"]',
        2002: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl18"]',
        2001: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl19"]',
        2000: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl20"]',
        1999: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl21"]',
        1998: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl22"]',
        1997: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl23"]',
        1996: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl24"]',
        1995: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl25"]',
        1994: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl26"]',
        1993: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl27"]',
        1992: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl28"]',
        1991: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl29"]',
        1990: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl30"]',
        1989: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl31"]',
        1988: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl32"]',
        1987: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl33"]',
        1986: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl34"]',
        1985: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl35"]',
        1984: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl36"]',
        1983: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl37"]',
        1982: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl38"]',
        1981: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl39"]',
        1980: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl40"]',
        1979: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl41"]'
    }

    try:
        counter = 1

        for year in year_html_dict:
            # Ensure no years selected to start
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # Select all
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # deselect all
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown
            # Years dropdown, make sure to select only one year
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(driver, year_html_dict[year])  # Select year
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown

            if counter == 1:
                # Regions dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl00"]')  # Select all
                # wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl00"]')  # Deselect all
                # wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl02"]')  # Select AK
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Close dropdown
                # National parks/monuments only
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_divDropDown_ctl00"]')  # Deselect all
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_divDropDown_ctl11"]')  # Select national monuments
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_divDropDown_ctl12"]')  # Select national parks
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl09_ddDropDownButton"]')  # Close dropdown
                # Parks dropdown - this MUST come after Regions dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl11_divDropDown_ctl00"]')  # Select all
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Close dropdown
                # Other fields dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl15_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl15_divDropDown_ctl00"]')  # Select all add'l fields
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl15_ddDropDownButton"]')  # Close dropdown
                # Types of visits
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl13_ddDropDownButton"]')  # Open dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl13_divDropDown_ctl00"]')  # Select all types
                wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl13_ddDropDownButton"]')  # Close dropdown

            # Generate report
            wait_to_click(driver, '//*[@id="ReportViewer_ctl04_ctl00"]')  # Report

            if scan_table:
                # Need the FULL xpath for the table
                table = wait_to_read(driver,
                                     button_xpath='//*[@id="ReportViewer_ctl04_ctl00"]',
                                     table_xpath='/html/body/form/div[3]/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table'
                                     )
                # Iterate through table items
                write_html_to_csv(table=table,
                                  filename=("data/visits_" + str(year) + ".csv"))

            if download_link:
                # Save dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Open save dropdown
                wait_to_click(driver, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_Menu"]/div[2]/a')  # Save as csv
                wait_to_click(driver, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Close save dropdown

            counter += 1

        print("All visit queries successful")
        #driver.quit()

    except:

        print("Visit queries interrupted")
        #driver.quit()


def run_data_scrapers():
    driver = setup_driver(
        url="https://irma.nps.gov/STATS/SSRSReports/National%20Reports/Query%20Builder%20for%20Traffic%20Counts%20(1985%20-%20Last%20Calendar%20Year)"
    )
    build_traffic_data(driver, scan_table=True)

    driver = setup_driver(
        url="https://irma.nps.gov/STATS/SSRSReports/National%20Reports/Query%20Builder%20for%20Public%20Use%20Statistics%20(1979%20-%20Last%20Calendar%20Year)"
    )
    build_visit_data(driver, scan_table=True)


if __name__ == '__main__':
    run_data_scrapers()
