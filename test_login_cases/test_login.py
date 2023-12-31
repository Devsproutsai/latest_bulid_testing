# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from basic_plan.config_reader import readconfig_file




class Test_Login_Cases():
  
  @classmethod
  def setup_class(cls):
    cls.driver = webdriver.Chrome()
    cls.driver.maximize_window()
    cls.vars = {}

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
  
  @pytest.mark.parametrize("username, password", [
        (readconfig_file("Login_Credentials", 'Login_username'), readconfig_file("Login_Credentials", 'Login_password')),
        (readconfig_file("Login_Credentials", 'case1_Login_username'), readconfig_file("Login_Credentials", 'case1_Login_password')),
        (readconfig_file("Login_Credentials", 'case2_Login_username'), readconfig_file("Login_Credentials", 'case2_Login_password')),
    ])
  def test_login(self, username, password):
      wait = WebDriverWait(self.driver, 10)

      self.driver.get(readconfig_file("Links", 'google_url'))
      self.driver.get(readconfig_file("Links", 'Login_Url'))

      email_element = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".w-full:nth-child(4)")))
      email_element.click()

      send_email_element = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".w-full:nth-child(4)")))
      send_email_element.send_keys(username)

      password_element = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".border:nth-child(1)")))
      password_element.click()

      send_password_element = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".border:nth-child(1)")))
      send_password_element.send_keys(password)

      show_password = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".absolute > svg")))
      show_password.click()

      login_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
      login_button.click()


      try:
        # Wait for the "Post new job" element
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(.,\'Post new job\')]")))
        print('successfull login')

      except TimeoutException:
          assert False, "Test failed due to incorrect username or password"

      # Check if "Post new job" is present after login
      assert "Post new job" in self.driver.page_source, "Post new job not found after login"


      logout_menu = wait.until(expected_conditions.element_to_be_clickable((By.ID, "job?.id")))
      logout_menu.click()

      logout_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "h5:nth-child(1)")))
      logout_button.click()

      time.sleep(3)
