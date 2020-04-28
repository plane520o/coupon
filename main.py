from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView, QPushButton
import newfaquan
from PyQt5 import QtCore, QtGui, QtWidgets
import base64
import requests
import urllib.parse
from urllib.parse import quote
import cv2
import time
import sys
import datetime


session = requests.session()
e = time.strftime('%Y-%m-%d')
nowtime = datetime.datetime.strptime(e, '%Y-%m-%d')
# class CommonHelper:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def readQss(style):
#         with open(style, 'r') as f:
#             return f.read()


def slot_init():   #函数槽
    timer_camera.timeout.connect(showcamera)
    ui.pushButton.clicked.connect(takePhoto)
    ui.pushButton_2.clicked.connect(faquan)

def showcamera(): #展示摄像头画面到ui.label
    global image
    flag, image = cap.read()
    #image = cv2.flip(image, 1)
    show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
    ui.label.setPixmap(QtGui.QPixmap.fromImage(showImage))
    ui.label.setScaledContents(True)

def takePhoto(): #保存摄像头画面并识别图片

    if timer_camera.isActive() != False:
        cv2.imwrite('pic_'+'.jpg',image)
        time.sleep(1)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'charset': "utf-8"
        }

        recognise_api_url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise"
        access_token = "24.298c7a432c3a1d856f74419e86de9ff0.2592000.1586822706.282335-18818243"
        templateSign = "1f7c71f7c0ac08871e323f82f17e7550"
        classifierId = "1"

        image_path = 'pic_.jpg'


        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_b64 = base64.b64encode(image_data).decode().replace("\r", "")
        recognise_bodys = "access_token=" + access_token + "&templateSign=" + templateSign + \
                          "&image=" + quote(image_b64.encode("utf8"))
        classifier_bodys = "access_token=" + access_token + "&classifierId=" + classifierId + \
                           "&image=" + quote(image_b64.encode("utf8"))
        response = requests.post(recognise_api_url, data=classifier_bodys, headers=headers)
        jsdata = response.json()
        try:
            data = jsdata['data']['ret']
            for key in data:
                ke = key['word_name']
                value = key['word']
                info = ke + ':' + value

                print(info)
            paytimevalue = jsdata['data']['ret'][0]['word']
            compyvalue = jsdata['data']['ret'][1]['word']
            payordervalue = jsdata['data']['ret'][2]['word']
            moneyvalue = jsdata['data']['ret'][3]['word']

            cutpaytime = paytimevalue[:10]
            datatimepaytime = datetime.datetime.strptime(cutpaytime, '%Y-%m-%d')
            orderlist = []
        except Exception:

            ui.label_2.setText('请重新调整小票位置然后点击识别')

        else:
            with open('order.txt', 'r') as f:
                for i in f:
                    a = i[:-1]
                    orderlist.append(a)
            if '-' in moneyvalue:
                if '沃' or '尔' or '玛' in compyvalue:
                    realmonyvalue = moneyvalue.replace('-', '')
                    flomony = float(realmonyvalue)
                    if datatimepaytime == nowtime:
                        if flomony >= 50:
                            if payordervalue not in orderlist:
                                ui.pushButton.setEnabled(True)
                                ui.label_2.setText('请输入车牌然后点领取优惠券')
                                ui.lineEdit.setFocus()

                            else:
                                ui.label_2.setText('您已经领取过了')

                        else:
                            ui.label_2.setText('消费大于50才能领取优惠券哦')
                    else:

                        ui.label_2.setText('仅限今天的小票领取优惠券哦')
            elif '-' not in moneyvalue:
                if '沃' or '尔' or '玛' in compyvalue:
                    if datatimepaytime == nowtime:
                        flomny = float(moneyvalue)
                        if flomny >= 50:
                            if payordervalue not in orderlist:
                                ui.pushButton.setEnabled(True)
                                ui.label_2.setText('请输入车牌然后点领取优惠券')
                                ui.lineEdit.setFocus()

                            else:
                                ui.label_2.setText('您已经领取过了')

                        else:
                            ui.label_2.setText('消费大于50才能领取优惠券哦')
                    else:

                        ui.label_2.setText('仅限今天的小票领取优惠券哦')

            with open('order.txt', 'a') as f:
                f.writelines(payordervalue + '\n')


    else:
        if timer_camera.isActive() == False:
            flag = cap.open(CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(
                     u"Warning", u"请检测相机与电脑是否连接正确",
                    buttons=QtWidgets.QMessageBox.Ok,
                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                timer_camera.start(30)

def faquan(): #沃尔玛发券函数
    carno = ui.lineEdit.text()
    url = '*'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    data = {
        'userName': '1001',
        'userPass': '1234'
    }
    session.post(url, headers=headers, data=data)
    utf = urllib.parse.quote(ui.comboBox.currentText())
    url_1 = 'http://www.wsgdgw.com:8080/api/Coupon/coupon-distribute?'
    data1 = 'ts=1585815211&storeId=15&carNo=' + utf + '-' + carno
    realurl = url_1 + data1
    session.get(realurl, headers=headers)
    ui.label_2.setText(ui.comboBox.currentText()+carno+'领取成功')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # styleFile = 'blue.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # MainWindow.setStyleSheet(qssStyle)

    ui = newfaquan.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #####初始化摄像头
    timer_camera = QtCore.QTimer()
    cap = cv2.VideoCapture()
    CAM_NUM = 0
    if timer_camera.isActive() == False:
        flag = cap.open(CAM_NUM)
        cap.set(3, 1920)
        cap.set(4, 1080)
        if flag == False:
            msg = QtWidgets.QMessageBox.warning(
                u"Warning", u"请检测相机与电脑是否连接正确",
                buttons=QtWidgets.QMessageBox.Ok,
                defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            timer_camera.start(30)
    #####
    #MainWindow.setWindowState(Qt.WindowMaximized) #窗口最大化


    #MainWindow.showFullScreen() #窗口全屏
    ui.label_2.setAlignment(Qt.AlignCenter)
    slot_init()
    ui.pushButton_2.setEnabled(False)
    sys.exit(app.exec_())