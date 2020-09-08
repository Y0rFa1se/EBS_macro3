import sys
import time
import webbrowser
import math

import pyautogui

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.QtCore import *

gui = uic.loadUiType("gui/gui.ui")[0]
log = open("properties/logs.ini", "a")

class Window(QMainWindow, gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(812, 590)
        self.setWindowTitle("EBS Macro")
        self.setWindowIcon(QIcon("gui/icon.ico"))
        self.pbar.setValue(0)

        log.write("program started /// " + str(time.ctime()) + "\n")
        print("program started")
        self.logs.append("program started")

        self.Help.clicked.connect(self.showHelp)
        self.Lectures.clicked.connect(self.lectures)
        self.Append.clicked.connect(self.Append_)
        self.Save.clicked.connect(self.save)
        self.Run.clicked.connect(self.run)
        self.Check.clicked.connect(self.check)
        self.LogIn.clicked.connect(self.login)
        self.Example.clicked.connect(self.example)

    def closeEvent(self, QCloseEvent):
        log.write("close event /// " + str(time.ctime()) + "\n")
        print("close event")
        self.logs.append("close event")
        reply = QMessageBox.question(self, 'ㄹㅇ?', 'ㄹㅇ 종료하시겠습니까???',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
            log.write("closed /// " + str(time.ctime()) + "\n")
            print("closed")
        else:
            QCloseEvent.ignore()

    def showHelp(self):
        log.write("show help /// " + str(time.ctime()) + "\n")
        print("show help")
        self.logs.append("show help")
        with open("properties/help.ini", "r") as he:
            self.txt.setPlainText(he.read())

    def lectures(self):
        log.write("show lectures /// " + str(time.ctime()) + "\n")
        print("loading lectures...")
        self.logs.append("loading lectures...")
        with open("properties/lectures.ini", "r") as lec:
            lecs = lec.read()
            if lecs:
                self.txt.setPlainText(lecs)
                log.write("show lectures_ /// " + str(time.ctime()) + "\n")
                print("show lectures")
                self.logs.append("show lectures")
                QMessageBox.information(self, "ㅊㅊ", "강의 로드됨")
            else:
                self.txt.setPlainText(lecs)
                log.write("saved letures does not exist /// " + str(time.ctime()) + "\n")
                print("saved letures does not exist")
                self.logs.append("saved letures does not exist")
                QMessageBox.information(self, "??", "저장된 강의 없음")

    def Append_(self):
        log.write("append lectures /// " + str(time.ctime()) + "\n")
        print("loading lectures...")
        self.logs.append("loading lectures...")
        txtargs = self.txt.toPlainText()
        with open("properties/lectures.ini", "a") as lec:
            if txtargs:
                lec.write("\n" + txtargs)
                print("successfully added")
                self.logs.append("successfully added")
                log.write("successfully added /// " + str(time.ctime()) + "\n")
                QMessageBox.information(self, "ㅊㅊ", "추가됨")
            else:
                print("argument does not exist")
                self.logs.append("argument does not exist")
                log.write("argument does not exist /// " + str(time.ctime()) + "\n")
                QMessageBox.information(self, "뭐하노", "뭐하노")

    def save(self):
        log.write("save lectures /// " + str(time.ctime()) + "\n")
        print("loading lectures...")
        self.logs.append("loading lectures...")
        txtargs = self.txt.toPlainText()
        with open("properties/lectures.ini", "w") as lec:
            lec.write(txtargs)
            print("successfully saved")
            self.logs.append("successfully saved")
            log.write("successfully saved /// " + str(time.ctime()) + "\n")
            QMessageBox.information(self, "ㅊㅊ", "저장됨")

    def example(self):
        log.write("show example /// " + str(time.ctime()) + "\n")
        print("loading example...")
        self.logs.append("loading example...")
        with open("properties/example.ini", "r") as ex:
            self.txt.setPlainText(ex.read())
            log.write("show example_ /// " + str(time.ctime()) + "\n")
            print("show example")
            self.logs.append("show example")

    def run(self):
        def tick(lrt):
            loop = QEventLoop()
            QTimer.singleShot(lrt * 1000, loop.quit)
            loop.exec_()

        log.write("resetting /// " + str(time.ctime()) + "\n")
        print("resetting...")
        self.logs.append("resetting...")

        if not self.Youtube.isChecked():
            youtube = True
        else:
            youtube = False
        self.time = 0
        self.pbar.setValue(0)
        links = []
        lrts = []
        sum = 0
        now = 0

        log.write("reset /// " + str(time.ctime()) + "\n")
        print("reset")
        self.logs.append("reset")

        log.write("loading lectures /// " + str(time.ctime()) + "\n")
        print("loading lectures...")
        self.logs.append("loading lectures...")

        with open("properties/lectures.ini", "r") as lec:
            while True:
                lecs = lec.readline().replace("\n", "")
                if (lecs == ""):
                    break
                links.append(lecs)
                lrntime = int(lec.readline().replace("\n", ""))
                lrnt = (lrntime * 60) * 0.7
                sum += lrntime * 0.7
                lrts.append(lrnt)

        log.write("loaded lectures /// " + str(time.ctime()) + "\n")
        print("loaded lectures")
        self.logs.append("loaded lectures")

        log.write("show learntime /// " + str(time.ctime()) + "\n")
        print("show learntime")
        self.logs.append("show learntime")

        self.txt.setPlainText("total learntime : " + str(sum) + "minutes")
        self.txt.append("started at : " + str(time.ctime()))
        self.txt.append("total lectures : " + str(len(links)))

        for i in range(len(links)):
            log.write(links[i] + " /// " + str(time.ctime()) + "\n")
            print("open browser")
            self.logs.append("open browser")

            webbrowser.open(links[i])
            tick(5)

            log.write("start scaning /// " + str(time.ctime()) + "\n")
            print("start scaning...")
            self.logs.append("start scaning...")
            ifFound = False

            for j in range(10, 7, -1):
                log.write("accuracy : " + str(j * 10) + "/// " + str(time.ctime()) + "\n")
                print("accuracy : " + str(j * 10))
                self.logs.append("accuracy : " + str(j * 10))
                ploc = pyautogui.locateOnScreen("Images/click.PNG", confidence=(j * 0.1))

                if (ploc != None):
                    log.write("found object /// " + str(time.ctime()) + "\n")
                    print("found object")
                    self.logs.append("found object")
                    ifFound = True
                    break

            if (ifFound == False):
                log.write("youtube /// " + str(time.ctime()) + "\n")
                print("youtube")
                self.logs.append("youtube")

                if youtube:
                    x_, y_ = pyautogui.size()
                    x_ = x_ // 2
                    y_ = y_ // 2
                    pyautogui.click(x = x_, y = y_)

            else:
                log.write("play /// " + str(time.ctime()) + "\n")
                print("play")
                self.logs.append("play")
                pyautogui.click(pyautogui.center(ploc))

            for k in range(math.ceil(lrts[i])):
                tick(1)
                now += 1
                self.time = int(((now / 60) / sum) * 100)
                self.pbar.setValue(self.time)
            pyautogui.hotkey("ctrl", "w")
            log.write("end /// " + str(time.ctime()) + "\n")
            print("end")
            self.logs.append("end")
            if (i == (len(links) - 1)):
                self.pbar.setValue(100)
                log.write("finished /// " + str(time.ctime()) + "\n")
                print("finished")
                self.logs.append("finished")

        QMessageBox.information(self, "ㅂㅂ", "종료됨")

    def check(self):
        log.write("start scaning /// " + str(time.ctime()) + "\n")
        print("start scaning...")
        self.logs.append("start scaning...")
        ifFound = False
        for i in range(10, 7, -1):
            log.write("accuracy : " + str(i * 10) + "/// " + str(time.ctime()) + "\n")
            print("accuracy : " + str(i * 10))
            self.logs.append("accuracy : " + str(i * 10))
            ploc = pyautogui.locateOnScreen("Images/click.PNG", confidence=(i * 0.1))
            if (ploc != None):
                log.write("found object /// " + str(time.ctime()) + "\n")
                print("found object")
                self.logs.append("found object")
                QMessageBox.information(self, "ㅊㅊ", "오브젝트 발견함")
                ifFound = True
                break
        if (ifFound == False):
            log.write("cannot find object /// " + str(time.ctime()) + "\n")
            print("cannot find object")
            self.logs.append("cannot find object")
            QMessageBox.warning(self, "뭐노", "오브젝트 찾지못함")
            
        if self.Youtube.isChecked():
            QMessageBox.information(self, "!", "유튜브 자동재생 버튼 활성화")
        else:
            QMessageBox.information(self, "!", "유튜브 자동재생 버튼 비활성화")

    def login(self):
        log.write("open webbrowser /// " + str(time.ctime()) + "\n")
        print("open webbrowser")
        self.logs.append("open webbrowser")
        webbrowser.open(url = "https://oc.ebssw.kr/")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    newWindow = Window()
    newWindow.show()
    app.exec_()