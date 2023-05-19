#Criação de uma janela(Utilizando o QT Designer) para calculo da resistência a compressão de paredes em Alvenaria Estrutural,
# conforme a ABNT NBR 16868-1/2021 – Alvenaria estrutural.
# Parte 1: Projeto. Esta norma estabelece os requisitos para o projeto de estruturas de alvenaria e à análise do desempenho estrutural
# de elementos de alvenaria inseridos em outros sistemas estruturais.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):#Classe para a criação e carregamento da janela
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 1091, 691))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dados = QtWidgets.QLabel(self.frame)
        self.dados.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dados.setFont(font)
        self.dados.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.dados.setObjectName("dados")
        self.eficiencia = QtWidgets.QLabel(self.frame)
        self.eficiencia.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eficiencia.setFont(font)
        self.eficiencia.setObjectName("eficiencia")
        self.espessura = QtWidgets.QLabel(self.frame)
        self.espessura.setGeometry(QtCore.QRect(10, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.espessura.setFont(font)
        self.espessura.setObjectName("espessura")
        self.lineEdit_t = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_t.setGeometry(QtCore.QRect(210, 100, 113, 22))
        self.lineEdit_t.setObjectName("lineEdit_t")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(330, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.altura = QtWidgets.QLabel(self.frame)
        self.altura.setGeometry(QtCore.QRect(10, 140, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.altura.setFont(font)
        self.altura.setObjectName("altura")
        self.lineEdit_2_h = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_h.setGeometry(QtCore.QRect(210, 140, 113, 22))
        self.lineEdit_2_h.setObjectName("lineEdit_2_h")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(330, 140, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3_C = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_C.setGeometry(QtCore.QRect(210, 180, 113, 22))
        self.lineEdit_3_C.setObjectName("lineEdit_3_C")
        self.comprimento = QtWidgets.QLabel(self.frame)
        self.comprimento.setGeometry(QtCore.QRect(10, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comprimento.setFont(font)
        self.comprimento.setObjectName("comprimento")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(330, 180, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.carregamento = QtWidgets.QLabel(self.frame)
        self.carregamento.setGeometry(QtCore.QRect(10, 220, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.carregamento.setFont(font)
        self.carregamento.setObjectName("carregamento")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(330, 220, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_4_G_Q = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4_G_Q.setGeometry(QtCore.QRect(210, 220, 113, 22))
        self.lineEdit_4_G_Q.setObjectName("lineEdit_4_G_Q")
        self.lineEdit_5_Coef_Acoes = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5_Coef_Acoes.setGeometry(QtCore.QRect(390, 260, 113, 22))
        self.lineEdit_5_Coef_Acoes.setText("")
        self.lineEdit_5_Coef_Acoes.setObjectName("lineEdit_5_Coef_Acoes")
        self.coef_acoes = QtWidgets.QLabel(self.frame)
        self.coef_acoes.setGeometry(QtCore.QRect(10, 250, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.coef_acoes.setFont(font)
        self.coef_acoes.setObjectName("coef_acoes")
        self.coef_resist = QtWidgets.QLabel(self.frame)
        self.coef_resist.setGeometry(QtCore.QRect(10, 290, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.coef_resist.setFont(font)
        self.coef_resist.setObjectName("coef_resist")
        self.lineEdit_6_coet_rest = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6_coet_rest.setGeometry(QtCore.QRect(390, 300, 113, 22))
        self.lineEdit_6_coet_rest.setText("")
        self.lineEdit_6_coet_rest.setObjectName("lineEdit_6_coet_rest")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(540, 50, 541, 411))
        self.label_13.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Parede02.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(170, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(56, 56, 168);\n"
"background-color: rgb(72, 0, 217);")
        self.pushButton.setObjectName("pushButton")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(10, 470, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_14.setStyleSheet("background-color: rgb(130, 130, 130);\n"
"background-color: rgb(255, 77, 64);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(50, 520, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(50, 550, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(50, 610, 751, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(50, 580, 431, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(50, 640, 661, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(500, 550, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(860, 610, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(850, 640, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(120, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color: rgb(255, 99, 38);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background-color: rgb(255, 99, 38);\n"
"background-color: rgb(138, 138, 138);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(440, 520, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(610, 580, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.labelResultadoEsbeltez = QtWidgets.QLabel(self.frame)
        self.labelResultadoEsbeltez.setGeometry(QtCore.QRect(290, 520, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResultadoEsbeltez.setFont(font)
        self.labelResultadoEsbeltez.setObjectName("labelResultadoEsbeltez")
        self.labelResultadoArea = QtWidgets.QLabel(self.frame)
        self.labelResultadoArea.setGeometry(QtCore.QRect(370, 550, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResultadoArea.setFont(font)
        self.labelResultadoArea.setObjectName("labelResultadoArea")
        self.labelResultadoRedutorR = QtWidgets.QLabel(self.frame)
        self.labelResultadoRedutorR.setGeometry(QtCore.QRect(490, 580, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResultadoRedutorR.setFont(font)
        self.labelResultadoRedutorR.setObjectName("labelResultadoRedutorR")
        self.labelResultadoPrisma = QtWidgets.QLabel(self.frame)
        self.labelResultadoPrisma.setGeometry(QtCore.QRect(730, 610, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResultadoPrisma.setFont(font)
        self.labelResultadoPrisma.setObjectName("labelResultadoPrisma")
        self.labelResultadoBloco = QtWidgets.QLabel(self.frame)
        self.labelResultadoBloco.setGeometry(QtCore.QRect(720, 640, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResultadoBloco.setFont(font)
        self.labelResultadoBloco.setObjectName("labelResultadoBloco")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dados.setText(_translate("MainWindow", "DADOS DA PAREDE:"))
        self.eficiencia.setText(_translate("MainWindow", "Eficiência:"))
        self.espessura.setText(_translate("MainWindow", "Espessura (t):"))
        self.label_4.setText(_translate("MainWindow", "(m)"))
        self.altura.setText(_translate("MainWindow", "Altura (h):"))
        self.label_6.setText(_translate("MainWindow", "(m)"))
        self.comprimento.setText(_translate("MainWindow", "Comprimento (L):"))
        self.label_8.setText(_translate("MainWindow", "(m)"))
        self.carregamento.setText(_translate("MainWindow", "Carregamento (G+Q):"))
        self.label_10.setText(_translate("MainWindow", "(kN/m)"))
        self.coef_acoes.setText(_translate("MainWindow", "Coeficiente de ponderação das ações:"))
        self.coef_resist.setText(_translate("MainWindow", "Coeficiente de ponderação das resistências:"))
        self.pushButton.setText(_translate("MainWindow", "DIMENSIONAR"))
        self.label_14.setText(_translate("MainWindow", "RESULTADOS:"))
        self.label_15.setText(_translate("MainWindow", "ÍNDICE DE ESBELTEZ ( ):"))
        self.label_16.setText(_translate("MainWindow", "ÁREA DA SEÇÃO TRANSVERSAL (A):"))
        self.label_17.setText(_translate("MainWindow", "RESISTÊNCIA CARACTERÍSTICA DE COMPRESSÃO SIMPLES DO PRISMA (fpk):"))
        self.label_18.setText(_translate("MainWindow", "COEFICIENTE REDUTOR DEVIDO À ESBELTEZ (R):"))
        self.label_19.setText(_translate("MainWindow", "RESISTÊNCIA CARACTERÍSTICA DE COMPRESSÃO SIMPLES DO BLOCO (fbk):"))
        self.label_20.setText(_translate("MainWindow", "(m2)"))
        self.label_21.setText(_translate("MainWindow", "(MPa)"))
        self.label_22.setText(_translate("MainWindow", "(MPa)"))
        self.radioButton.setText(_translate("MainWindow", "Bloco Cerâmico"))
        self.radioButton_2.setText(_translate("MainWindow", "Bloco de  Concreto"))
        self.label_23.setText(_translate("MainWindow", "(adimensional)"))
        self.label_24.setText(_translate("MainWindow", "(adimensional)"))
        self.labelResultadoEsbeltez.setText(_translate("MainWindow", "TextLabel"))
        self.labelResultadoArea.setText(_translate("MainWindow", "TextLabel"))
        self.labelResultadoRedutorR.setText(_translate("MainWindow", "TextLabel"))
        self.labelResultadoPrisma.setText(_translate("MainWindow", "TextLabel"))
        self.labelResultadoBloco.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.clicked.connect(self.esbeltez)
        self.pushButton.clicked.connect(self.area)
        self.pushButton.clicked.connect(self.redutor)
        self.pushButton.clicked.connect(self.prisma)

    def esbeltez(self):#Está função Calcula o índice de esbeltez: a razão entre a altura efetiva e a espessura efetiva da parede
        numb1 = self.lineEdit_t.text()
        numb2 = self.lineEdit_2_h.text()
        x = float(numb2)#Define a altura da parede
        y = float(numb1)#Define a espessura da parede
        z = x/y
        self.labelResultadoEsbeltez.setText(f'{z:.2f}')

    def area(self):#Está função calcula a área da parede
        numb3 = self.lineEdit_t.text()
        numb4 = self.lineEdit_3_C.text()
        aa = float(numb3)#define o comprimento da parede
        bb = float(numb4)#define a espessura da parede
        AA = aa*bb
        self.labelResultadoArea.setText(f'{AA:.2f}')

    def redutor(self):#Está função calcula o coeficiente redutor devido à esbeltez
        numb5 = self.lineEdit_t.text()
        numb6 = self.lineEdit_2_h.text()
        ss = float(numb5)
        dd = float(numb6)
        R = (1-(dd/(40*ss))**(3))
        self.labelResultadoRedutorR.setText(f'{R:.2f}')

    def prisma(self): #Está função calcula a resistência característica de compressão simples do prisma e do bloco - fpk
        numb7 = self.lineEdit_4_G_Q.text()
        numb8 = self.lineEdit_5_Coef_Acoes.text()
        numb9 = self.lineEdit_6_coet_rest.text()
        numb10 = self.lineEdit_3_C.text()
        gg = float(numb7)
        ee = float(numb8)
        f = float(numb9)
        l = float(numb10)
        fpk = (gg*ee*ff*l)/(0.875*0.336*0.7)/1000
        if self.radioButton.isChecked():
            fbk = fpk/0.5
        elif self.radioButton_2.isChecked():
            fbk = fpk/0.8
        self.labelResultadoPrisma.setText(f'{fpk:.2f}')#calcula a resistência característica de compressão simples do prisma - fpk
        self.labelResultadoBloco.setText(f'{fbk:.2f}')#calcula a resistência característica de compressão simples do bloco - fbk

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
