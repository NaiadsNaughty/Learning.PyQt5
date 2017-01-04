#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		self.setGeometry(300,300,300,220)
		self.setWindowTitle('Quit Button')
		self.show()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message',
			"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())



