import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow
import math
from Ui_MainWindow2 import Ui_MainWindow


def calculation_error_messageBox():
    messageBox = QMessageBox()
    messageBox.setWindowTitle("არასწორი პარამეტრები")
    messageBox.setText("გთხოვთ შეიყვანოთ 0-სგან განსხვავებული ციფრები ფიგურის ფართობის გამოსათვლელად")
    messageBox.setIcon(QMessageBox.Warning)
    messageBox.exec_()


def not_equal_sides_error_messageBox():
    messageBox = QMessageBox()
    messageBox.setWindowTitle("არასწორი პარამეტრები")
    messageBox.setText("გთხოვთ შეიყვანოთ თანაბარი კვადრატის გერდები")
    messageBox.setIcon(QMessageBox.Warning)
    messageBox.exec_()


def equal_sides_error_messageBox():
    messageBox = QMessageBox()
    messageBox.setWindowTitle("არასწორი პარამეტრები")
    messageBox.setText("გთხოვთ შეიყვანოთ არათანაბარი გერდები")
    messageBox.setIcon(QMessageBox.Warning)
    messageBox.exec_()


class MyWindow:
    def __init__(self):
        self.window = QMainWindow()
        self.initUI = Ui_MainWindow()
        self.initUI.setupUi(self.window)

        # Main Page
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Home_Page)

        # Displays selected Page
        self.initUI.radioButton_Triangle.clicked.connect(self.Triangle_Page)
        self.initUI.radioButton_Square.clicked.connect(self.Square_Page)
        self.initUI.radioButton_Rectangle.clicked.connect(self.Rectangle_Page)
        self.initUI.radioButton_Trapezium.clicked.connect(self.Trapezium_Area_Page)
        self.initUI.pushButton.clicked.connect(self.fromTrapeziumAreaToPerimeterButton)

        # Displays return from selected Page to home page
        self.initUI.pushButton_Return_Back_from_Trianglw_Page_to_Main.clicked.connect(self.homePage)
        self.initUI.pushButton_Return_Back_from_Square_Page_to_Main.clicked.connect(self.homePage)
        self.initUI.pushButton_Return_Back_from_Rectangle_to_Main.clicked.connect(self.homePage)
        self.initUI.pushButton_Return_Back_TrapeziumArea_To_Main.clicked.connect(self.homePage)
        self.initUI.pushButton_Return_Back_TrapeziumPerimeterPage_To_Main.clicked.connect(self.Trapezium_Area_Page)

        # Outputs calculation of each figure
        self.initUI.pushButton_Calculate_For_Triangle.clicked.connect(self.triangleCalculator)
        self.initUI.pushButton_Calculate_For_Rectangle.clicked.connect(self.rectangleCalculator)
        self.initUI.pushButton_Calculate_For_Square.clicked.connect(self.squareCalculator)
        self.initUI.pushButton_Calculate_Trapezium_area.clicked.connect(self.trapeziumAreaCalculator)
        self.initUI.pushButton_Calculate_Trapezium_Perimeter.clicked.connect(self.trapeziumPerimeterCalculator)

    # Show's selected page
    def showSelectedPage(self):
        if self.initUI.radioButton_Rectangle.isChecked():
            self.Rectangle_Page()
        elif self.initUI.radioButton_Square.isChecked():
            self.Square_Page()
        elif self.initUI.radioButton_Triangle.isChecked():
            self.Triangle_Page()
        elif self.initUI.radioButton_Trapezium.isChecked():
            self.Trapezium_Area_Page()

    def homePage(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Home_Page)

    def Rectangle_Page(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Rectangle_Page)

    def Square_Page(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Square_Page)

    def Triangle_Page(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Triangle_Page)

    def Trapezium_Area_Page(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Trapezium_Page)

    def backToTheMainPage(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Home_Page)

    def fromTrapeziumAreaToPerimeterButton(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Trapezium_Perimeter_page)

    def triangleCalculator(self):
        triangle_side1 = float(self.initUI.first_side_Of_Triangle.text())
        triangle_side2 = float(self.initUI.Second_side_Of_Triangle.text())
        triangle_side3 = float(self.initUI.Third_side_Of_Triangle.text())

        if triangle_side1 == 0 or triangle_side2 == 0 or triangle_side3 == 0:
            calculation_error_messageBox()
        else:
            half_perimeter = (triangle_side1 + triangle_side2 + triangle_side3) / 2
            area = math.sqrt(half_perimeter * (half_perimeter - triangle_side1) * (half_perimeter - triangle_side2) * (
                        half_perimeter - triangle_side3))
            perimeter = triangle_side1 + triangle_side2 + triangle_side3

            self.initUI.Triangel_perimeter.display(perimeter)
            self.initUI.Triangle_area.display(area)

    def squareCalculator(self):
        square_side1 = float(self.initUI.Firts_side_Of_Square.text())
        square_side2 = float(self.initUI.Second_side_Of_Square.text())
        if square_side1 == 0 or square_side2 == 0:
            calculation_error_messageBox()
        elif square_side1 != square_side2:
            not_equal_sides_error_messageBox()
        else:
            square_area = square_side1 * square_side2
            square_perimeter = (square_side1 + square_side2) * 2

            self.initUI.Square_Perimeter.display(square_perimeter)
            self.initUI.Square_Area.display(square_area)

    def rectangleCalculator(self):
        rectangle_side1 = float(self.initUI.First_side_Of_Rectangle.text())
        rectangle_side2 = float(self.initUI.Second_side_Of_Rectangle.text())

        if rectangle_side1 == 0 or rectangle_side2 == 0:
            calculation_error_messageBox()
        elif rectangle_side1 == rectangle_side2:
            equal_sides_error_messageBox()
        else:
            rectangle_area = rectangle_side1 * rectangle_side2
            rectangle_perimeter = (rectangle_side1 * 2) + (rectangle_side2 * 2)

            self.initUI.Rectangle_perimeter.display(rectangle_perimeter)
            self.initUI.Rectangle_area.display(rectangle_area)

    def trapeziumAreaCalculator(self):
        trapezium_side1 = float(self.initUI.First_side_Of_Trapezium.text())
        trapezium_side2 = float(self.initUI.Second_side_Of_Trapezium.text())
        trapezium_height = float(self.initUI.Thierd_side_Of_Trapezium.text())

        if trapezium_side1 == 0 or trapezium_side2 == 0 or trapezium_height == 0:
            calculation_error_messageBox()
        else:
            trapezium_area = ((trapezium_side1 + trapezium_side2) / 2) * trapezium_height
            self.initUI.Trapezium_area.display(trapezium_area)

    def trapeziumPerimeterCalculator(self):
        trapezium_side1 = float(self.initUI.First_side_Of_Trapezium_1.text())
        trapezium_side2 = float(self.initUI.Second_side_Of_Trapezium_2.text())
        trapezium_side3 = float(self.initUI.First_ferd_Of_Trapezium.text())
        trapezium_side4 = float(self.initUI.Second_ferd_Of_Trapezium.text())

        if trapezium_side1 == 0 or trapezium_side2 == 0 or trapezium_side3 == 0 or trapezium_side4 == 0:
            calculation_error_messageBox()
        else:
            trapezium_perimeter = trapezium_side1 + trapezium_side2 + trapezium_side3 + trapezium_side4
            self.initUI.Trapezium_perimeter.display(trapezium_perimeter)

    def show(self):
        self.window.show()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(application.exec_())
