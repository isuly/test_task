import webAuto
import fileAuto
from selenium import webdriver
import logging
import time
import lackey
import pyautogui
from selenium.webdriver.common.keys import Keys
import csv
import os
import datetime

logging.basicConfig(filename='C:/pyrobot/logger.log', level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
        path = 'C:/pyrobot'
        if not os.path.exists(path):
            os.makedirs(path)

        try:
              driver = webdriver.Chrome()
        except:
             driver = webdriver.Firefox()
        web = webAuto.webAuto()
        try:
            logger.info('Information gathering started')
            info = web.getAllInf(driver)
        except Exception as ex:
            template = "An exception of type {0} occurred."
            message = template.format(type(ex).__name__)
            logger.info(message)
        else:
            logger.info('Information assembly was completed')
            file = fileAuto.fileAuto()
            try:
                logger.info('Started writing to file')
                file.write(info)
            except Exception as ex:
                template = "An exception of type {0} occurred."
                message = template.format(type(ex).__name__)
                logger.info(message)
            else:
                logger.info('Writing to file was finished')
                try:
                    logger.info('Message sending was started')
                    web.sendMsg(driver)
                except Exception as ex:
                    template = "An exception of type {0} occurred."
                    message = template.format(type(ex).__name__)
                    logger.info(message)
                else:
                    logger.info('Message sent successfully')
        driver.close()

