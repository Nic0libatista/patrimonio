import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import patrimonio
from local import local

class telainicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("clique para abrir a janela ")
        self.button = QPushButton ("abrir patrimonio")
        self.button2= QPushButton ("abrir localização")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)


        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.abrir_local)

        self.setLayout(self.layout_v)
    def abrir_cadastro(self):
        self.pat = patrimonio()
        self.pat.show()

    def abrir_local(self):
        self.pat2 = local()
        self.pat2.show()

app = QApplication(sys.argv)
tela = telainicial()
tela.show()
app.exec()