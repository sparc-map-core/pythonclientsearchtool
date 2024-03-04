import sys

from PySide6.QtWidgets import QApplication

from retrieveportaldatawidget import RetrievePortalDataWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = RetrievePortalDataWidget()
    widget.show()
    sys.exit(app.exec())
