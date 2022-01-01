import sys
from PyQt5.QtWidgets import QApplication, QSplitter, QFrame,  QDoubleSpinBox, QComboBox, QPushButton, QMainWindow, QWidget, QDesktopWidget, QLabel, QVBoxLayout, QLineEdit
from PyQt5.QtCore import QTime, Qt
from PyQt5.QtGui import *


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.dateTime = QTime.currentTime()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        frame_1 = QFrame()
        frame_1.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_2 = QFrame()
        frame_2.setFrameShape(QFrame.Panel | QFrame.Sunken)
        frame_3 = QFrame()
        frame_3.setFrameShape(QFrame.Panel | QFrame.Sunken)

        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()
        layout_3 = QVBoxLayout()

        self.statusBar().showMessage(self.dateTime.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle('업비트 자동매매')
        self.resize(500, 300)

        # 텍스트영역
        label1 = QLabel('API key', self)
        label1.move(10, 10)
        label1.setAlignment(Qt.AlignVCenter)
        font1 = label1.font()
        font1.setBold(True)
        label1.setFont(font1)

        label2 = QLabel('종목선택', self)
        label2.move(10, 55)
        label2.setAlignment(Qt.AlignVCenter)
        font2 = label2.font()
        font2.setBold(True)
        label2.setFont(font2)

        label3 = QLabel('주문방식', self)
        label3.move(10, 100)
        label3.setAlignment(Qt.AlignVCenter)
        font3 = label3.font()
        font3.setBold(True)
        label3.setFont(font3)
        # 텍스트영역 끝

        # 문자입력 파트
        qle = QLineEdit(self)
        qle.move(80, 10)
        # 문자입력 파트 끝

        # 버튼 파트
        btn1 = QPushButton('입력', self)
        btn1.move(200, 10)
        # 버튼 파트 끝

        # 종목설정메뉴
        cb1 = QComboBox(self)
        cb1.addItem('KRW-BTC')
        cb1.addItem('KRW-ETH')
        cb1.addItem('KRW-XRP')
        cb1.addItem('KRW-SOL')
        cb1.move(80, 55)

        cb2 = QComboBox(self)
        cb2.addItem('지정가')
        cb2.addItem('시장가')
        cb2.move(80, 100)
        # 종목설정메뉴 끝

        # 로스컷
        label4 = QLabel('로스컷', self)
        label4.move(200, 55)
        label4.setAlignment(Qt.AlignVCenter)
        font4 = label4.font()
        font4.setBold(True)
        label4.setFont(font4)

        dspinbox1 = QDoubleSpinBox(self)
        dspinbox1.setRange(0, 100)
        dspinbox1.setSingleStep(0.01)
        dspinbox1.setPrefix('% ')
        dspinbox1.move(270, 55)
        # 로스컷 끝

        # 익절컷
        label5 = QLabel('익절컷', self)
        label5.move(200, 100)
        label5.setAlignment(Qt.AlignVCenter)
        font5 = label5.font()
        font5.setBold(True)
        label5.setFont(font5)

        dspinbox2 = QDoubleSpinBox(self)
        dspinbox2.setRange(0, 100)
        dspinbox2.setSingleStep(0.01)
        dspinbox2.setPrefix('% ')
        dspinbox2.move(270, 100)
        # 익절컷 끝

        # 슬리피지
        label6 = QLabel('슬리피지', self)
        label6.move(200, 145)
        label6.setAlignment(Qt.AlignVCenter)
        font6 = label6.font()
        font6.setBold(True)
        label6.setFont(font6)
        label6.setToolTip('신호발생 이후 몇 % 이상 높은 가격까지 주문을 허용할 것인지 설정')

        dspinbox3 = QDoubleSpinBox(self)
        dspinbox3.setRange(0, 100)
        dspinbox3.setSingleStep(0.01)
        dspinbox3.setPrefix('% ')
        dspinbox3.move(270, 145)
        dspinbox3.setToolTip('신호발생 이후 몇 % 이상 높은 가격까지 주문을 허용할 것인지 설정')
        # 슬리피지 끝

        # widget 생성
        layout_1.addWidget(label1)
        layout_1.addWidget(qle)
        layout_1.addWidget(btn1)

        layout_2.addWidget(label2)
        layout_2.addWidget(label3)
        layout_2.addWidget(cb1)
        layout_2.addWidget(cb2)

        layout_3.addWidget(label4)  # 로스컷( %)
        layout_3.addWidget(label5)  # 익절컷( %)
        layout_3.addWidget(label6)  # 슬리피지( %)
        layout_3.addWidget(dspinbox1)
        layout_3.addWidget(dspinbox2)
        layout_3.addWidget(dspinbox3)
        # widget 생성 끝

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
