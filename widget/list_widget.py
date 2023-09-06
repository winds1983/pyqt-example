import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ListWidget(QListWidget):
	def clicked(self,item):
		QMessageBox.information(self, "ListWidget", "你选择了: "+item.text())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	listWidget  = ListWidget()
	listWidget.resize(300,120) 
	listWidget.addItem("Pyhon语言");
	listWidget.addItem("C语言");
	listWidget.addItem("C++语言");
	listWidget.addItem("Java语言");
	listWidget.setWindowTitle('QListwidget 例子')
	listWidget.itemClicked.connect(listWidget.clicked)
	listWidget.show() 
	sys.exit(app.exec_())

