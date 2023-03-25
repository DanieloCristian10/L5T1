import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore


def debug_trace(ui=None):
    from pdb import set_trace
    QtCore.pyqtRemoveInputHook()
    set_trace()
    # QtCore.pyqtRestoreInputHook()


class HTMLConverter(QWidget):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        super(HTMLConverter, self).__init__()
        ui_path = os.path.join(self.ROOT_DIR, 'html_converter.ui')
        loadUi(ui_path, self)
        self.browse_btn2.clicked.connect(self.browse)

        self.convert_btn.clicked.connect(self.convert)
        self.file_path = None

    def convert(self):
        print(self.path_line_edit.text())
        f = open(self.path_line_edit.text(), "r")
        htmlText=  ""
        htmlText = htmlText+ f"<h1>{f.readline()}</h1>\n"
        for line in f:
            htmlText = htmlText + f"<p>{line}</p>\n"
        self.textEdit.setText(htmlText)
    def browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self,
                                              caption='Select file',
                                              directory='',
                                              filter="Text Files (*.txt)",
                                              options=options)
        if file:
            self.file_path = file
            self.path_line_edit.setText(file)
            print(file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HTMLConverter()
    window.show()
    sys.exit(app.exec_())
