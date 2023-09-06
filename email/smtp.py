# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMTP.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#
# http://www.noobyard.com/article/p-mulsvusb-bs.html


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 842)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(310, 300, 81, 18))
        self.label_title.setObjectName("label_title")
        self.textEdit_title = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_title.setGeometry(QtCore.QRect(410, 290, 351, 41))
        self.textEdit_title.setObjectName("textEdit_title")
        self.label_passage = QtWidgets.QLabel(self.centralwidget)
        self.label_passage.setGeometry(QtCore.QRect(60, 350, 81, 18))
        self.label_passage.setObjectName("label_passage")
        self.textEdit_passage = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_passage.setGeometry(QtCore.QRect(60, 380, 971, 361))
        self.textEdit_passage.setObjectName("textEdit_passage")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(510, 750, 112, 34))
        self.button_send.setObjectName("button_send")
        self.button_send.clicked.connect(self.send_email)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 40, 271, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_smtpserver = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_smtpserver.setObjectName("textEdit_smtpserver")
        self.gridLayout.addWidget(self.textEdit_smtpserver, 0, 2, 1, 1)
        self.textEdit_port = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_port.setObjectName("textEdit_port")
        self.gridLayout.addWidget(self.textEdit_port, 1, 2, 1, 1)
        self.label_port = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_port.setObjectName("label_port")
        self.gridLayout.addWidget(self.label_port, 1, 0, 1, 1)
        self.label_smtpserver = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_smtpserver.setObjectName("label_smtpserver")
        self.gridLayout.addWidget(self.label_smtpserver, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 150, 531, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_receivernickname = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_receivernickname.setObjectName("label_receivernickname")
        self.gridLayout_2.addWidget(self.label_receivernickname, 2, 0, 1, 1)
        self.label_sender = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_sender.setObjectName("label_sender")
        self.gridLayout_2.addWidget(self.label_sender, 0, 0, 1, 1)
        self.label_receiver = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_receiver.setObjectName("label_receiver")
        self.gridLayout_2.addWidget(self.label_receiver, 1, 0, 1, 1)
        self.textEdit_receiver = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_receiver.setObjectName("textEdit_receiver")
        self.gridLayout_2.addWidget(self.textEdit_receiver, 1, 2, 1, 1)
        self.textEdit_sender = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_sender.setObjectName("textEdit_sender")
        self.gridLayout_2.addWidget(self.textEdit_sender, 0, 2, 1, 1)
        self.textEdit_receivernickname = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_receivernickname.setObjectName("textEdit_receivernickname")
        self.gridLayout_2.addWidget(self.textEdit_receivernickname, 2, 2, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(500, 40, 531, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.smtp_username = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.smtp_username.setObjectName("smtp_username")
        self.gridLayout_3.addWidget(self.smtp_username, 0, 0, 1, 1)
        self.textEdit_username = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_username.setObjectName("textEdit_username")
        self.gridLayout_3.addWidget(self.textEdit_username, 0, 1, 1, 1)
        self.textEdit_pwd = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_pwd.setObjectName("textEdit_pwd")
        self.gridLayout_3.addWidget(self.textEdit_pwd, 1, 1, 1, 1)
        self.label_pwd = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_pwd.setObjectName("label_pwd")
        self.gridLayout_3.addWidget(self.label_pwd, 1, 0, 1, 1)
        self.button_upload = QtWidgets.QPushButton(self.centralwidget)
        self.button_upload.setGeometry(QtCore.QRect(640, 180, 51, 61))
        self.button_upload.setObjectName("button_upload")
        self.button_upload.clicked.connect(self.upload_file)

        # self.listView = QtWidgets.QListView(self.centralwidget)
        # self.listView.setGeometry(QtCore.QRect(700, 168, 331, 101))
        # self.listView.setObjectName("listView")
        self.file_list = QtWidgets.QTextEdit(self.centralwidget)
        self.file_list.setEnabled(False)
        self.file_list.setGeometry(QtCore.QRect(700, 180, 331, 101))
        self.file_list.setObjectName("file_list")

        self.checkBox_SSL = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_SSL.setGeometry(QtCore.QRect(360, 70, 105, 22))
        self.checkBox_SSL.setObjectName("checkBox_SSL")

        self.label_list = QtWidgets.QLabel(self.centralwidget)
        self.label_list.setGeometry(QtCore.QRect(700, 150, 81, 18))
        self.label_list.setObjectName("label_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SMTP邮件发送"))
        self.label_title.setText(_translate("MainWindow", "标题"))
        self.label_passage.setText(_translate("MainWindow", "正文"))
        self.button_send.setText(_translate("MainWindow", "发送"))
        self.label_port.setText(_translate("MainWindow", "端口号"))
        self.label_smtpserver.setText(_translate("MainWindow", "smtp服务器"))
        self.label_sender.setText(_translate("MainWindow", "发件人"))
        self.label_receiver.setText(_translate("MainWindow", "收件人"))
        self.smtp_username.setText(_translate("MainWindow", "用户名"))
        self.label_pwd.setText(_translate("MainWindow", "受权码/密码"))
        self.button_upload.setText(_translate("MainWindow", "上传\n"
                                                           "文件"))
        self.label_list.setText(_translate("MainWindow", "附件列表"))
        self.label_receivernickname.setText(_translate("MainWindow", "收件人昵称"))
        self.checkBox_SSL.setText(_translate("MainWindow", "使用SSL"))

    message = MIMEMultipart()
    def send_email(self):
        my_sender = self.textEdit_username.toPlainText()  # 发件人邮箱帐号
        my_pass = self.textEdit_pwd.toPlainText()  # 发件人邮箱密码
        my_user = self.textEdit_receiver.toPlainText()  # 收件人邮箱帐号，我这边发送给本身
        sender_kickname = self.textEdit_sender.toPlainText()  # 发件人邮箱
        title = self.textEdit_title.toPlainText()
        passage = self.textEdit_passage.toPlainText()
        SMTP_server = self.textEdit_smtpserver.toPlainText()
        port = self.textEdit_port.toPlainText()
        ret = True
        try:

            self.message['From'] = formataddr([sender_kickname, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱帐号
            self.message['To'] = formataddr([self.textEdit_receivernickname.toPlainText(), my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱帐号
            self.message['Subject'] = title  # 邮件的主题，也能够说是标题

            self.message.attach(MIMEText(passage, 'plain', 'utf-8'))
            if(self.checkBox_SSL.checkState()==0):
                server = smtplib.SMTP(SMTP_server, port)
            else:
                server = smtplib.SMTP_SSL(SMTP_server, port)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱帐号、邮箱密码
            server.sendmail(my_sender, [my_user, ], self.message.as_string())  # 括号中对应的是发件人邮箱帐号、收件人邮箱帐号、发送邮件
            server.quit()  # 关闭链接
        except Exception:  # 若是 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        if ret:
            print("邮件发送成功")
            self.message = MIMEMultipart() #清空邮件内容
        else:
            print("邮件发送失败")

    def upload_file(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'All Types(*.*)')
        if(('', '')!=openfile_name):
            import os
            attach_file = MIMEText(open(openfile_name[0], 'rb').read(), 'base64', 'utf-8')
            attach_file["Content-Type"] = 'application/octet-stream'
            # 这里的filename能够任意写，写什么名字，邮件中显示什么名字
            filename=os.path.basename(openfile_name[0])
            attach_file["Content-Disposition"] = 'attachment; filename=\"'+filename+'\"'
            self.message.attach(attach_file)
            # self.listView.addAction(filename)
            files=self.file_list.toPlainText()
            self.file_list.setText(files+"\n"+filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())