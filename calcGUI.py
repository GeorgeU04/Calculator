# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.7.0.dev2404081550
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import ctypes
from ctypes import c_char_p, c_int

class Ui_MainWindow(object):
    @staticmethod
    def check_input(exp):
        left_paren = 0
        right_paren = 0
        operands = 0
        for char in exp:
            if char == "(":
                left_paren += 1
            elif char == ")":
                right_paren += 1
        if left_paren == right_paren:
            return True
        return False

    @staticmethod
    def to_byte_string(py_str):
        return py_str.encode('utf-8') + b'\0'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 468)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setKerning(True)
        self.outputLabel.setFont(font)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setMidLineWidth(1)
        self.outputLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.clear_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("C"))
        self.clear_Button.setGeometry(QtCore.QRect(0, 90, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.clear_Button.setFont(font)
        self.clear_Button.setObjectName("clear_Button")
        self.negative_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("-"))
        self.negative_Button.setGeometry(QtCore.QRect(100, 90, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.negative_Button.setFont(font)
        self.negative_Button.setObjectName("negative_Button")
        self.percent_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("%"))
        self.percent_Button.setGeometry(QtCore.QRect(200, 90, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.percent_Button.setFont(font)
        self.percent_Button.setObjectName("percent_Button")
        self.division_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("/"))
        self.division_Button.setGeometry(QtCore.QRect(300, 90, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.division_Button.setFont(font)
        self.division_Button.setObjectName("division_Button")
        self.eight_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("8"))
        self.eight_button.setGeometry(QtCore.QRect(100, 160, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.nine_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("9"))
        self.nine_button.setGeometry(QtCore.QRect(200, 160, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.multiply_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("*"))
        self.multiply_Button.setGeometry(QtCore.QRect(300, 160, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.multiply_Button.setFont(font)
        self.multiply_Button.setObjectName("multiply_Button")
        self.seven_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("7"))
        self.seven_button.setGeometry(QtCore.QRect(0, 160, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.five_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("5"))
        self.five_button.setGeometry(QtCore.QRect(100, 230, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.six_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("6"))
        self.six_button.setGeometry(QtCore.QRect(200, 230, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.subtract_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("-"))
        self.subtract_Button.setGeometry(QtCore.QRect(300, 230, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.subtract_Button.setFont(font)
        self.subtract_Button.setObjectName("subtract_Button")
        self.four_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("4"))
        self.four_button.setGeometry(QtCore.QRect(0, 230, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.two_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("2"))
        self.two_button.setGeometry(QtCore.QRect(100, 300, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.three_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("3"))
        self.three_button.setGeometry(QtCore.QRect(200, 300, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.add_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("+"))
        self.add_Button.setGeometry(QtCore.QRect(300, 300, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.add_Button.setFont(font)
        self.add_Button.setObjectName("add_Button")
        self.one_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("1"))
        self.one_button.setGeometry(QtCore.QRect(0, 300, 100, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.equal_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("="))
        self.equal_button.setGeometry(QtCore.QRect(319, 370, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.decimal_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("."))
        self.decimal_button.setGeometry(QtCore.QRect(240, 370, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.decimal_button.setFont(font)
        self.decimal_button.setObjectName("decimal_button")
        self.zero_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("0"))
        self.zero_button.setGeometry(QtCore.QRect(0, 370, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.rightparen_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it(")"))
        self.rightparen_Button.setGeometry(QtCore.QRect(170, 370, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.rightparen_Button.setFont(font)
        self.rightparen_Button.setObjectName("rightparen_Button")
        self.leftparen_Button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda : self.press_it("("))
        self.leftparen_Button.setGeometry(QtCore.QRect(100, 370, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.leftparen_Button.setFont(font)
        self.leftparen_Button.setObjectName("leftparen_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self, pressed):
        if pressed == "=" :
            if self.check_input(self.outputLabel.text()): 
                output = eval_function(postfix_function(self.to_byte_string(self.outputLabel.text())))
                self.outputLabel.setText(str(output))       
            else:
                self.outputLabel.setText("Syntax Error")
        elif pressed == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.clear_Button.setText(_translate("MainWindow", "AC"))
        self.negative_Button.setText(_translate("MainWindow", "+/-"))
        self.percent_Button.setText(_translate("MainWindow", "%"))
        self.division_Button.setText(_translate("MainWindow", "/"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.multiply_Button.setText(_translate("MainWindow", "x"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.subtract_Button.setText(_translate("MainWindow", "-"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.add_Button.setText(_translate("MainWindow", "+"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.decimal_button.setText(_translate("MainWindow", "."))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.rightparen_Button.setText(_translate("MainWindow", ")"))
        self.leftparen_Button.setText(_translate("MainWindow", "("))


if __name__ == "__main__":
 # Define the C function and its argument and return types
    calc_lib = ctypes.CDLL("./calculator.so")
    eval_function = calc_lib.eval
    postfix_function = calc_lib.in_to_post
    eval_function.argtypes = [c_char_p]
    eval_function.restype = c_int
    postfix_function.argtypes = [c_char_p]
    postfix_function.restype = c_char_p
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
