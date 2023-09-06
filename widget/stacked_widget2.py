# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QWidget, QStackedWidget, QHBoxLayout, QGridLayout, \
    QPushButton


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        # 创建左侧按键元件
        self.btn1 = QPushButton("按钮1")
        self.btn2 = QPushButton("按钮2")
        self.btn3 = QPushButton("按钮3")
        # 设置按键点击属性
        self.btn1.clicked.connect(self.display)
        self.btn2.clicked.connect(self.display)
        self.btn3.clicked.connect(self.display)
        # 创建左侧布局
        self.left_layout = QGridLayout()
        self.left_layout.addWidget(self.btn1)
        self.left_layout.addWidget(self.btn2)
        self.left_layout.addWidget(self.btn3)
        # 创建左侧组件
        self.left_widget = QWidget()
        self.left_widget.setLayout(self.left_layout)
        # 创建右侧分页
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        # 创建右侧分页各个组件
        self.initStack1()
        self.initStack2()
        self.initStack3()
        # 创建整体页组件，并将三个分页添加到主页上
        self.Stack = QStackedWidget()
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        # 创建主组件布局
        self.main_layout = QHBoxLayout()
        # 向主组件布局中添加左右两个整体组件
        self.main_layout.addWidget(self.left_widget)
        self.main_layout.addWidget(self.Stack)
        # 设置主组件的布局为创建的主布局
        self.setLayout(self.main_layout)

    def initStack1(self):
        layout = QHBoxLayout()
        list1 = QListWidget()
        list1.insertItem(0, "第一页")
        layout.addWidget(list1)

        self.stack1.setLayout(layout)

    def initStack2(self):
        layout = QHBoxLayout()
        list1 = QListWidget()
        list1.insertItem(0, "第二页")
        layout.addWidget(list1)

        self.stack2.setLayout(layout)

    def initStack3(self):
        layout = QHBoxLayout()
        list1 = QListWidget()
        list1.insertItem(0, "第三页")
        layout.addWidget(list1)

        self.stack3.setLayout(layout)

    def display(self):
        sender = self.sender()
        if sender.text() == "按钮1":
            self.Stack.setCurrentIndex(0)
        elif sender.text() == "按钮2":
            self.Stack.setCurrentIndex(1)
        elif sender.text() == "按钮3":
            self.Stack.setCurrentIndex(2)


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

