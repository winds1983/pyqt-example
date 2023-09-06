# 窗口之间数据传递（通过属性来进行消息传递）
from PyQt5.QtWidgets import QDialogButtonBox, QDateTimeEdit, QDialog, QComboBox, QTableView, QAbstractItemView, \
    QHeaderView, QTableWidget, QTableWidgetItem, QMessageBox, QListWidget, QListWidgetItem, QStatusBar, QMenuBar, QMenu, \
    QAction, QLineEdit, QStyle, QFormLayout, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow, \
    QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel, QCursor, QFont, QBrush, QColor, QPainter, \
    QMouseEvent, QImage, QTransform
from PyQt5.QtCore import QStringListModel, QAbstractListModel, QModelIndex, QSize, Qt, QObject, pyqtSignal, QTimer, \
    QEvent, QDateTime, QDate

import sys


class Win(QWidget):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.resize(400, 400)

        self.btn = QPushButton("按钮", self)
        self.btn.move(50, 50)
        self.btn.setMinimumWidth(80)


        self.label = QLabel('显示信息', self)
        self.label.setMinimumWidth(420)

        self.btn.clicked.connect(self.fn)   # 按钮绑定槽函数

    # 显示子窗口传来的日期字符串或者其他数据
    def fn(self):
        # 调用静态方法，无需实例化
        date, time, res = Child_Dialog.getResult(self)
        print(date, time, res)
        # 直接实例化自定义的对话框类
        # dialog=Child_Dialog()
        # res=dialog.exec_()	# 阻塞运行，直到窗口关闭
        # date=dialog.datetime.date()
        # time=dialog.datetime.time()
        # print(res,date,time)


# 弹出框对象
class Child_Dialog(QDialog):

    def __init__(self, parent=None):
        super(Child_Dialog, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        self.label.setText("请选择日期")
        layout.addWidget(self.label)
        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)  # 点击ok，该方法默认存在
        buttons.rejected.connect(self.reject)  # 点击cancel，该方法默认存在
        layout.addWidget(buttons)

    # 该方法在父类方法中调用，直接打开了子窗体，返回值则用于向父窗体数据的传递
    @staticmethod
    def getResult(self, parent=None):
        dialog = Child_Dialog(parent)
        result = dialog.exec_()
        d = dialog.datetime.dateTime()
        return (d.date(), d.time(), result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())

