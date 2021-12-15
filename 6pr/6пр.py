from PyQt5 import QtCore, QtGui, QtWidgets

ch=[]
matr=["""0""",
"""1. Распечатать все квадраты, не
провосходящие N в порядке возрастания.

Введите в окно целое неотрицательное
значение N.""",
      
"""2. Вывести наименьший натуральный
делитель числа N, отличающийся
от единицы.

Введите в окно целое неотрицательное
число N (N>=2)""",
      
"""3. Найти наибольшую целую
степень двойки, не превосходящую N.
вывести показатель степени и саму степень.

Введите в окно целое неотрицательное
число N""",

"""4. В первый день было пройдено Х км,
а затем каждый день расстояние
увеличивалось на 10% от предыдущего
значения. По данному числу У
определить номер дня, на который
расстояние составит не менее У км.

Введите в окно через пробел
целые натуральные числа Х и У.""",

"""5. Введите в окно последовательность
целых неотрицательных чисел.
Последовательность необходимо
ввести, разделяя каждое число
пробелом. Завершать цифрой
0 не нужно.

Выводом будет количество
элементов последовательности.""",

"""6. Введите в окно последовательность
целых неотрицательных чисел.
Последовательность необходимо
ввести, разделяя каждое число
пробелом. Завершать цифрой
0 не нужно.

Выводом будет среднее
значение всех элементов
последовательности.""",

"""7. Введите в окно последовательность
целых неотрицательных чисел.
Последовательность необходимо
ввести, разделяя каждое число
пробелом. Завершать цифрой
0 не нужно.

Выводом будет количество
случаев, когда элемент
последовательности оказался больше
предыдущего элемента.""",

"""8. Введите в окно последовательность
целых неотрицательных чисел.
Последовательность необходимо
ввести, разделяя каждое число
пробелом. Завершать цифрой
0 не нужно.

Выводом будет те наибольшие
числа подряд идущих элементов
последовательности, которые равны
друг другу.
"""]


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(980, 780)
        Dialog.setMinimumSize(QtCore.QSize(980, 780))
        Dialog.setMaximumSize(QtCore.QSize(980, 780))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setMouseTracking(True)
        Dialog.setTabletTracking(True)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet("background-color: #012126 ;")
        self.button1 = QtWidgets.QPushButton(Dialog)
        self.button1.setGeometry(QtCore.QRect(30, 70, 118, 118))
        self.button1.setMinimumSize(QtCore.QSize(118, 118))
        self.button1.setMaximumSize(QtCore.QSize(118, 118))
        self.button1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button1.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(Dialog)
        self.button2.setGeometry(QtCore.QRect(30, 220, 118, 118))
        self.button2.setMinimumSize(QtCore.QSize(118, 118))
        self.button2.setMaximumSize(QtCore.QSize(118, 118))
        self.button2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button2.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(Dialog)
        self.button3.setGeometry(QtCore.QRect(30, 370, 118, 118))
        self.button3.setMinimumSize(QtCore.QSize(118, 118))
        self.button3.setMaximumSize(QtCore.QSize(118, 118))
        self.button3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button3.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(Dialog)
        self.button4.setGeometry(QtCore.QRect(30, 520, 118, 118))
        self.button4.setMinimumSize(QtCore.QSize(118, 118))
        self.button4.setMaximumSize(QtCore.QSize(118, 118))
        self.button4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button4.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button4.setObjectName("button4")
        self.button7 = QtWidgets.QPushButton(Dialog)
        self.button7.setGeometry(QtCore.QRect(180, 430, 118, 118))
        self.button7.setMinimumSize(QtCore.QSize(118, 118))
        self.button7.setMaximumSize(QtCore.QSize(118, 118))
        self.button7.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button7.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button7.setObjectName("button7")
        self.button5 = QtWidgets.QPushButton(Dialog)
        self.button5.setEnabled(True)
        self.button5.setGeometry(QtCore.QRect(180, 130, 118, 118))
        self.button5.setMinimumSize(QtCore.QSize(118, 118))
        self.button5.setMaximumSize(QtCore.QSize(118, 118))
        self.button5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button5.setMouseTracking(True)
        self.button5.setTabletTracking(True)
        self.button5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button5.setAcceptDrops(False)
        self.button5.setAutoFillBackground(False)
        self.button5.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button5.setFlat(False)
        self.button5.setObjectName("button5")
        self.button8 = QtWidgets.QPushButton(Dialog)
        self.button8.setGeometry(QtCore.QRect(180, 580, 118, 118))
        self.button8.setMinimumSize(QtCore.QSize(118, 118))
        self.button8.setMaximumSize(QtCore.QSize(118, 118))
        self.button8.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button8.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button8.setIconSize(QtCore.QSize(20, 20))
        self.button8.setObjectName("button8")
        self.button6 = QtWidgets.QPushButton(Dialog)
        self.button6.setGeometry(QtCore.QRect(180, 280, 118, 118))
        self.button6.setMinimumSize(QtCore.QSize(118, 118))
        self.button6.setMaximumSize(QtCore.QSize(118, 118))
        self.button6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button6.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.button6.setObjectName("button6")
        self.label_big = QtWidgets.QLabel(Dialog)
        self.label_big.setGeometry(QtCore.QRect(340, 90, 581, 321))
        self.label_big.setStyleSheet("color: #00bdde;\n"
"font: 12pt \"Yu Gothic UI Semibold\";\n"
"background-color: #003640;\n"
"")
        self.label_big.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_big.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_big.setAlignment(QtCore.Qt.AlignCenter)
        self.label_big.setText("")
        self.label_big.setObjectName("label_big")
        self.buttonE = QtWidgets.QPushButton(Dialog)
        self.buttonE.setGeometry(QtCore.QRect(760, 480, 161, 71))
        self.buttonE.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonE.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.buttonE.setStyleSheet("  QPushButton {\n"
"    \n"
"    font: 22pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #003640 ;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #34cfeb ; \n"
"    background-color: #004c59 ; \n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: #008299 ; \n"
"    background-color: #001a1f ; \n"
"  }")
        self.buttonE.setObjectName("buttonE")
        self.line_enter = QtWidgets.QLineEdit(Dialog)
        self.line_enter.setGeometry(QtCore.QRect(760, 580, 161, 61))
        self.line_enter.setStyleSheet("color: #00bdde;\n"
"font: 63 17pt \"Yu Gothic UI Semibold\";\n"
"background-color: #003640;\n"
"border: none;")
        self.line_enter.setAlignment(QtCore.Qt.AlignCenter)
        self.line_enter.setObjectName("line_enter")
        self.button_up_0 = QtWidgets.QPushButton(Dialog)
        self.button_up_0.setGeometry(QtCore.QRect(340, 60, 351, 28))
        self.button_up_0.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #012126 ;\n"
"    border: none;\n"
"}")
        self.button_up_0.setObjectName("button_up_0")
        self.label_small = QtWidgets.QLabel(Dialog)
        self.label_small.setGeometry(QtCore.QRect(360, 460, 331, 211))
        self.label_small.setStyleSheet("color: #00bdde;\n"
"font: 16pt \"Yu Gothic UI Semibold\";\n"
"background-color: #003640;\n"
"")
        self.label_small.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_small.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_small.setLineWidth(1)
        self.label_small.setMidLineWidth(0)
        self.label_small.setText("")
        self.label_small.setAlignment(QtCore.Qt.AlignCenter)
        self.label_small.setObjectName("label_small")
        self.button_name_0 = QtWidgets.QPushButton(Dialog)
        self.button_name_0.setGeometry(QtCore.QRect(330, 720, 351, 28))
        self.button_name_0.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Yu Gothic UI Semibold\";\n"
"    color: #00bdde ;\n"
"    background-color: #012126 ;\n"
"    border: none;\n"
"}")
        self.button_name_0.setObjectName("button_name_0")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Харитонова Я."))
        self.button1.setText(_translate("Dialog", "1"))
        self.button2.setText(_translate("Dialog", "2"))
        self.button3.setText(_translate("Dialog", "3"))
        self.button4.setText(_translate("Dialog", "4"))
        self.button7.setText(_translate("Dialog", "7"))
        self.button5.setText(_translate("Dialog", "5"))
        self.button8.setText(_translate("Dialog", "8"))
        self.button6.setText(_translate("Dialog", "6"))
        self.buttonE.setText(_translate("Dialog", "Enter"))
        self.button_up_0.setText(_translate("Dialog", "Краткое описание выполняемой задачи:"))
        self.button_name_0.setText(_translate("Dialog", "Харитонова Яна У-214"))


if __name__ == "__main__":
    import sys

    
    app = QtWidgets.QApplication(sys.argv)

    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    def b1():
        ui.label_big.setText(matr[1])
        ch.append("1")
    def b2():
        ui.label_big.setText(matr[2])
        ch.append("2")
    def b3():
        ui.label_big.setText(matr[3])
        ch.append("3")
    def b4():
        ui.label_big.setText(matr[4])
        ch.append("4")
    def b5():
        ui.label_big.setText(matr[5])
        ch.append("5")
    def b6():
        ui.label_big.setText(matr[6])
        ch.append("6")
    def b7():
        ui.label_big.setText(matr[7])
        ch.append("7")
    def b8():
        ui.label_big.setText(matr[8])
        ch.append("8")



    def E():


        
        if ch[-1] == "1":
            er = []
            n = int(ui.line_enter.text())
            i = 0
            while True:
                a = i * i
                if a < n:
                    er.append(a)
                    i+=1
                else:
                    break
            label_small = er
            ui.label_small.setText(str(label_small))
        


            
        elif ch[-1] == "2":
            i = 2
            n = int(ui.line_enter.text())
            while int(n) % i != 0:
                i += 1
            label_small = i
            ui.label_small.setText(str(label_small))

            
        elif ch[-1] == "3":
            i = 2
            powContainer = 2
            counter = 1
            n = int(ui.line_enter.text())
        
            while powContainer * i < int(n):
                powContainer *= i
                counter+=1
            label_small=("""Показатель степени: %s
    Степень: %s""" % (powContainer, counter))
            ui.label_small.setText(str(label_small))


            
        elif ch[-1] == "4":
            n=(ui.line_enter.text()).split()
            x = n[0]
            y = n[1]
            counter = 1
            x=int(x)
            while x < int(y):
                x *= 1.1
                counter+=1
            label_small = counter
            ui.label_small.setText(str(label_small))


            
        elif ch[-1] == "5":
            n = (ui.line_enter.text()).split()
            label_small = len(n)
            ui.label_small.setText(str(label_small))



        #elif ch[-1] == "6":
            #ch=0
            #n = (ui.line_enter.text()).split()
            #for i in range(len(n)):
                #n[ch] = int(n[ch])
                #ch+=1
            #label_small = (sum(n)/len(m))
            #ui.label_small.setText(str(label_small))


            
        elif ch[-1] == "7":
            counter = 0
            loopCount = 0
            while True:
                while True:
                    x = int(ui.line_enter.text())
                    if x.isdigit() == False:
                        print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
                    else:
                        break
                x=int(x)
                if x == 0:    
                    break           
                if(loopCount != 0):
                    if(x > container):
                        counter += 1
                container = x
                loopCount+=1
            print(counter)


            
        elif ch[-1] == "8":
            counter = 1
            maxStreak = 0
            loopCount = 0
            while True:
                while True:
                    x = int(ui.line_enter.text())
                    if x.isdigit() == False:
                        print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
                    else:
                       break
                x=int(x)
        
                if x == 0:
                    break
                if(loopCount != 0):
    
                    if(x == container):
                        counter += 1
                    else:
                        if(maxStreak < counter):
                            maxStreak = counter
                        counter = 1
                container = x
                loopCount+=1
            print(max(maxStreak, counter))
            


    ui.button1.clicked.connect(b1)
    ui.button2.clicked.connect(b2)
    ui.button3.clicked.connect(b3)
    ui.button4.clicked.connect(b4)
    ui.button5.clicked.connect(b5)
    ui.button6.clicked.connect(b6)
    ui.button7.clicked.connect(b7)
    ui.button8.clicked.connect(b8)
    
    ui.buttonE.clicked.connect(E)




    
    sys.exit(app.exec_())
