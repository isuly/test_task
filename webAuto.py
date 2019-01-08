import time
import lackey
import pyautogui
from selenium.webdriver.common.keys import Keys
import logging
import os

class webAuto:
    def __init__(self):
        logging.basicConfig(filename='C:/pyrobot/logger.log', level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    def getAllInf(self, driver):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        xpath = '/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a[1]/div/div[1]/div[3]/div[1]/span[1]/span'
        driver.get("https://www.cbr.ru/")
        elem = driver.find_elements_by_class_name('w_data_wrap')
        info = [0, 0, 0, 0]
        part = elem[0].text.split('\n')
        info[0] = part[2].replace(',', '.')
        part = elem[1].text.split('\n')
        info[1] = part[2].replace(',', '.')
        logger.info('www.cbr.ru loaded')
        driver.get("https://www.gismeteo.ru/weather-kazan-4364/")
        temperatureKzn = driver.find_element_by_xpath(xpath)
        fixedStr = temperatureKzn.text.replace(',', '.')
        fixedStr = fixedStr.replace('−', '-')
        info[2] = fixedStr
        logger.info('www.gismeteo.ru/weather-kazan-4364/ loaded')
        driver.get("https://www.gismeteo.ru/weather-moscow-4368/")
        temperatureMsk = driver.find_element_by_xpath(xpath)
        fixedStr = temperatureMsk.text.replace(',', '.')
        fixedStr = fixedStr.replace('−', '-')
        info[3] = fixedStr
        logger.info('www.gismeteo.ru/weather-moscow-4368/ loaded')
        return info

    def sendMsg(self, driver):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        driver.get("https://mail.ru/")
        try:
            driver.find_element_by_id("mailbox:submit")
        except Exception:
            driver.find_element_by_id("P_Exit_16x16").click()
        finally:
            driver.find_element_by_id("mailbox:login").send_keys("test.task.robot@mail.ru")
            driver.find_element_by_id("mailbox:password").send_keys('AF1234')
            driver.find_element_by_id("mailbox:submit").click()
        logger.info('Authorization on mail.ru complete successfully')
        time.sleep(2)
        driver.find_element_by_link_text("Написать письмо").click()
        lack = lackey.Screen(0)
        time.sleep(2)
        driver.find_element_by_class_name("b-input").send_keys("   test.task.robot@mail.ru")
        #fileDir = r'C:\Users\Public\test_task'
        filename = os.path.join(fileDir, r'img\file.jpg')
        print(filename)
        lack.click(filename)
        time.sleep(4)
        lack.paste(r'C:\pyrobot\users.csv')
        pyautogui.hotkey('enter')
        driver.find_element_by_link_text("Написать письмо").send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(4)
        try:
            filename = os.path.join(fileDir, r'img\continue.jpg')
            print(filename)
            lack.click(filename)
        except Exception:
            driver.find_element_by_id("PH_logoutLink").click()
        else:
            driver.find_element_by_id("PH_logoutLink").click()

