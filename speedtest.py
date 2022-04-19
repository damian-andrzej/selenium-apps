# to start program you need webdriver installed for your 
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class InternetSpeedTester:
    def __init__(self):
        self.driver = webdriver.Edge()
        #self.up
        #self.down

    def get_net_speed(self):
        self.driver.get("https://www.speedtest.pl")
        time.sleep(2)
        zgoda = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]')
        zgoda.click()
        time.sleep(2)
        # klikanie start speedtest
        save = self.driver.find_element(By.XPATH, '//*[@id="tester"]/div[1]/div/div/div/div[1]')
        save.click()
        time.sleep(60)
        # pobieranie wyniku
        net_speed = self.driver.find_element(By.XPATH,
                                        '/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/span')
        print(net_speed.text)
        network_speed = float(net_speed.text)
        return network_speed


    def check_speed_requirements(self,speed):
        if speed < 500:
            print('Network speed is lower than  amount guaranteed in agreement ')


speedTester = InternetSpeedTester()
print(speedTester.get_net_speed())




