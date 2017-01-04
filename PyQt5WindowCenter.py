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
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget

class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.resize(250,150)
		self.center()

		self.setWindowTitle('Center')
		self.show()

	def center(self):
		qr = self.frameGeometry() # Geometry of the window
		cp = QDesktopWidget().availableGeometry().center() # Geometry of the desktop
		qr.moveCenter(cp) # set the "qr" center to desktop center
		self.move(qr.topLeft()) # move the window to "qr" center


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())



