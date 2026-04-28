import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


# [Core] 연산 로직을 담당하는 클래스
class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_value = '0'
        self.first_operand = None
        self.operator = None
        self.new_number_start = True

    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            return 'Error'
        return a / b

    def change_sign(self, val):
        if val == '0': return '0'
        return str(-float(val)).replace('.0', '') if float(val) % 1 == 0 else str(-float(val))

    def percent(self, val):
        return str(float(val) / 100)


# [UI] 화면 및 이벤트 연결을 담당하는 클래스
class IPhoneCalculator(QWidget):
    BUTTON_CONFIG = [
        [('AC', 'special'), ('+/-', 'special'), ('%', 'special'), ('/', 'operator')],
        [('7', 'digit'), ('8', 'digit'), ('9', 'digit'), ('*', 'operator')],
        [('4', 'digit'), ('5', 'digit'), ('6', 'digit'), ('-', 'operator')],
        [('1', 'digit'), ('2', 'digit'), ('3', 'digit'), ('+', 'operator')],
        [('0', 'digit'), ('.', 'digit'), ('=', 'operator')]
    ]

    COMMON_STYLE = 'font-size: 24px; border-radius: 30px; border: none; font-weight: bold;'
    STYLES = {
        'digit': f'{COMMON_STYLE} background-color: #333333; color: white;',
        'operator': f'{COMMON_STYLE} background-color: #FF9500; color: white;',
        'special': f'{COMMON_STYLE} background-color: #A5A5A5; color: black;',
        'display': 'font-size: 60px; color: white; background-color: black; border: none; padding-right: 15px;'
    }

    def __init__(self):
        super().__init__()
        self.calc_core = Calculator()  # 계산기 심장(로직) 장착
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet('background-color: black;')
        main_layout = QVBoxLayout()
        
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet(self.STYLES['display'])
        main_layout.addWidget(self.display)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)
        self.__create_buttons()
        main_layout.addLayout(self.grid_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('iPhone Calculator')
        self.setFixedSize(320, 500)
        self.show()

    def __create_buttons(self):
        for row, row_buttons in enumerate(self.BUTTON_CONFIG):
            col_offset = 0
            for col, (btn_text, style_key) in enumerate(row_buttons):
                button = QPushButton(btn_text)
                if btn_text == '0':
                    button.setFixedSize(135, 60)
                    self.grid_layout.addWidget(button, row, col + col_offset, 1, 2)
                    col_offset = 1
                else:
                    button.setFixedSize(60, 60)
                    self.grid_layout.addWidget(button, row, col + col_offset)
                
                button.setStyleSheet(self.STYLES[style_key])
                button.clicked.connect(self.handle_click)

    def handle_click(self):
        key = self.sender().text()
        display_val = self.display.text()

        # 1. 숫자 및 소수점 처리
        if key.isdigit() or key == '.':
            if self.calc_core.new_number_start:
                new_val = key if key != '.' else '0.'
                self.calc_core.new_number_start = False
            else:
                if key == '.' and '.' in display_val: return # 소수점 중복 방지
                new_val = display_val + key
            self.display.setText(new_val)

        # 2. 기능 버튼 처리
        elif key == 'AC':
            self.calc_core.reset()
            self.display.setText('0')
        elif key == '+/-':
            self.display.setText(self.calc_core.change_sign(display_val))
        elif key == '%':
            self.display.setText(self.calc_core.percent(display_val))

        # 3. 연산자 및 결과 처리
        elif key in ['+', '-', '*', '/']:
            self.calc_core.first_operand = float(display_val)
            self.calc_core.operator = key
            self.calc_core.new_number_start = True
        elif key == '=':
            if self.calc_core.operator:
                second_operand = float(display_val)
                ops = {
                    '+': self.calc_core.add, '-': self.calc_core.subtract,
                    '*': self.calc_core.multiply, '/': self.calc_core.divide
                }
                result = ops[self.calc_core.operator](self.calc_core.first_operand, second_operand)
                
                # 에러(0으로 나누기 등) 처리
                if result == 'Error':
                    self.display.setText('Error')
                else:
                    # 정수면 소수점 제거, 아니면 유지
                    formatted_res = str(result).replace('.0', '') if result % 1 == 0 else f'{result:.8g}'
                    self.display.setText(formatted_res)
                
                self.calc_core.reset()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = IPhoneCalculator()
    sys.exit(app.exec())