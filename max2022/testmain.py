import os

print(os.getcwd())

import funs
A = funs.Glass('black')
A.sayname()
print(11111111111)

from PySide2.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from qtmax import GetQMaxMainWindow

class PyMaxDialog(QDialog):
    """
    Custom dialog attached to the 3ds Max main window
    Message label and action push button to create a cylinder in the 3ds Max scene graph
    """
    def __init__(self, parent=None):
        super(PyMaxDialog, self).__init__(parent)
        self.setWindowTitle('Pyside2 Qt Window')
        self.init_ui()

    def init_ui(self):
        """ Prepare Qt UI layout for custom dialog """
        main_layout = QVBoxLayout()
        label = QLabel("Click button to create a cylinder in the scene")
        main_layout.addWidget(label)

        cylinder_btn = QPushButton("Cylinder")
        main_layout.addWidget(cylinder_btn)

        self.setLayout(main_layout)
        self.resize(250, 100)



B_box = PyMaxDialog()
B_box.show()