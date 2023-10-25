from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QFormLayout, QTabWidget, QLineEdit, QLabel, QPushButton
from PySide6.QtGui import Qt, QPixmap, QMouseEvent
from PySide6.QtCore import QSize, QPoint
import usefull_functions as uf
import algorithms as alg       

"""
Brief: Creat a new widget to show a message in program.
"""
class MessageBox(QWidget):
    def __init__(self, txt: str):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        info = QLabel(txt)
        info_line = QHBoxLayout()
        info_line.addWidget(info)
        info_line.setContentsMargins(5, 5, 5, 5)
        button_line = QHBoxLayout()
        button = QPushButton("Ok")
        button_line.addWidget(button)
        whole_window = QVBoxLayout()
        whole_window.addLayout(info_line)
        whole_window.addLayout(button_line)
        self.setLayout(whole_window)
        self.load_style()

        # Signals:
        button.clicked.connect(self.quit_window)

    # Load style symilar to main window.
    def load_style(self):

        style_sheet = """

QWidget {
    background-color: #001449;
    color: white;
}

QPushButton {
    background-color: #005bc5;
    color: white;
    width: 25px;
    font-size: 18px;
}

QLabel {
    font-size: 18px;
}
"""
        self.setStyleSheet(style_sheet)
    
    def quit_window(self):
        self.close()
    
    # Detecting an event of pressing mouse.
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.old_position = event.globalPos()
    
    # Move window with mouse.
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.delta_to_change = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + self.delta_to_change.x(), self.y() + self.delta_to_change.y())
        self.old_position = event.globalPos()


class Main_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        icon = QPixmap("images\window_icon.png")
        self.setWindowIcon(icon)

        # Creat title bar.
        self.title_bar = QHBoxLayout()
        self.title_bar.setContentsMargins(5, 0, 0, 5)
        self.title_bar.setSpacing(5)

        # Title icon:
        icon_label = QLabel()
        icon_label.setPixmap(icon)
        icon_label.setMaximumSize(QSize(10, 28))

        # Title:
        title = QLabel("Pediatric dose's calculator", objectName="title")

        self.title_bar.addWidget(icon_label)
        self.title_bar.addWidget(title)

        self.minimalize_button = QPushButton("_", objectName="minimize")
        self.exit_button = QPushButton("X", objectName="exit_button")
        title_bar_buttons = QHBoxLayout()

        title_bar_buttons.addWidget(self.minimalize_button)
        title_bar_buttons.addWidget(self.exit_button)
        title_bar_buttons.setContentsMargins(0, 0, 0, 0)
        title_bar_buttons.setSpacing(0)

        self.title_bar.addLayout(title_bar_buttons)


        # Tabs layout:
        self.tab = QTabWidget()
        self.load_style_sheet()

        # Creat tab 1:
        self.frieds_widget = QWidget()
        lines = QFormLayout()
        first_label = QLabel("Child age (months):")
        self.frieds_first_data = QLineEdit()
        lines.addRow(first_label, self.frieds_first_data)
        
        second_label = QLabel("Dose for adult:")
        self.frieds_second_data = QLineEdit()
        lines.addRow(second_label, self.frieds_second_data)

        self.frieds_calculate_button = QPushButton("Calculate dose")
        lines.addWidget(self.frieds_calculate_button)
        
        result_label = QLabel("Dose for child:")
        self.frieds_result_data = QLineEdit()
        self.frieds_copy_button = QPushButton("Copy")
        result_line = QHBoxLayout()
        result_line.addWidget(self.frieds_result_data)
        result_line.addWidget(self.frieds_copy_button)
        lines.addRow(result_label, result_line)

        self.frieds_widget.setLayout(lines)
        self.tab.addTab(self.frieds_widget, "Frieds's")

        # Creat tab 2
        cowlings_widget = QWidget()
        lines = QFormLayout()
        first_label = QLabel("Child age (years):")
        self.cowlings_first_data = QLineEdit()
        lines.addRow(first_label, self.cowlings_first_data)
        
        second_label = QLabel("Dose for adult:")
        self.cowlings_second_data = QLineEdit()
        lines.addRow(second_label, self.cowlings_second_data)

        self.cowlings_calculate_button = QPushButton("Calculate dose")
        lines.addWidget(self.cowlings_calculate_button)
        
        result_label = QLabel("Dose for child:")
        self.cowlings_result_data = QLineEdit()
        self.cowlings_copy_button = QPushButton("Copy")
        result_line = QHBoxLayout()
        result_line.addWidget(self.cowlings_result_data)
        result_line.addWidget(self.cowlings_copy_button)
        lines.addRow(result_label, result_line)

        cowlings_widget.setLayout(lines)
        self.tab.addTab(cowlings_widget, "Cowling's")

        # Creat tab 3
        youngs_widget = QWidget()
        lines = QFormLayout()
        first_label = QLabel("Child age (years):")
        self.youngs_first_data = QLineEdit()
        lines.addRow(first_label, self.youngs_first_data)
        
        second_label = QLabel("Dose for adult:")
        self.youngs_second_data = QLineEdit()
        lines.addRow(second_label, self.youngs_second_data)

        self.youngs_calculate_button = QPushButton("Calculate dose")
        lines.addWidget(self.youngs_calculate_button)
        
        result_label = QLabel("Dose for child:")
        self.youngs_result_data = QLineEdit()
        self.youngs_copy_button = QPushButton("Copy")
        result_line = QHBoxLayout()
        result_line.addWidget(self.youngs_result_data)
        result_line.addWidget(self.youngs_copy_button)
        lines.addRow(result_label, result_line)

        youngs_widget.setLayout(lines)
        self.tab.addTab(youngs_widget, "Young's")

        # Creat tab 4
        clarks_widget = QWidget()
        lines = QFormLayout()
        first_label = QLabel("Child's age (years):")
        self.clarks_first_data = QLineEdit()
        lines.addRow(first_label, self.clarks_first_data)
        
        second_label = QLabel("Dose for adult:")
        self.clarks_second_data = QLineEdit()
        lines.addRow(second_label, self.clarks_second_data)

        third_label = QLabel("Child weight (kg):")
        self.clarks_third_data = QLineEdit()
        lines.addRow(third_label, self.clarks_third_data)

        self.clarks_calculate_button = QPushButton("Calculate dose")
        lines.addWidget(self.clarks_calculate_button)
        
        result_label = QLabel("Dose for child:")
        self.clarks_result_data = QLineEdit()
        self.clarks_copy_button = QPushButton("Copy")
        result_line = QHBoxLayout()
        result_line.addWidget(self.clarks_result_data)
        result_line.addWidget(self.clarks_copy_button)
        lines.addRow(result_label, result_line)

        clarks_widget.setLayout(lines)
        self.tab.addTab(clarks_widget, "Clark's")

        # Creat tab 5
        skin_surface_widget = QWidget()
        lines = QFormLayout()
        first_label = QLabel("Child's age (years):")
        self.skin_surface_first_data = QLineEdit()
        lines.addRow(first_label, self.skin_surface_first_data)
        
        second_label = QLabel("Dose for adult:")
        self.skin_surface_second_data = QLineEdit()
        lines.addRow(second_label, self.skin_surface_second_data)

        third_label = QLabel("Surface of child skin (m²):")
        self.skin_surface_third_data = QLineEdit()
        lines.addRow(third_label, self.skin_surface_third_data)

        self.skin_surface_calculate_button = QPushButton("Calculate dose")
        lines.addWidget(self.skin_surface_calculate_button)
        
        result_label = QLabel("Dose for child:")
        self.skin_surface_result_data = QLineEdit()
        self.skin_surface_copy_button = QPushButton("Copy")
        result_line = QHBoxLayout()
        result_line.addWidget(self.skin_surface_result_data)
        result_line.addWidget(self.skin_surface_copy_button)
        lines.addRow(result_label, result_line)

        skin_surface_widget.setLayout(lines)
        self.tab.addTab(skin_surface_widget, "Skin surface")

        tabs = QVBoxLayout(objectName="tabs")
        tabs.addWidget(self.tab)

        self.whole_window = QGridLayout()
        self.whole_window.addLayout(self.title_bar, 0, 0)
        self.whole_window.addLayout(tabs, 1, 0)
        self.whole_window.setContentsMargins(0, 0, 0, 0)
        self.whole_window.setSpacing(0)

        self.setLayout(self.whole_window)

        self.previous_tab_index = self.tab.currentIndex()
        self.actual_tab_index = self.tab.currentIndex()

        # Signals:
        self.minimalize_button.clicked.connect(self.minimalize_window)
        self.exit_button.clicked.connect(self.quit_application)
        self.frieds_calculate_button.clicked.connect(self.gather_data)
        self.cowlings_calculate_button.clicked.connect(self.gather_data)
        self.youngs_calculate_button.clicked.connect(self.gather_data)
        self.clarks_calculate_button.clicked.connect(self.gather_data)
        self.skin_surface_calculate_button.clicked.connect(self.gather_data)
        self.tab.currentChanged.connect(self.clean_inputs)
        self.frieds_copy_button.clicked.connect(self.copy_result_line)
        self.cowlings_copy_button.clicked.connect(self.copy_result_line)
        self.youngs_copy_button.clicked.connect(self.copy_result_line)
        self.clarks_copy_button.clicked.connect(self.copy_result_line)
        self.skin_surface_copy_button.clicked.connect(self.copy_result_line)

        self.load_style_sheet()

    # Gather data from QLineEdit's objects from actual active tab.
    def gather_data(self):
        self.actual_tab = self.tab.currentIndex()

        if self.actual_tab == 0:
            self.first_input = uf.isNumber(self.frieds_first_data.text())
            self.second_input = uf.isNumber(self.frieds_second_data.text())

            if self.check_inputs() is False:
                return 0
            
            # Protection before wrong input:
            if self.first_input > 12:
                self.warning = MessageBox("You can't use the frieds pattern to calculate dose for child older than one year.")
                self.warning.show()
                return 0
            
            result = alg.frieds_dose_pattern(self.first_input, self.second_input)
            self.frieds_result_data.setText(str(result))

        elif self.actual_tab == 1:
            self.first_input = uf.isNumber(self.cowlings_first_data.text())
            self.second_input = uf.isNumber(self.cowlings_second_data.text())

            if self.check_inputs() is False:
                return 0

            if self.first_input >= 2:
                self.warning = MessageBox("You can use the Cowling's pattern to calculate dose only for child younger than two years old.")
                self.warning.show()
                return 0
            
            self.cowlings_result_data.setText(str(alg.cowlings_dose_pattern(self.first_input, self.second_input)))

        elif self.actual_tab == 2:
            self.first_input = uf.isNumber(self.youngs_first_data.text())
            self.second_input = uf.isNumber(self.youngs_second_data.text())

            if self.check_inputs() is False:
                return 0

            if self.first_input < 2 or self.first_input > 12:
                self.warning = MessageBox("You can use the Young's pattern to calculate dose only for child from 2 to 12 years old.")
                self.warning.show()
                return 0
            
            self.youngs_result_data.setText(str(alg.youngs_dose_pattern(self.first_input, self.second_input)))

        elif self.actual_tab == 3:
            self.first_input = uf.isNumber(self.clarks_first_data.text())
            self.second_input = uf.isNumber(self.clarks_second_data.text())
            self.third_input = uf.isNumber(self.clarks_third_data.text())

            # Input protection:
            if self.check_inputs() is False:
                return 0

            if self.first_input < 2 or self.first_input >= 18:
                self.warning = MessageBox("You can use Clark's pattern for child in age above 2 years.")
                self.warning.show()
                return 0
            
            self.clarks_result_data.setText(str(alg.clarks_dose_pattern(self.second_input, self.third_input)))

        elif self.actual_tab == 4:
            self.first_input = uf.isNumber(self.skin_surface_first_data.text())
            self.second_input = uf.isNumber(self.skin_surface_second_data.text())
            self.third_input = uf.isNumber(self.skin_surface_third_data.text())

            # Input protection:
            if self.check_inputs() is False:
                return 0

            if self.first_input <= 2:
                self.warning = MessageBox("You can use skin surface pattern for child in age above 2 years.")
                self.warning.show()
                return 0
            
            self.skin_surface_result_data.setText(str(alg.skin_surface_dose_pattern(self.second_input, self.third_input)))

    # User's inputs protection.
    def check_inputs(self):

        if type(self.first_input) is bool or type(self.second_input) is bool:
            self.warning = MessageBox("You have to pass a positive numbers.")
            self.warning.show()
            return False
            
        if len(self.first_input) == 0 or len(self.second_input) == 0:
            self.warning = MessageBox("You have to pass a data.")
            self.warning.show()
            return False
        
        self.first_input = float(self.first_input)
        self.second_input = float(self.second_input)

        if self.actual_tab > 2:
            if type(self.third_input) is bool:
                self.warning = MessageBox("You have to pass a numbers.")
                self.warning.show()
                return False
            
            if len(self.third_input) == 0:
                self.warning = MessageBox("You have to pass a data.")
                self.warning.show()
                return False
            
            self.third_input = float(self.third_input)

    # Clean a content from QLineEdit's object of recent active tab.
    def clean_inputs(self):

        self.actual_tab_index = self.tab.currentIndex()

        
        if self.previous_tab_index == 0:
            self.frieds_first_data.setText("")
            self.frieds_second_data.setText("")
            self.frieds_result_data.setText("")
        elif self.previous_tab_index == 1:
            self.cowlings_first_data.setText("")
            self.cowlings_second_data.setText("")
            self.cowlings_result_data.setText("")
        elif self.previous_tab_index == 2:
            self.youngs_first_data.setText("")
            self.youngs_second_data.setText("")
            self.youngs_result_data.setText("")
        elif self.previous_tab_index == 3:
            self.clarks_first_data.setText("")
            self.clarks_second_data.setText("")
            self.clarks_third_data.setText("")
            self.clarks_result_data.setText("")
        elif self.previous_tab_index == 4:
            self.skin_surface_first_data.setText("")
            self.skin_surface_second_data.setText("")
            self.skin_surface_third_data.setText("")
            self.skin_surface_result_data.setText("")
        
        self.previous_tab_index = self.actual_tab_index

    # Load stylesheet for main window.
    def load_style_sheet(self):

        self.main_style_sheet = """

QWidget {
    background-color: #001449;
    color: white;
}

QPushButton {
    background-color: #005bc5;
    color: white;
    width: 25px;
    font-size: 18px;
}

QPushButton#minimize {
    background-color: #001449;
    border: 0px;
    padding: 5px;
    margin: 0px;
    font-weight: bold;
}

QPushButton#minimize:hover {
    background-color: #005bc5;
    width: 25px;
}

QPushButton#exit_button {
    background-color: #001449;
    width: 25px;
    border: 0px;
    padding: 5px;
    margin: 0px;
    font-weight: bold;
}

QPushButton#exit_button:hover {
    background-color: red;
}

QLineEdit {
    background-color: #17f9ff;
    color: black;
    font-size: 18px;
}

QTabBar::tab {
    background-color: #005bc5;
    color: white;
    padding: 4px;
    border: 3px solid #001449;
    font-size: 18px;
    font-weight: bold;
}

QTabWidget::pane {
    border 0;
}

QTabBar::tab:selected {
    background-color: #00b4fc;
    color: black;
    margin-left: 5px;
}

QLabel {
    font-size: 18px;
}

QLabel#title {
    font-weight: bold;
    padding: 5px;
}
"""
        self.setStyleSheet(self.main_style_sheet)
    
    # Slots:
    def quit_application(self):
        self.close()

    def minimalize_window(self):
        self.showMinimized()
    
    # Copy data from result dose QLineEdit's object from active tab.
    def copy_result_line(self):
        if self.actual_tab_index == 0:
            self.frieds_result_data.selectAll()
            self.frieds_result_data.copy()
        elif self.actual_tab_index == 1:
            self.cowlings_result_data.selectAll()
            self.cowlings_result_data.copy()
        elif self.actual_tab_index == 2:
            self.youngs_result_data.selectAll()
            self.youngs_result_data.copy()
        elif self.actual_tab_index == 3:
            self.clarks_result_data.selectAll()
            self.clarks_result_data.copy()
        elif self.actual_tab_index == 4:
            self.skin_surface_result_data.selectAll()
            self.skin_surface_result_data.copy()
        else:
            return 1

    # Detecting an event of pressing mouse.
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.old_position = event.globalPos()
    
    # Move window with mouse.
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
       self.actual_position = QPoint(event.globalPos() - self.old_position)
       self.move(self.x() + self.actual_position.x(), self.y() + self.actual_position.y())
       self.old_position = event.globalPos()

