
from __future__ import division, unicode_literals, print_function, absolute_import

import sys
from PySide import QtGui, QtCore


class MainWindowWidget(QtGui.QWidget):

    def __init__(self):
        super(MainWindowWidget, self).__init__()
        self.show()

        self.load_button = QtGui.QPushButton("Load image")
        self.load_button.clicked.connect(self.load_image)

        self.lbl = QtGui.QLabel(self)

        layout_button = QtGui.QHBoxLayout()
        layout_button.addWidget(self.load_button)
        layout_button.addStretch()

        layout = QtGui.QVBoxLayout()
        layout.addLayout(layout_button)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

    def load_image(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        pixmap = QtGui.QPixmap(fname)
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.lbl.setPixmap(pixmap)


if __name__ == '__main__':

    # Initialise the PKView application
    app = QtGui.QApplication(sys.argv)
    # Pass arguments from the terminal (if any) into the main application
    ex = MainWindowWidget()
    sys.exit(app.exec_())