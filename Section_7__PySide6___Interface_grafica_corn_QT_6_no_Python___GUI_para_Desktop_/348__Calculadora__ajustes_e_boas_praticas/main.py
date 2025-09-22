import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()

	# Define o ícone
	label1 = QLabel('O meu texto')
	label1.setStyleSheet('font-size: 150px;')
	window.addWidgetToVLayout(label1)

	window.show()
	app.exec()
