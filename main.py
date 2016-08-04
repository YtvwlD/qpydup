#! /usr/bin/env python3
#    qpydup - a front-end for Duplicity made with Python and Qt
#    Copyright (C) 2016  Niklas Sombert
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PySide2.QtWidgets import QApplication, QMainWindow
from sys import argv

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)

app = QApplication(argv)
win = MainWindow()
win.show()
app.exec_()
