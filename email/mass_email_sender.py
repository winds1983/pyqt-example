# https://www.ab62.cn/article/12647.html

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 应用操作相关的库
import sys

# 邮件发送相关的库
import smtplib
from email.mime.text import MIMEText


class EmailWork(QThread):
    trigger = pyqtSignal(str)
    finished = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(EmailWork, self).__init__(parent)
        self.parent = parent
        self.working = True

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        email_subject_text = self.parent.email_subject_text.text().strip()
        recipient_text = self.parent.recipient_text.text().strip()
        current_text = self.parent.current_text.toPlainText().strip()

        print(email_subject_text)
        print(recipient_text)
        print(current_text)

        self.trigger.emit("邮件信息读取完成！")

        # 发件人邮箱
        send_email_name = '1342929047@qq.com'
        # 发件人授权码
        passwd = 'fjyjqlzxprzihcii'

        self.trigger.emit(send_email_name)
        self.trigger.emit("发件人信息初始化完成！")
        # 收件人邮箱
        msg_to = recipient_text.split(';')
        self.trigger.emit(recipient_text)
        self.trigger.emit("收件人信息初始化完成！")
        print(msg_to)
        # 设置邮件
        msg = MIMEText(current_text)
        msg['subject'] = email_subject_text
        # 设置发件人
        msg['From'] = '一匹来自北方的狼'
        # 设置收件人
        msg['To'] = ';'.join(msg_to)
        # 连接服务器
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
        self.trigger.emit("服务器连接成功！")
        # 登录邮箱
        smtp.login(send_email_name, passwd)
        self.trigger.emit("邮箱登录成功！")
        # 发送邮件
        smtp.sendmail(send_email_name, msg_to, msg.as_string())
        self.trigger.emit("邮件发送成功！")
        self.finished.emit(True)


class StmpEmail(QWidget):
    def __init__(self):
        super(StmpEmail, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle('批量邮件工具  公众号：[Python 集中营]')
        self.setWindowIcon(QIcon('邮件.ico'))
        self.setFixedSize(500, 400)

        hbox = QHBoxLayout()
        self.send_btn = QPushButton()
        self.send_btn.setText('发送')
        self.send_btn.clicked.connect(self.send_btn_click)

        self.brower = QTextBrowser()
        self.brower.setFont(QFont('宋体', 8))
        self.brower.setReadOnly(True)
        self.brower.setPlaceholderText('执行进度显示区域...')
        self.brower.ensureCursorVisible()

        hbox.addWidget(self.send_btn)

        self.email_subject_text = QLineEdit()
        self.email_subject_text.setPlaceholderText('请输入主题')

        self.recipient_text = QLineEdit()
        self.recipient_text.setPlaceholderText('请输入收件人，示例：134047@qq.com;092837@163.com')

        self.current_text = QTextEdit()
        self.current_text.setPlaceholderText('请输入邮件正文')

        self.thread_ = EmailWork(self)
        self.thread_.trigger.connect(self.update_log)
        self.thread_.finished.connect(self.finished)

        vbox = QVBoxLayout()

        vbox.addWidget(self.email_subject_text)
        vbox.addWidget(self.recipient_text)
        vbox.addWidget(self.current_text)
        vbox.addWidget(self.brower)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def update_log(self, text):
        '''
        槽函数：向文本浏览器中写入内容
        :param text:
        :return:
        '''
        cursor = self.brower.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.brower.append(text)
        self.brower.setTextCursor(cursor)
        self.brower.ensureCursorVisible()

    def finished(self, finished):
        if finished is True:
            self.send_btn.setEnabled(True)

    def send_btn_click(self):
        self.send_btn.setEnabled(False)
        self.thread_.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StmpEmail()
    main.show()
    sys.exit(app.exec_())
