require "selenium-webdriver"

driver = Selenium::WebDriver.for :chrome
driver.navigate.to "https://app.jubelio.com/login"

sleep(5)