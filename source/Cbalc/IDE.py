# 
import os
import sys

"""
# for GUI
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import 

class CbalcIDE(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 
    
    # 위젯별 설정
    def initUI(self):
        # 위젯
        build_btn = QPushButton('Build', self)
        tree_btn = QPushButton('View tree', self)
        source_te = QTextEdit(self)

        ### /self 하위 버튼
        source_te.move(0, 30)

        ## / 최상위 윈도우
        self.resize(800, 480)
        self.center()
        self.setWindowTitle('Cbalc IDE')
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cbalc = CbalcIDE()
    #실행하고 끝나면 종료
    sys.exit(app.exec_())
"""

from tkinter import *

class IDE(Tk):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        tree_btn = Button(self, text="tree")
        build_btn = Button(self, text="build")
        source_te = Text(self)
        result_te = Text(self, height=10)

        tree_btn.grid(row=0, column=0, sticky='we')
        build_btn.grid(row=0, column=1, sticky='we')
        source_te.grid(row=1, columnspan=2)
        result_te.grid(row=2, columnspan=2)


if __name__ == '__main__':
    root = IDE()
    root.title("Cbalc IDE")
    root.mainloop()

    