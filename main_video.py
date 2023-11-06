import csv
import enum
import os
import sys
import pandas as pd
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QMessageBox, QProgressBar, QLCDNumber, QLabel
from multi_combox import CheckableComboBox
from simple_facerec import SimpleFacerec
import cv2
import datetime
from design import *
from setting import *
import winsound

pic = 'images'
sfr = SimpleFacerec()
classN1 = []
classN2 = []
late = 'L'
yes = '+'
c = ' '
face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
time = str(datetime.datetime.now().strftime('%H:%M:%S'))
dont = '-'
wait_time = 1000
electrical1 = ["Tr1 pto", "Tr3 63_sex"]
# electrical2 = ["E-201", "E-202", "E-203", "E-204", "E-205", "E-206"]
# architecture1 = ["A-101", "A-102", "A-103", "A-104", "A-105", "A-106"]
# architecture2 = ["A-201", "A-202", "A-203", "A-204", "A-205", "A-206"]
# civil1 = ["C-101", "C-102", "C-103", "C-104", "C-105", "C-106"]
# civil2 = ["C-201", "C-202", "C-203", "C-204", "C-205", "C-206"]



class Cam(QMainWindow):
    path = 'detected-sound.mp3'
    # class constructor

    def __init__(self):
        path = 'detected-sound.mp3'
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.camera)
        self.ui.pushButton_1.clicked.connect(sys.exit)
        self.ui.pushButton_2.clicked.connect(self.creates)
        self.ui.pushButton_3.clicked.connect(self.save)
        self.ui.pushButton_4.clicked.connect(sys.exit)
        self.ui.pushButton_5.clicked.connect(self.showMinimized)
        self.ui.pushButton_6.clicked.connect(self.settingwindow)
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(115, 540, 305, 20)
        self.pbar.setStyleSheet("background-color: rgb(0,0,0,100)")
        self.lcd = self.findChild(QLCDNumber, "lcdNumber")
        self.combo1 = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox, "comboBox_2")
        self.combo3 = CheckableComboBox(self)
        self.combo3.setGeometry(150, 410, 301, 22)
        self.combo3.addItems(electrical1)
        # self.combo1.addItem("1-Course")
        # self.combo1.addItem("2-Course")
        # self.combo2.addItem("Electrical and Computer Engineering")
        # self.combo2.addItem("Architecture")
        # self.combo2.addItem("Civil")
        # self.combo1.activated.connect(self.clicker)
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_num)
        self.t = 0
        self.s = 0

    def settingwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def lcd_num(self):
        self.s += 1
        while self.s == 60:
            self.s = 0
            self.t = self.t + 1
        self.lcd.display(f'{self.t}:{self.s}')
        if self.t == 30:
          self.timer.stop()



    # def clicker(self, index):
    #     course = self.ui.comboBox.currentText()
    #     facultate = self.ui.comboBox_2.currentText()
    #     if course == '1-Course' and facultate == 'Electrical and Computer Engineering':
    #         self.combo3.clear()
    #         self.combo3.addItems(electrical1)
    #     else:
    #         self.combo3.clear()
    #
    #     # elif course == '1-Course' and facultate == 'Architecture':
    #     #     self.combo3.clear()
    #     #     self.combo3.addItems(architecture2)
    #     # elif course == '1-Course' and facultate == 'Civil':
    #     #     self.combo3.clear()
    #     #     self.combo3.addItems(civil2)
    #     # elif course == '2-Course' and facultate == 'Electrical and Computer Engineering':
    #     #     self.combo3.clear()
    #     #     self.combo3.addItems(electrical1)
    #     # elif course == '2-Course' and facultate == 'Architecture':
    #     #     self.combo3.clear()
    #     #     self.combo3.addItems(architecture1)
    #     # elif course == '2-Course' and facultate == 'Civil':
    #     #     self.combo3.clear()
    #     #     self.combo3.addItems(civil1)

    def apcend(self, name):
        group = self.combo3.currentText()
        group1 = group[0:5]
        with open(f'{group}/{date} {group1}.csv', 'r+', ) as f:
            myData = f.readlines()
            nameList = []
            for line in myData:
                entr = line.split(',')
                nameList.append(entr[0])
            if name not in nameList:
                f.writelines(f'{name}, {late}, {time}, {date}\n')
        f.close()

    def apcend2(self, names):
        group = self.combo3.currentText()
        group2 = group[7:]
        with open(f'{group}/{date} {group2}.csv', 'r+', ) as f:
            myData = f.readlines()
            nameList = []
            for line in myData:
                entr = line.split(',')
                nameList.append(entr[0])
            if names not in nameList:
                f.writelines(f'{names}, {late}, {time}, {date}\n')
        f.close()

    def marks(self, name):
        course = self.ui.comboBox.currentText()
        facultate = self.ui.comboBox_2.currentText()
        group = self.combo3.currentText()
        group1 = group[0:5]
        with open(f'{course}/{facultate}/{group}/{date} {group1}.csv', 'r+',) as f:
            myData = f.readlines()
            nameList = []
            for line in myData:
                entr = line.split(',')
                nameList.append(entr[0])
            if name not in nameList:
                f.writelines(f'{name}, {yes}, {time}, {date}\n')
        f.close()

    def mark(self, names):
        group = self.combo3.currentText()
        group2 = group[7:]
        with open(f'{group}/{date} {group2}.csv', 'r+',) as f:
            myData = f.readlines()
            nameList = []
            for line in myData:
                entr = line.split(',')
                nameList.append(entr[0])
            if names not in nameList:
                f.writelines(f'{names}, {yes}, {time}, {date}\n')
        f.close()

    def save1(self):
        group = self.combo3.currentText()
        group1 = group[0:5]
        with open(f'{group}/{date} {group1}.csv', 'r+', ) as fs:
            myData = fs.readlines()
            nameList = []
            for line in myData:
                entr = line.split(',')
                nameList.append(entr[0])
            for apend in classN1:
                if apend not in nameList:
                    fs.write(f'{apend}, {dont}, {c}, {date}\n')
        df = pd.read_csv(f'{group}/{date} {group1}.csv')
        df[~df.duplicated(subset=['Fullname', 'Check', 'Time', 'Date'])].to_csv(f'{group}/{date} {group1}.csv', index=False)

    def save2(self):
        group = self.combo3.currentText()
        group2 = group[7:]
        with open(f'{group}/{date} {group2}.csv', 'r+', ) as fs:
            myData = fs.readlines()
            nameList = []
            for line in myData:
                entr = line.split(',')
                nameList.append(entr[0])
            for apend in classN2:
                if apend not in nameList:
                    fs.write(f'{apend}, {dont}, {c}, {date}\n')
        df = pd.read_csv(f'{group}/{date} {group2}.csv')
        df[~df.duplicated(subset=['Fullname', 'Check', 'Time', 'Date'])].to_csv(f'{group}/{date} {group2}.csv',index=False)

    def save(self):
        try:
            group = self.combo3.currentText()
            group1 = group[0:5]
            group2 = group[7:]
            if group1 == group:
                self.save1()
                read1 = pd.read_csv(f'{group}/{date} {group1}.csv')
                read1.to_excel(f'{group}/{date} {group1}.xlsx', index=None, header=True)
                os.remove(f'{group}/{date} {group1}.csv')
            else:
                self.save1()
                self.save2()
                read1 = pd.read_csv(f'{group}/{date} {group1}.csv')
                read1.to_excel(f'{group}/{date} {group1}.xlsx', index=None, header=True)
                os.remove(f'{group}/{date} {group1}.csv')
                read2 = pd.read_csv(f'{group}/{date} {group2}.csv')
                read2.to_excel(f'{group}/{date} {group2}.xlsx', index=None, header=True)
                os.remove(f'{group}/{date} {group2}.csv')

            msg = QMessageBox()
            msg.setWindowTitle("Successfully")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Saved successfully!!!")
            x = msg.exec_()
        except OSError:
            msg = QMessageBox()
            msg.setWindowTitle("Error files")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Don't find choosing files!")
            x = msg.exec_()

    def createFolder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. ' + directory)

    def creates(self):
        try:
            group = self.combo3.currentText()
            group1 = group[0:5]
            group2 = group[7:]
            self.createFolder(f'{group}')
            self.createFolder(f'{pic}/{group1}')
            self.createFolder(f'{pic}/{group2}')
            msg = QMessageBox()
            msg.setWindowTitle("Successfully")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Create successfully!!!")
            x = msg.exec_()
        except OSError:
            msg = QMessageBox()
            msg.setWindowTitle("Error files")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("All ready create files!")
            x = msg.exec_()

    def faceImg(self):
        group = self.combo3.currentText()
        group1 = group[0:5]
        if group1 == group:
            self.pbar.setValue(100)
        else:
            self.pbar.setValue(50)
        with open(f'{group}/{date} {group1}.csv', 'w+') as f:
            write = csv.writer(f, lineterminator='\n')
            write.writerow(['Fullname', 'Check', 'Time', 'Date'])
        path = f'{pic}/{group1}'
        mylist = os.listdir(path)
        image = []
        sfr.load_encoding_images(f'{pic}/{group1}')
        for cl in mylist:
            crm = cv2.imread(f'{path}/{cl}')
            image.append(crm)
            classN1.append(os.path.splitext(cl)[0])

    def faceImg2(self):
        group = self.combo3.currentText()
        group2 = group[7:]
        with open(f'{group}/{date} {group2}.csv', 'w+') as f:
            write = csv.writer(f, lineterminator='\n')
            write.writerow(['Fullname', 'Check', 'Time', 'Date'])
        path = f'{pic}/{group2}'
        mylist = os.listdir(path)
        image = []
        sfr.load_encoding_images(f'{pic}/{group2}')
        for cl in mylist:
            crm = cv2.imread(f'{path}/{cl}')
            image.append(crm)
            classN2.append(os.path.splitext(cl)[0])
        self.pbar.setValue(100)

    def camera(self):
        try:
            group = self.combo3.currentText()
            group1 = group[0:5]
            if group1 == group:
                self.faceImg()
            else:
                self.faceImg()
                self.faceImg2()
            cap = cv2.VideoCapture(0)
            self.timer.start(1000)
            while True:
                success, image = cap.read()
                image = cv2.putText(image,' Group: ' + group, (10, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (170,85,0), 1, cv2.LINE_AA)
                face_locations, face_names = sfr.detect_known_faces(image)
                for face_loc, name in zip(face_locations, face_names):
                    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                    cv2.putText(image, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)
                    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 255), 1)
                    if not name == 'Unknown':
                        winsound.PlaySound('detected-sound.wav', winsound.SND_FILENAME)
                        if group1 == group:
                            if self.t <= 15:
                                self.marks(name)
                            else:
                                self.apcend(name)
                        else:
                            if self.t <= 15:
                                for a in classN1:
                                    if name == a:
                                        self.marks(name)
                                for b in classN2:
                                    if name == b:
                                        self.mark(name)
                            else:
                                for a in classN1:
                                    if name == a:
                                        self.apcend(name)
                                for b in classN2:
                                    if name == b:
                                        self.apcend2(name)

                cv2.imshow('Attendance WebCam', image)
                keyCode = cv2.waitKey(1)
                if cv2.getWindowProperty('Attendance WebCam', cv2.WND_PROP_VISIBLE) < 1:
                    break
                if self.t == 30:
                    break
            cv2.destroyAllWindows()
            cap.release()
        except OSError:
            msg = QMessageBox()
            msg.setWindowTitle("Error camera")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please check for errors!")
            x = msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = Cam()
    mainWindow.show()
    sys.exit(app.exec_())
