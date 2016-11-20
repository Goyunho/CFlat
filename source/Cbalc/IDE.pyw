# modules
import os
import sys
import tempfile
# GUI
from tkinter import *


class IDE(Tk):
    def __init__(self):
        super().__init__()
        os.chdir("source/Cbalc")
        self.setUI()
        self.event()

    def setUI(self):
        # 위젯 정의
        self.tree_T_btn = Button(self, text="tree_text")
        self.tree_G_btn = Button(self, text="tree_GUI")
        self.build_btn = Button(self, text="build")
        self.source_te = Text(self)
        self.source_sb = Scrollbar(self, command=self.source_te.yview)
        self.result_te = Text(self, height=10, state=DISABLED)
        self.result_sb = Scrollbar(self, command=self.result_te.yview)

        # 위젯 위치
        self.tree_T_btn.grid(row=0, column=0, sticky='we')
        self.tree_G_btn.grid(row=0, column=1, sticky='we')
        self.build_btn.grid(row=0, column=2, sticky='we')
        self.source_te.grid(row=1, columnspan=3)
        self.source_sb.grid(row=1, column=3, sticky='nsew')
        self.result_te.grid(row=2, columnspan=3)
        self.result_sb.grid(row=2, column=3, sticky='nsew')

    # event
    def event(self) :
        self.tree_T_btn.bind("<Button-1>", self.event_tree_T)
        self.tree_G_btn.bind("<Button-1>", self.event_tree_G)
        self.build_btn.bind("<Button-1>", self.event_build)

    def event_tree_T(self, source):
        source = self.source_te.get('1.0', END)
        with open('.source.cbc', 'w') as file :
            file.write(source)
        result = os.popen("python pygrun -t Cbalc prog " + file.name).read()
        self.setResult_te(self.result_te, result)

    def event_tree_G(self, source):
        source = self.source_te.get('1.0', END)
        with open('.source.cbc', 'w') as file :
            file.write(source)
        result = os.popen("python pygrun -g -t Cbalc prog " + file.name).read()

    def event_build(self, source):
        source = self.source_te.get('1.0', END)
        with open('.source.cbc', 'w') as file :
            file.write(source)
        result = os.popen("python Cbalc.py " + file.name).read()
        self.setResult_te(self.result_te, result)

    # functions
    def setResult_te(self, result_te, text):
        result_te.configure(state="normal")
        result_te.delete('1.0', END)
        result_te.insert('end', text)
        result_te.configure(state=DISABLED)


if __name__ == '__main__':
    root = IDE()
    root.title("Cbalc IDE")
    root.mainloop()

    