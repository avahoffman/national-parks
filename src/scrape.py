import os
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By


def setup_driver(url: str):
    driver = Chrome(os.getcwd() + "/src/chromedriver")
    driver.get(url)
    # Dive into iframe section
    frame = driver.find_element_by_xpath('/html/body/iframe')
    driver.switch_to.frame(frame)
    return (driver)


def wait_to_click(delay: int, xpath: str):
    query = WebDriverWait(driver, delay).until(EC.element_to_be_clickable(
        (By.XPATH, xpath))).click()  # Open dropdown
    return query


def build_traffic_data(driver: None):

    # Build dictionary of year: xpaths so that it can be iterated through
    year_html_dict = {2019: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl02"]',
                      2018: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl03"]',
                      2017: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl04"]',
                      2016: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl05"]'}

    try:
        counter = 1

        for year in year_html_dict:
            # Ensure no years selected to start
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # Select all
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # deselect all
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown

            # Years dropdown, make sure to select only one year
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(20, year_html_dict[year])  # Select year
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown

            if counter == 1:
                # Regions drop down
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Open dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl00"]')  # Select all
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Close dropdown

                # Parks drop down - this MUST come after Regions dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Open dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl11_divDropDown_ctl00"]')  # Select all
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Close dropdown

            # Generate report
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl00"]')  # Report

            # Save dropdown
            wait_to_click(20, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Open save dropdown
            # wait_to_click(20, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_Menu"]/div[2]/a')  # Save as csv
            wait_to_click(20, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Close save dropdown

            counter += 1

        driver.quit()

    except:

        driver.quit()


def build_visit_data(driver: None):

    # Build dictionary of year: xpaths so that it can be iterated through
    year_html_dict = {2018: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl02"]',
                      2017: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl03"]',
                      2016: '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl04"]'}

    try:
        counter = 1

        for year in year_html_dict:
            # Ensure no years selected to start
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # Select all
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_divDropDown_ctl00"]')  # deselect all
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown

            # Years dropdown, make sure to select only one year
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Open dropdown
            wait_to_click(20, year_html_dict[year])  # Select year
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl03_ddDropDownButton"]')  # Close dropdown

            if counter == 1:
                # Regions dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Open dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl07_divDropDown_ctl00"]')  # Select all
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl07_ddDropDownButton"]')  # Close dropdown

                # Parks dropdown - this MUST come after Regions dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Open dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl11_divDropDown_ctl00"]')  # Select all
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl11_ddDropDownButton"]')  # Close dropdown

                # Other fields dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl15_ddDropDownButton"]')  # Open dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl15_divDropDown_ctl00"]')  # Select all add'l fields
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl15_ddDropDownButton"]')  # Close dropdown

                # Types of visits
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl13_ddDropDownButton"]')  # Open dropdown
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl13_divDropDown_ctl00"]')  # Select all types
                wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl13_ddDropDownButton"]')  # Close dropdown

            # Generate report
            wait_to_click(20, '//*[@id="ReportViewer_ctl04_ctl00"]')  # Report

            # Save dropdown
            wait_to_click(20, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Open save dropdown
            #wait_to_click(20, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_Menu"]/div[2]/a')  # Save as csv
            wait_to_click(20, '//*[@id="ReportViewer_ctl05_ctl04_ctl00_ButtonImg"]')  # Close save dropdown

            counter += 1

        driver.quit()

    except:

        driver.quit()


if __name__ == '__main__':
    # driver = setup_driver(
    #     url="https://irma.nps.gov/STATS/SSRSReports/National%20Reports/Query%20Builder%20for%20Traffic%20Counts%20(1985%20-%20Last%20Calendar%20Year)"
    # )
    #
    # build_traffic_data(driver)

    # driver = setup_driver(
    #     url="https://irma.nps.gov/STATS/SSRSReports/National%20Reports/Query%20Builder%20for%20Public%20Use%20Statistics%20(1979%20-%20Last%20Calendar%20Year)"
    # )
    #
    # build_visit_data(driver)
