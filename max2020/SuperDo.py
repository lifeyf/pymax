#from qtmax import GetQMaxMainWindow
import MaxPlus
from PySide2.QtWidgets import QMainWindow, QDockWidget, QToolButton, QToolBar, QAction, QPushButton, QBoxLayout, QWidget
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import QColor, QPalette


main_window = MaxPlus.GetQMaxMainWindow()


def main():
	main_widget = QDockWidget(main_window)

	main_widget.setObjectName("SuperDO")
	main_widget.setWindowTitle("SuperDO")
	main_widget.setFloating(False)

	btn1 = QPushButton('Red', main_widget)
	palette = QPalette()
	palette.setColor(QPalette.Button, QColor(255,0,0))
	btn1.setPalette(palette)
	btn1.clicked.connect(red_click)

	btn2 = QPushButton('Green', main_widget)
	palette = QPalette()
	palette.setColor(QPalette.Button, QColor(0,255,0))
	btn2.setPalette(palette)
	btn2.clicked.connect(green_click)

	btn3 = QPushButton('Blue', main_widget)
	palette = QPalette()
	palette.setColor(QPalette.Button, QColor(0,0,255))
	btn3.setPalette(palette)
	btn3.clicked.connect(blue_click)
	
	btn4 = QPushButton('White', main_widget)
	palette = QPalette()
	palette.setColor(QPalette.Button, QColor(255,255,255))
	btn4.setPalette(palette)
	btn4.clicked.connect(white_click)

	btn5 = QPushButton('Black', main_widget)
	palette = QPalette()
	palette.setColor(QPalette.Button, QColor(0,0,0))
	btn5.setPalette(palette)
	btn5.clicked.connect(black_click)
	
	btn6 = QPushButton('Restore', main_widget)
	btn6.clicked.connect(restore_click)

	box = QBoxLayout(QBoxLayout.TopToBottom)
	box.addWidget(btn1)
	box.addWidget(btn2)
	box.addWidget(btn3)
	box.addWidget(btn4)
	box.addWidget(btn5)
	box.addWidget(btn6)
	
	inner = QWidget(main_widget)
	inner.setMaximumSize(60,150)
	inner.setLayout(box)
	main_widget.setWidget(inner)
	
	main_widget.dockLocationChanged.connect(lambda event:change_layout(event, box, inner))
	main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, main_widget)
	main_widget.setFloating(True)
	main_widget.show()
	
def red_click(pram):
	print(pram)
def green_click(pram):
	print(pram)
def blue_click(pram):
	print(pram)
def white_click(pram):
	print(pram)
def black_click(pram):
	print(pram)
def restore_click(pram):
	print("restore")
	
def change_layout(pram, box, inner):
	top = QtCore.Qt.DockWidgetArea.TopDockWidgetArea
	bottom = QtCore.Qt.DockWidgetArea.BottomDockWidgetArea
	left = QtCore.Qt.DockWidgetArea.LeftDockWidgetArea
	right = QtCore.Qt.DockWidgetArea.RightDockWidgetArea
	if pram in [top, bottom]:
		box.setDirection(QBoxLayout.LeftToRight)
		inner.setMaximumSize(150,100)
	elif pram in [left, right]:
		box.setDirection(QBoxLayout.TopToBottom)
		inner.setMaximumSize(50,150)


if __name__ == "__main__":
	main()
