import checking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from prettytable import PrettyTable
from datetime import datetime
import time


class Checking:

    def __init__(self, teardown=False):
        options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument("--headless")
        options.add_experimental_option("detach", True)     
        self.driver = webdriver.Chrome(options=options)
        self.teardown = teardown
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def __enter__(self):
        return self 

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def garibaldi_click(self):
        garibaldi_element = self.driver.find_element(By.CSS_SELECTOR,
                'button[aria-label="Book a pass for Garibaldi Provincial Park"]'
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", garibaldi_element)
        garibaldi_element =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                'button[aria-label="Book a pass for Garibaldi Provincial Park"]')))
        time.sleep(0.25)
        garibaldi_element.click()
        

    def format_date(self, date):
        day_of_month = date.day

        if day_of_month > 9:
            date_format = "%A, %B %e, %Y"
        else:
            date_format = "%A, %B%e, %Y"

        formatted_date = date.strftime(date_format)
        return formatted_date
    
    def select_date(self, date):

        
        date_box_element = self.driver.find_element(By.CLASS_NAME, 'date-input__calendar-btn')
        time.sleep(1)
        date_box_element.click()
        date_element = self.driver.find_element(By.CSS_SELECTOR,
            f'div[aria-label="{date}"]'
        )
        date_element.click()

    def select_pass_type(self):
        pass_type_element = self.driver.find_element(By.CSS_SELECTOR, 'select[data-testid="passtype-select"]')
        pass_type_element.click()
        pass_type_element.send_keys(Keys.ARROW_DOWN)
        pass_type_element.send_keys(Keys.ARROW_DOWN)
        pass_type_element.send_keys(Keys.ENTER)
        time.sleep(0.25)

    def availability_status(self):
        booking_element = self.driver.find_element(By.CSS_SELECTOR, 'p[data-testid="day-availability-text"]')
        availability_element = booking_element.find_element(By.TAG_NAME, 'span')
        availability = availability_element.get_attribute('innerHTML').strip()
        return availability


