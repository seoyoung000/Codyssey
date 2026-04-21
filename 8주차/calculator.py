import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 전체 레이아웃 설정
        main_layout = QVBoxLayout()
        
        # 숫자 및 결과가 표시될 창 (QLineEdit)
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet('font-size: 30px; height: 50px; margin-bottom: 10px;')
        main_layout.addWidget(self.display)

        # 버튼 배치 (아이폰 계산기 스타일 배열)
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        grid_layout = QGridLayout()
        
        for row, row_buttons in enumerate(buttons):
            for col, btn_text in enumerate(row_buttons):
                button = QPushButton(btn_text)
                button.setFixedSize(60, 60)
                
                # '0' 버튼은 가로로 두 칸 차지 (아이폰 스타일)
                if btn_text == '0':
                    grid_layout.addWidget(button, row, col, 1, 2)
                elif btn_text == '.' or btn_text == '=':
                    # 0 뒤의 버튼들 위치 조정
                    grid_layout.addWidget(button, row, col + 1)
                else:
                    grid_layout.addWidget(button, row, col)
                
                # 버튼 클릭 이벤트 연결
                button.clicked.connect(self.on_button_clicked)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)
        self.setWindowTitle('iPhone Style Calculator')
        self.show()

    def on_button_clicked(self):
        button = self.sender()
        key = button.text()
        
        # 현재 디스플레이 텍스트
        current_text = self.display.text()

        if key == 'C':
            self.display.setText('0')
        elif key in '0123456789.':
            if current_text == '0':
                self.display.setText(key)
            else:
                self.display.setText(current_text + key)
        # 이번 과제에서 실제 계산 기능(=, +, -, 등)은 구현하지 않음


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec())