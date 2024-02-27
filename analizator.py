# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # создание окна приложения и его размеры
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 638)

        # установка шрифта
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 920, 371))

        # Установка на экран приложения графика и задание ему шрифта
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 440, 271, 151))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)

        # ЛЕВЫЙ БЛОК КНОПОК
        # Установка группы объектов конфига и класса
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 271, 151))

        # добавление к групбоксу вертикального выравнивания
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Добавление выпадающего списка моделей анализатора
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.move(0, 0)
        self.comboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())

        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBox.setBaseSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # Добавление кнопки конфигурация
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        # Добавление кнопки подключения устройства
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")

        # порядок размещения кнопок на экране приложения
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.pushButton_8)

        # ЦЕНТРАЛЬНЫЙ ЛЕВЫЙ БЛОК
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(320, 440, 271, 151))

        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(320, 440, 271, 151))

        # Добавление выпадающего списка моделей анализатора
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_4.setGeometry(QtCore.QRect(0, 13, 271, 27))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("ОПУ -1 ")
        self.comboBox_4.addItem("ОПУ -2 ")

        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setText("Конфигурация")
        self.pushButton_9.setGeometry(QtCore.QRect(0, 60, 271, 29))

        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setText("Подключиться к устройству")
        self.pushButton_10.setGeometry(QtCore.QRect(0, 108, 271, 29))

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 415, 271, 29))

        # ЦЕНТРАЛЬНЫЙ ПРАВЫЙ БЛОК
        # Установка группы кнопок управления измерениями

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(640, 440, 271, 151))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

        # добавление к групбоксу вертикального выравнивания
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 271, 136))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # добавление кнопки остановки измерения
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        # добавление кнопки аварийной остановки измерения
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        # добавление кнопки запуска измерений
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        # добавление отображения прогресса выполнения измерений
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")

        # порядок размещения кнопок на экране приложения
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.pushButton_5)

        # ПРАВЫЙ БЛОК
        # Установка группы кнопки сохранения результатов и выхода из программы

        # self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        # self.groupBox_3.setGeometry(QtCore.QRect(960, 440, 271, 151))
        # font = QtGui.QFont()
        # font.setFamily("Liberation Serif")
        # font.setPointSize(14)
        # self.groupBox_3.setFont(font)
        # self.groupBox_3.setTitle("")
        # self.groupBox_3.setObjectName("groupBox_3")
        # self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        # self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 271, 151))
        # self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        # self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        # self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_3.setObjectName("verticalLayout_3")

        # добавление кнопки сохранения результатов
        # self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setFamily("Liberation Serif")
        # font.setPointSize(14)
        # self.pushButton_7.setFont(font)
        # self.pushButton_7.setObjectName("pushButton_7")

        # добавление кнопки выхода из программы
        # self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setFamily("Liberation Serif")
        # font.setPointSize(14)
        # self.pushButton_6.setFont(font)
        # self.pushButton_6.setObjectName("pushButton_6")
        # порядок размещения кнопок на экране приложения
        # self.verticalLayout_3.addWidget(self.pushButton_7)
        # self.verticalLayout_3.addWidget(self.pushButton_6)

        # Установка надписей на эран приложения
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 410, 259, 39))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 400, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 61, 16))
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Установка меню
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 21))

        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")

        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")

        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.menu.setFont(font)
        self.menu_2.setFont(font)
        self.menu_3.setFont(font)

        # добавление кликабельных кнопок
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()
        self.pushButton_2.clicked.connect(self.config)
        self.pushButton_9.clicked.connect(self.config_opu)

        self.action_3.triggered.connect(lambda: self.exit())
        self.action_4.triggered.connect(lambda: self.config())
        self.action_5.triggered.connect(lambda: self.config_opu())
        self.action_6.triggered.connect(lambda: self.clicked_spravka())

        # добавление вывода текста нажатой кнопки в консоль

    def add_functions(self):
        self.pushButton_2.clicked.connect(lambda: self.write_text(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write_text(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.write_text(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.write_text(self.pushButton_5.text()))

        # self.pushButton_6.clicked.connect(lambda: self.write_text(self.pushButton_6.text()))
        # self.pushButton_7.clicked.connect(lambda: self.write_text(self.pushButton_7.text()))

        self.pushButton_8.clicked.connect(lambda: self.write_text(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.write_text(self.pushButton_9.text()))
        self.pushButton_10.clicked.connect(lambda: self.write_text(self.pushButton_10.text()))

        self.action.triggered.connect(lambda: self.write_text(self.action.text()))
        self.action_2.triggered.connect(lambda: self.write_text(self.action_2.text()))
        self.action_3.triggered.connect(lambda: self.write_text(self.action_3.text()))
        self.action_4.triggered.connect(lambda: self.write_text(self.action_4.text()))
        self.action_5.triggered.connect(lambda: self.write_text(self.action_5.text()))
        self.action_6.triggered.connect(lambda: self.write_text(self.action_6.text()))

    def write_text(self, text):
        print(text)

    def config_opu(self):
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        OPU_Config = QDialog()
        OPU_Config.setWindowTitle("Выбор конфигурации опорно-поворотного устройства")
        OPU_Config.resize(440, 240)
        OPU_Config.setFont(font)

        ugol = QtWidgets.QLabel(OPU_Config)
        ugol.setText("Начальный угол")
        ugol.move(10, 0)
        ugol_start = QtWidgets.QDoubleSpinBox(OPU_Config)
        ugol_start.setMinimum(0.00)
        ugol_start.setMaximum(180.00)
        ugol_start.move(10, 20)

        ugol_finish = QtWidgets.QLabel(OPU_Config)
        ugol_finish.setText("Конечный угол")
        ugol_finish.move(180, 0)
        ugol_finish = QtWidgets.QDoubleSpinBox(OPU_Config)
        ugol_finish.setMinimum(0.00)
        ugol_finish.setMaximum(180.00)
        ugol_finish.move(180, 20)

        shag = QtWidgets.QLabel(OPU_Config)
        shag.setText("Шаг")
        shag.move(340, 0)
        shag = QtWidgets.QDoubleSpinBox(OPU_Config)
        shag.setMinimum(0.00)
        shag.setMaximum(180.00)
        shag.move(340, 20)

        azimut = QtWidgets.QLabel(OPU_Config)
        azimut.setText("Азимут")
        azimut.move(10, 60)
        azimut = QtWidgets.QDoubleSpinBox(OPU_Config)
        azimut.setMinimum(0.00)
        azimut.setMaximum(180.00)
        azimut.move(10, 80)

        elev = QtWidgets.QLabel(OPU_Config)
        elev.setText("Элевация")
        elev.move(180, 60)
        elev = QtWidgets.QDoubleSpinBox(OPU_Config)
        elev.setMinimum(0.00)
        elev.setMaximum(180.00)
        elev.move(180, 80)

        ugol_mesta = QtWidgets.QLabel(OPU_Config)
        ugol_mesta.setText("Угол места")
        ugol_mesta.move(340, 60)
        ugol_mesta = QtWidgets.QDoubleSpinBox(OPU_Config)
        ugol_mesta.setMinimum(0.00)
        ugol_mesta.setMaximum(180.00)
        ugol_mesta.move(340, 80)

        kalibr = QtWidgets.QLabel(OPU_Config)
        kalibr.setText("Калибровка")
        kalibr.move(300, 120)
        kalibr = QtWidgets.QPushButton(OPU_Config)
        kalibr.setText("Начать")
        kalibr.resize(100, 29)
        kalibr.move(300, 140)

        null = QtWidgets.QLabel(OPU_Config)
        null.setText("Начальное положение")
        null.move(10, 120)
        nul_btn = QtWidgets.QPushButton(OPU_Config)
        nul_btn.setText("Установить")
        nul_btn.resize(180, 29)
        nul_btn.move(10, 140)

        pod = QtWidgets.QLabel(OPU_Config)
        pod.setText("Применить выбранную конфигурацию")
        pod.move(80, 180)
        btn_pod = QtWidgets.QPushButton(OPU_Config)
        btn_pod.setText("Подтвердить")
        btn_pod.resize(180, 29)
        btn_pod.move(120, 200)

        OPU_Config.exec_()

    def config(self):
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)

        WindowConfig = QDialog()
        WindowConfig.setWindowTitle("Выбор конфигурации векторного анализатора цепей")
        WindowConfig.resize(520, 220)
        WindowConfig.setFont(font)

        self.parameters = []

        power = QtWidgets.QLabel(WindowConfig)
        power.setText("Мощность сигнала")
        power.move(10, 0)

        self.power_1 = QtWidgets.QDoubleSpinBox(WindowConfig)
        self.power_1.setMaximum(9999999999.00)
        self.power_1.move(10, 20)

        self.comboBox_4 = QtWidgets.QComboBox(WindowConfig)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("Вт")
        self.comboBox_4.addItem("КВт")
        self.comboBox_4.addItem("МВТ")

        self.comboBox_4.move(150, 20)

        min_frequency = QtWidgets.QLabel(WindowConfig)
        min_frequency.setText("Минимальная частота")
        min_frequency.move(10, 60)
        self.min_frequency_1 = QtWidgets.QDoubleSpinBox(WindowConfig)
        self.min_frequency_1.setMaximum(999999999999.00)
        self.min_frequency_1.move(10, 80)

        self.comboBox_5 = QtWidgets.QComboBox(WindowConfig)
        self.comboBox_5.setObjectName("comboBox_4")
        self.comboBox_5.addItem("Гц")
        self.comboBox_5.addItem("КГц")
        self.comboBox_5.addItem("МГц")
        self.comboBox_5.addItem("ГГц")
        self.comboBox_5.move(150, 80)

        max_frequency = QtWidgets.QLabel(WindowConfig)
        max_frequency.setText("Максимальная частота")
        max_frequency.move(280, 60)
        self.max_frequency_1 = QtWidgets.QDoubleSpinBox(WindowConfig)
        self.max_frequency_1.setMaximum(999999999999.00)
        self.max_frequency_1.setMinimum(0.00)
        self.max_frequency_1.move(280, 80)

        self.comboBox_6 = QtWidgets.QComboBox(WindowConfig)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("Гц")
        self.comboBox_6.addItem("КГц")
        self.comboBox_6.addItem("МГц")
        self.comboBox_6.addItem("ГГц")
        self.comboBox_6.move(420, 80)

        tochki = QtWidgets.QLabel(WindowConfig)
        tochki.setText("Количество точек измерения")
        tochki.move(280, 0)
        self.tochki_1 = QtWidgets.QSpinBox(WindowConfig)
        self.tochki_1.resize(135, 28)
        self.tochki_1.setMaximum(9999999999)
        self.tochki_1.move(280, 20)

        port = QtWidgets.QLabel(WindowConfig)
        port.setText("Порт управления")
        port.move(280, 120)

        self.comboBox_7 = QtWidgets.QComboBox(WindowConfig)
        self.comboBox_7.setObjectName("comboBox_7")

        s = QtWidgets.QLabel(WindowConfig)
        s.setText("S параметр")
        s.move(140, 120)
        self.comboBox_8 = QtWidgets.QComboBox(WindowConfig)
        self.comboBox_8.setObjectName("comboBox_8")

        self.comboBox_8.addItem("S11")
        self.comboBox_8.addItem("S12")
        self.comboBox_8.addItem("S13")
        self.comboBox_8.addItem("S14")

        self.comboBox_8.addItem("S21")
        self.comboBox_8.addItem("S22")
        self.comboBox_8.addItem("S23")
        self.comboBox_8.addItem("S24")

        self.comboBox_8.addItem("S31")
        self.comboBox_8.addItem("S32")
        self.comboBox_8.addItem("S33")
        self.comboBox_8.addItem("S34")

        self.comboBox_8.addItem("S41")
        self.comboBox_8.addItem("S42")
        self.comboBox_8.addItem("S43")
        self.comboBox_8.addItem("S44")

        self.comboBox_8.move(10, 140)

        format = QtWidgets.QLabel(WindowConfig)
        format.setText("Тип измерения")
        format.move(10, 120)
        self.comboBox_9 = QtWidgets.QComboBox(WindowConfig)
        self.comboBox_9.setObjectName("comboBox_9")

        self.comboBox_9.addItem("Магнитуда")
        self.comboBox_9.addItem("Фаза")
        self.comboBox_9.addItem("КСВ")
        self.comboBox_9.move(140, 140)

        self.serial = QSerialPort()
        self.serial.setBaudRate(115200)
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portlist.append(port.portName())
        print(portlist)
        self.comboBox_7.addItems(portlist)
        self.comboBox_7.move(280, 140)

        self.btn_save = QtWidgets.QPushButton(WindowConfig)
        self.btn_save.setText("Подтвердить")
        self.btn_save.move(200, 180)
        self.btn_save.resize(120, 40)

        self.btn_save.clicked.connect(lambda: self.parametrs_config())

        WindowConfig.exec_()
        


    def parametrs_config(self):
        self.param = [self.power_1.value(),
                 self.comboBox_4.currentText(),
                 self.min_frequency_1.value(),
                 self.comboBox_5.currentText(),
                 self.max_frequency_1.value(),
                 self.comboBox_6.currentText(),
                 self.comboBox_8.currentText(),
                 self.comboBox_9.currentText(),
                 self.comboBox_7.currentText()
                 ]
        print(self.param)



    def clicked_spravka(self):
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)

        WindowSpravka = QDialog()
        WindowSpravka.setWindowTitle("О приложении")
        WindowSpravka.resize(400, 200)
        WindowSpravka.setFont(font)

        razrab = QtWidgets.QTextEdit(WindowSpravka)
        razrab.setText("Приложение создано инженером - конструктором отдела 703"
                       " Глазыриным Вадимом Денисовичем ")
        razrab.resize(400, 180)
        razrab.move(10, 10)

        WindowSpravka.exec_()

    def exit(self):
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)

        WindowExit = QDialog()
        WindowExit.setWindowTitle("Выход из программы")
        WindowExit.resize(220, 150)
        WindowExit.setFont(font)

        message_exit = QtWidgets.QLabel(WindowExit)
        message_exit.setText("Вы точно хотите выйти?")
        message_exit.move(10, 20)
        message_exit.resize(200, 100)

        self.btn_cancel = QtWidgets.QPushButton(WindowExit)
        self.btn_cancel.setText("Нет")
        self.btn_cancel.move(100, 100)
        self.btn_cancel.resize(50, 29)

        self.btn_ok = QtWidgets.QPushButton(WindowExit)
        self.btn_ok.setText("Да")

        self.btn_ok.move(50, 100)
        self.btn_ok.resize(50, 29)

        self.btn_ok.clicked.connect(lambda: self.close())

        WindowExit.exec_()

    def close(self):
        self.close()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Универсальный комплекс  Gl inc"))

        self.comboBox.setItemText(0, _translate("MainWindow", "ZVA-24"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ZVA-8"))

        self.label.setText(_translate("MainWindow", "Векторный анализатор цепей"))
        self.label_2.setText(_translate("MainWindow", " F, МГц"))
        self.label_3.setText(_translate("MainWindow", "P, Дб"))
        self.label_4.setText(_translate("MainWindow", "Опорно-поворотное устройство"))

        self.pushButton_2.setText(_translate("MainWindow", "Конфигурация"))
        self.pushButton_3.setText(_translate("MainWindow", "Начать измерение"))
        self.pushButton_4.setText(_translate("MainWindow", "Остановить измерение"))
        self.pushButton_5.setText(_translate("MainWindow", "Аварийная остановка"))

        # self.pushButton_6.setText(_translate("MainWindow", "Выход"))
        # self.pushButton_7.setText(_translate("MainWindow", "Сохранить результаты"))

        self.pushButton_8.setText(_translate("MainWindow", "Подключиться к устройству"))
        self.menu.setTitle(_translate("MainWindow", "&Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "&Параметры"))
        self.menu_3.setTitle(_translate("MainWindow", "&Справка"))

        self.action.setText(_translate("MainWindow", "&Открыть"))
        self.action_2.setText(_translate("MainWindow", "&Сохранить"))
        self.action_3.setText(_translate("MainWindow", "&Выход"))
        self.action_4.setText(_translate("MainWindow", "&Конфигурация анализатора"))
        self.action_5.setText(_translate("MainWindow", "&Конфигурация ОПУ"))
        self.action_6.setText(_translate("MainWindow", "&О программе"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
