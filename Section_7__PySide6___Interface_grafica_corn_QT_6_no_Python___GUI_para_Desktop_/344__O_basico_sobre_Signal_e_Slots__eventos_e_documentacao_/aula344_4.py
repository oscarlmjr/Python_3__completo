# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

botao1 = QPushButton('Texto do botão 1')
botao1.setStyleSheet('font-size: 60px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner

def outro_slot(checked):
    print('Está marcado?', checked)

def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar)
)

segunda_action = primeiro_menu.addAction('Segunda ação')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)  # type:ignore
segunda_action.hovered.connect(terceiro_slot(segunda_action))  # type:ignore

botao1.clicked.connect(terceiro_slot(segunda_action))  # type:ignore

window.show()
app.exec()  # O loop da aplicação
