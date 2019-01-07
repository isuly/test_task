import csv
import os
import datetime


class fileAuto:
    def __init__(self):
        path = 'C:/pyrobot'
        if not os.path.exists(path):
            os.makedirs(path)

    def write(self, info):
        now = datetime.datetime.now()
        path = 'C:/pyrobot'
        user = [datetime.date.today(), now.strftime("%H:%M"), info[0], info[1], info[2], info[3]]
        filename = 'users.csv'
        FILENAME = path+'/'+filename
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(user)

