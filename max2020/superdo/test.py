from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
import MaxPlus

main_window = MaxPlus.GetQMaxMainWindow()
def message():
    message = QMessageBox()
    text = "Export Succeed!, file at:\n path to file"
    message.information(main_window, "title", text)
message()
