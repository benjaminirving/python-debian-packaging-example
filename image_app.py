
from __future__ import division, unicode_literals, print_function, absolute_import

from PySide import QtGui, QtCore
import sys
import platform

op_sys = platform.system()
if op_sys == 'Darwin':
    from Foundation import NSURL


class MainWindowWidget(QtGui.QWidget):

    def __init__(self):
        super(MainWindowWidget, self).__init__()

        self.load_button = QtGui.QPushButton("Load image")
        self.load_button.clicked.connect(self.load_image_but)

        self.lbl = QtGui.QLabel(self)

        layout_button = QtGui.QHBoxLayout()
        layout_button.addWidget(self.load_button)
        layout_button.addStretch()

        layout = QtGui.QVBoxLayout()
        layout.addLayout(layout_button)
        layout.addWidget(self.lbl)

        self.setLayout(layout)
        self.setAcceptDrops(True)
        self.show()

    def load_image_but(self):
        self.fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.load_image()

    def load_image(self):
        pixmap = QtGui.QPixmap(self.fname)
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.lbl.setPixmap(pixmap)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        """
        Drop files directly onto the widget

        File locations are stored in fname
        :param e:
        :return:
        """
        if e.mimeData().hasUrls:
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            for url in e.mimeData().urls():
                if op_sys == 'Darwin':
                    fname = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
                else:
                    fname = str(url.toLocalFile())

            self.fname = fname
            self.load_image()
        else:
            e.ignore()


if __name__ == '__main__':
    # Initialise the PKView application
    app = QtGui.QApplication(sys.argv)
    # Pass arguments from the terminal (if any) into the main application
    ex = MainWindowWidget()
    sys.exit(app.exec_())