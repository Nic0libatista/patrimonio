
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import sys

class localpatrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # VAMOS CONFIGURAR A GEOMETRIA DA TELA. sETANDO OS VALORES DE POSIÇÃO X E Y ALÉM DE LARGURA E ALTURA
        self.setGeometry(300,300,400,300)

        # UM TEXTO PARA A BARRA DE TITULO
        self.setWindowTitle("cadastrar atualizaçoes do patrimônio")

        # GERENCIADOR DE LAYOUT VERTICAL 
        self.layout_v = QVBoxLayout()
        # HORIZONTAL
        self.layout_h = QHBoxLayout()

        # LABEL

        self.label_id = QLabel("id do produto: ")
        self.label_id.setStyleSheet("QLabel{font-size:12pt} color:pink")

        self.label_serie = QLabel("serie: ")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")

        self.label_data = QLabel("data da ultima verificação: ")
        self.label_data.setStyleSheet("QLabel{font-size:12pt}")

        self.label_observacao = QLabel("número: ")
        self.label_observacao.setStyleSheet("QLabel{font-size:12pt}")

        
        # EDITAVEL
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_data = QLineEdit()
        self.edit_data.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_observacao = QLineEdit()
        self.edit_observacao.setStyleSheet("QLineEdit{font-size:12px}")

    
        # CADASTRO
        self.button = QPushButton("cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red; color:white; font-size:12pt; font-weight:bold;}")

        # CHAMAR A FUNÇÃO CADASTRO DO CLIENTE AO CLICAR NO BOTÃO
        self.button.clicked.connect(self.cadastrar)

        # APARECER NA TELA
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        self.layout_v.addWidget(self.label_data)
        self.layout_v.addWidget(self.edit_data)

        self.layout_v.addWidget(self.label_observacao)
        self.layout_v.addWidget(self.edit_observacao)


        self.layout_v.addWidget(self.button)

        # Adicionando ambos os layouts ao layout principal (vertical)
        self.layout_v.addLayout(self.layout_h)

        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)
      

    def cadastrar(self):
        # print(self.edit_nome.text())
        #VAMOS CRIAR UMA VARIÁVEL QUE FARÁ REFERÊNCIA AO ARQUIVO DE TEXTO
        arquivo = open("clientes.txt","+a",encoding="utf8")
        arquivo.write(f"id: {self.edit_id.text()} \n")
        arquivo.write(f"numero de serie: {self.edit_serie.text()} \n")
        arquivo.write(f"data da ultima verificacao: {self.edit_data.text()} \n")
        arquivo.write(f"observacao: {self.edit_observacao.text()} \n")
        arquivo.write("------------------------------------------------------------------------------------------\n")
        arquivo.close()

app = QApplication(sys.argv)
# NSTANCIA DA CLASSE CADASTROCLIENTE PARA INICIAR A JANELA
tela = localpatrimonio()
# EXIBIR A TELA DURANTE A EXECUÇÃO
tela.show()
# AO CLICAR NO BOTAO FECHAR A TELA DEVE FECHAR A JANELA E SAIR DA MEMORIA
app.exec()

