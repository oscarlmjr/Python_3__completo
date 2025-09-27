# from PySide6.QtCore import Qt
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
	eqRequested = Signal()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.configStyle()

	def configStyle(self):
		margins = [TEXT_MARGIN for _ in range(4)]
		self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
		self.setMinimumHeight(BIG_FONT_SIZE * 2)
		self.setMinimumWidth(MINIMUM_WIDTH)
		self.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.setTextMargins(*margins)

	def keyPressEvent(self, event: QKeyEvent) -> None:
		# print(event.text())
		# print(event.key())
		key = event.key()
		KEYS = Qt.Key

		isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]

		# if key == '':
		# # if key == KEYS.Key_Enter:
		if isEnter:
			print('Enter pressionado, sinal emitido', type(self).__name__)
			self.eqRequested.emit()
			return event.ignore()

		# return super().keyPressEvent(event)

