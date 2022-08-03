import Youtube.constant as cons
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class TestCase(webdriver.Chrome):
      def __init__(self,  driver_path="usr/local/bin/chromedriver"):
            self.driver_path = driver_path
            super(TestCase, self).__init__()
            self.maximize_window()
 
      def home_page(self):
            self.get(cons.BASE_URL)
      
      def scroll_down(self):
            SCROLL_PAUSE_TIME = 0.5
          
            last_height = self.execute_script("return document.body.scrollHeight")
            while True:
                  self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                  time.sleep(SCROLL_PAUSE_TIME)
                  new_height = self.execute_script("return document.body.scrollHeight")
                  if new_height == last_height:
                        break
                  last_height = new_height
            time.sleep(2)
            home_menu = self.find_element(By.XPATH, cons.home_menu)
            home_menu.click()
            time.sleep(5)
      
      def play_quick_pick_non_login(self):
            container_play_button = self.find_element(By.XPATH, cons.container_play_button)
            container_play_button.click()
            play_button = self.find_element(By.XPATH, cons.play_button)
            play_button.click()
            time.sleep(3)
            pause_button = self.find_element(By.XPATH, cons.pause_button)
            pause_button.click()
            home_menu = self.find_element(By.XPATH, cons.home_menu)
            home_menu.click()
            time.sleep(5)

      def sign_in(self):
            sign_in_button = self.find_element(By.XPATH, cons.sign_in_button)
            sign_in_button.click()
            time.sleep(2)

            gmail_field = self.find_element(By.XPATH, cons.gmail_field)
            gmail_field.send_keys(cons.email)
            time.sleep(5)
            
            next_button = self.find_element(By.XPATH, cons.next_button1)
            next_button.click()
            time.sleep(5)

            password_field = self.find_element(By.XPATH, cons.password_field)
            password_field.send_keys(cons.password)
            time.sleep(5)

            next_button2 = self.find_element(By.XPATH, cons.next_button2)
            next_button2.click()
            time.sleep(5)

      def play_quick_pick_login(self):
            container_play_button = self.find_element(By.XPATH, cons.container_play_button)
            container_play_button.click()
            play_button = self.find_element(By.XPATH, cons.play_button)
            time.sleep(3)
            play_button.click()
            time.sleep(5)
            pause_button = self.find_element(By.XPATH, cons.pause_button)
            pause_button.click()
            home_menu = self.find_element(By.XPATH, cons.home_menu)
            home_menu.click()
            time.sleep(5)

      def search_specific_song(self):
            search_button = self.find_element(By.XPATH, cons.search_button)
            search_button.click()

            search_text_input = self.find_element(By.XPATH, cons.search_text_input)
            search_text_input.send_keys(cons.search_query)
             
            time.sleep(5)

            container_searched_button = self.find_element(By.XPATH, cons.container_searched_button)
            container_searched_button.click()
            time.sleep(5)

            searched_button = self.find_element(By.XPATH, cons.searched_button)
            searched_button.click()
            time.sleep(10)
