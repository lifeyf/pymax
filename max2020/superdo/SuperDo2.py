'''
@File    :   stableCamera.py
@Time    :   2023/10/05 14:05:48
@Author  :   William Smith (Alias) 
@Version :   1.0
@Contact :   lifeyf@hotmail.com
@License :   Copyright @ 2022 <William Smith>
'''

from qtmax import GetQMaxMainWindow
import os
import sys
#import MaxPlus
from PySide2.QtWidgets import QDockWidget, QPushButton, QBoxLayout, QWidget
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import QColor, QPalette
from pymxs import runtime as rt

work_path = os.path.dirname(__file__)
sys.path.append(work_path)

from superdo_exportSof import sof_save_main
from superdo_stableCamera import stable_camera_main
from superdo_proxySwitch import proxy_switch_main
from superdo_transformLock import transform_lock_main
from superdo_cleanMaterial import clean_material_main


main_window = GetQMaxMainWindow()


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

	btn7 = QPushButton('Ccclip', main_widget)
	btn7.clicked.connect(ccclip_click)
	
	btn8 = QPushButton('WirColor', main_widget)
	btn8.clicked.connect(wirecolor_click)

	btn9 = QPushButton('StaCam', main_widget)
	btn9.clicked.connect(stacamera_click)

	btn10 = QPushButton('ExpoSof', main_widget)
	btn10.clicked.connect(exportsof_click)

	btn11 = QPushButton('ProxySw', main_widget)
	btn11.clicked.connect(proxyswitch_click)

	btn12 = QPushButton('TrsLock', main_widget)
	btn12.clicked.connect(transformlock_click)

	btn13 = QPushButton('ClenMat', main_widget)
	btn13.clicked.connect(cleanmaterial_click)

	box = QBoxLayout(QBoxLayout.TopToBottom)
	box.addWidget(btn1)
	box.addWidget(btn2)
	box.addWidget(btn3)
	box.addWidget(btn4)
	box.addWidget(btn5)
	box.addWidget(btn6)
	box.addWidget(btn7)
	box.addWidget(btn8)
	box.addWidget(btn9)
	box.addWidget(btn10)
	box.addWidget(btn11)
	box.addWidget(btn12)
	box.addWidget(btn13)
	
	inner = QWidget(main_widget)
	inner.setMaximumSize(50,280)
	inner.setLayout(box)
	main_widget.setWidget(inner)
	
	main_widget.dockLocationChanged.connect(lambda event:change_layout(event, box, inner))
	main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, main_widget)
	#main_widget.setFloating(True)
	main_widget.show()

def change_color_all_do():
	rt.useenvironmentmap = False
	rt.actionman.executeaction(0, "619")

def red_click(pram):
	rt.backgroundcolor = rt.red
	change_color_all_do()

def green_click(pram):
	rt.backgroundcolor = rt.green
	change_color_all_do()

def blue_click(pram):
	rt.backgroundcolor = rt.blue
	change_color_all_do()
def white_click(pram):
	rt.backgroundcolor = rt.white
	change_color_all_do()
def black_click(pram):
	rt.backgroundcolor = rt.black
	change_color_all_do()
def restore_click(pram):
	rt.backgroundcolor = rt.black
	rt.useenvironmentmap = True
	rt.actionman.executeaction(0, "617")

def ccclip_click(pram):
    currents = rt.getcurrentselection()
    for i in rt.selection:
        if rt.classof(i) == rt.targetcamera:
            i.clipmanually = not (i.clipmanually)
            print("CClip>> " + str(i.clipmanually))
    rt.clearselection()
    rt.selectmore(currents)

def wirecolor_click(pram):
	for i in rt.selection:
		a = rt.random(0, 255)
		b = rt.random(0, 255)
		c = rt.random(0, 255)
		i.wirecolor = rt.color(a, b, c)
	rt.redrawviews()

###################stable camera########################

def stacamera_click():
	stable_camera_main()

#################stablecamera end#######################

#################save sof #######################

def exportsof_click():
	sof_save_main(main_window)

#################save sof end#######################

def proxyswitch_click():
	proxy_switch_main()
	
def transformlock_click():
	transform_lock_main()

def cleanmaterial_click():
	clean_material_main()

def change_layout(pram, box, inner):
	top = QtCore.Qt.DockWidgetArea.TopDockWidgetArea
	bottom = QtCore.Qt.DockWidgetArea.BottomDockWidgetArea
	left = QtCore.Qt.DockWidgetArea.LeftDockWidgetArea
	right = QtCore.Qt.DockWidgetArea.RightDockWidgetArea
	if pram in [top, bottom]:
		box.setDirection(QBoxLayout.LeftToRight)
		inner.setMaximumSize(280,100)
	elif pram in [left, right]:
		box.setDirection(QBoxLayout.TopToBottom)
		inner.setMaximumSize(50,280)


if __name__ == "__main__":
	main()
