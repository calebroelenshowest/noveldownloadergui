from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot as register
from pubsub.pub import sendMessage, subscribe
import gui.Listeners as AppList
import sys
import os
import subprocess


class GUI(QtWidgets.QMainWindow):

    def __init__(self):
        # Super
        super().__init__()
        self.setWindowTitle("NovelAPI GUI")
        self.setObjectName("Main")
        self.setEnabled(True)
        self.size = (790, 570)
        self.resize(*self.size)
        self.setMinimumSize(*self.size)
        self.setMaximumSize(*self.size)

        self.main_panel = QtWidgets.QWidget(self)
        self.main_panel.setMouseTracking(False)
        self.main_panel.setObjectName("main_panel")

        self.main_panel_layout_box_h = QtWidgets.QWidget(self.main_panel)
        self.main_panel_layout_box_h.setGeometry(QtCore.QRect(9, 8, 771, 551))
        self.main_panel_layout_box_h.setObjectName("main_panel_layout_box_h")

        self.left_layout_box = QtWidgets.QHBoxLayout(self.main_panel_layout_box_h)
        self.left_layout_box.setContentsMargins(0, 0, 0, 0)
        self.left_layout_box.setObjectName("left_layout_box")

        self.tabs = QtWidgets.QTabWidget(self.main_panel_layout_box_h)
        self.tabs.setObjectName("tabs")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")

        self.vertical_box_tab_info = QtWidgets.QWidget(self.tab_info)
        self.vertical_box_tab_info.setGeometry(QtCore.QRect(9, 9, 351, 501))
        self.vertical_box_tab_info.setObjectName("vertical_box_tab_info")

        self.tab_info_box = QtWidgets.QVBoxLayout(self.vertical_box_tab_info)
        self.tab_info_box.setContentsMargins(0, 0, 0, 0)
        self.tab_info_box.setObjectName("tab_info_box")

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_pixmap = QtGui.QPixmap('img/empty.jpg')
        self.image_label.setPixmap(self.image_pixmap)
        self.tab_info_box.addWidget(self.image_label)

        self.title_box = QtWidgets.QHBoxLayout()
        self.title_box.setObjectName("title_box")

        self.title_label = QtWidgets.QLabel(self.vertical_box_tab_info)
        self.title_label.setObjectName("title_label")
        self.title_box.addWidget(self.title_label)

        self.title_value = QtWidgets.QLabel(self.vertical_box_tab_info)
        self.title_value.setObjectName("title_value")
        self.title_box.addWidget(self.title_value)

        self.tab_info_box.addLayout(self.title_box)
        self.chapter_box = QtWidgets.QHBoxLayout()
        self.chapter_box.setObjectName("chapter_box")

        self.chapter_label = QtWidgets.QLabel(self.vertical_box_tab_info)
        self.chapter_label.setObjectName("chapter_label")
        self.chapter_box.addWidget(self.chapter_label)

        self.chapter_value = QtWidgets.QLabel(self.vertical_box_tab_info)
        self.chapter_value.setObjectName("chapter_value")
        self.chapter_box.addWidget(self.chapter_value)
        self.tab_info_box.addLayout(self.chapter_box)
        self.tabs.addTab(self.tab_info, "")

        self.tab_chapters = QtWidgets.QWidget()
        self.tab_chapters.setObjectName("tab_chapters")
        self.chapter_list = QtWidgets.QListView(self.tab_chapters)
        self.chapter_list.setGeometry(QtCore.QRect(5, 10, 361, 501))
        self.chapter_list.setObjectName("chapter_list")
        self.chapter_list.setModel(QtGui.QStandardItemModel())
        self.tabs.addTab(self.tab_chapters, "")

        self.left_layout_box.addWidget(self.tabs)
        self.left_right_seperator = QtWidgets.QFrame(self.main_panel_layout_box_h)
        self.left_right_seperator.setFrameShape(QtWidgets.QFrame.VLine)
        self.left_right_seperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.left_right_seperator.setObjectName("left_right_seperator")
        self.left_layout_box.addWidget(self.left_right_seperator)
        self.right_layout_box = QtWidgets.QVBoxLayout()
        self.right_layout_box.setObjectName("right_layout_box")
        self.urlbox = QtWidgets.QHBoxLayout()
        self.urlbox.setObjectName("urlbox")
        self.url_label = QtWidgets.QLabel(self.main_panel_layout_box_h)
        self.url_label.setObjectName("url_label")
        self.urlbox.addWidget(self.url_label)
        self.url_input_box = QtWidgets.QLineEdit(self.main_panel_layout_box_h)
        self.url_input_box.setObjectName("url_input_box")
        self.urlbox.addWidget(self.url_input_box)
        self.right_layout_box.addLayout(self.urlbox)
        self.outputbox = QtWidgets.QVBoxLayout()
        self.outputbox.setObjectName("outputbox")
        self.download_info_btn = QtWidgets.QPushButton(self.main_panel_layout_box_h)
        self.download_info_btn.setObjectName("download_info_btn")
        self.outputbox.addWidget(self.download_info_btn)
        self.download_epub_btn = QtWidgets.QPushButton(self.main_panel_layout_box_h)
        self.download_epub_btn.setObjectName("download_epub_btn")
        self.outputbox.addWidget(self.download_epub_btn)
        self.output_line_seperator = QtWidgets.QFrame(self.main_panel_layout_box_h)
        self.output_line_seperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.output_line_seperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_line_seperator.setObjectName("output_line_seperator")
        self.outputbox.addWidget(self.output_line_seperator)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.outputbox.addItem(spacerItem)
        self.open_folder_btn = QtWidgets.QPushButton(self.main_panel_layout_box_h)
        self.open_folder_btn.setObjectName("open_folder_btn")
        self.outputbox.addWidget(self.open_folder_btn)
        self.output_field = QtWidgets.QTextEdit(self.main_panel_layout_box_h)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_field.sizePolicy().hasHeightForWidth())
        self.output_field.setSizePolicy(sizePolicy)
        self.output_field.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.output_field.setObjectName("output_field")
        self.outputbox.addWidget(self.output_field)
        self.progressbar = QtWidgets.QProgressBar(self.main_panel_layout_box_h)
        self.progressbar.setProperty("value", 0)
        self.progressbar.setTextVisible(True)
        self.progressbar.setInvertedAppearance(False)
        self.progressbar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar.setObjectName("progressbar")
        self.outputbox.addWidget(self.progressbar)
        self.right_layout_box.addLayout(self.outputbox)
        self.left_layout_box.addLayout(self.right_layout_box)
        self.setCentralWidget(self.main_panel)
        self.tabs.setCurrentIndex(0)
        self.translate = QtCore.QCoreApplication.translate
        QtCore.QMetaObject.connectSlotsByName(self)
        self.set_text()
        self.register_listeners()


        # Events
        self.show()

    def set_text(self):
        self.tabs.setToolTip("Shows novel info")
        self.title_label.setText("Title:")
        self.title_value.setText("________")
        self.chapter_label.setText("Chapters:")
        self.chapter_value.setText("________")
        self.tabs.setTabText(self.tabs.indexOf(self.tab_info), "Info")
        self.tabs.setTabText(self.tabs.indexOf(self.tab_chapters), "Chapters")
        self.url_label.setText("URL:")
        self.download_info_btn.setText("Download Novel Info")
        self.download_epub_btn.setText("Download EPUB")
        self.open_folder_btn.setText("Open Output Directory")

    def register_listeners(self):
        # Level: GUI
        self.open_folder_btn.clicked.connect(self.open_folder)

        # Level: PubSub
        subscribe(self.download_bar_listener, "download_number")

    @register()
    def open_folder(self):
        if "\gui" in os.getcwd():
            os.chdir("..")
        subprocess.Popen(f'explorer "{os.getcwd()}\publish"')

    def download_bar_listener(self, max_val, now_val):
        percentage = int((now_val / max_val) * 100)
        self.progressbar.setValue(percentage)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = GUI()
    file = QtCore.QFile(os.getcwd() + "/style/darktheme.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    app.exec()