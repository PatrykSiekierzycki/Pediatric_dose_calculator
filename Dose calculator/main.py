from PySide6.QtWidgets import QApplication
from widgets import Main_window
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Main_window()
    main_window.show()
    app.exec()

