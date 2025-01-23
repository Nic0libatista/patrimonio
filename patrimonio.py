from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import sys

class patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # VAMOS CONFIGURAR A GEOMETRIA DA TELA. sETANDO OS VALORES DE POSIÇÃO X E Y ALÉM DE LARGURA E ALTURA
        self.setGeometry(300,300,400,300)

        # UM TEXTO PARA A BARRA DE TITULO
        self.setWindowTitle("cadastrar patrimônio")

        # GERENCIADOR DE LAYOUT VERTICAL 
        self.layout_v = QVBoxLayout()
        # HORIZONTAL
        self.layout_h = QHBoxLayout()

        # LABEL

        self.label_id = QLabel("id do produto: ")
        self.label_id.setStyleSheet("QLabel{font-size:12pt} color:pink")

        self.label_serie = QLabel("número de série do produto: ")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")

        self.label_nome = QLabel("nome do patrimônio: ")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")

        self.label_tipo = QLabel("tipo: ")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        self.label_descricao = QLabel("descrição: ")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")

        self.label_local = QLabel("localização: ")
        self.label_local.setStyleSheet("QLabel{font-size:12pt}")

        self.label_fabricacao = QLabel("Data de fabricação: ")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:12pt}")

        self.label_aquisicao = QLabel("Data de aquisição: ")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:12pt}")

        # EDITAVEL
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_aquisicao = QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12px}")

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

        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        self.layout_v.addWidget(self.label_local)
        self.layout_v.addWidget(self.edit_local)

        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_fabricacao)

        self.layout_v.addWidget(self.label_aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)

        self.layout_v.addWidget(self.button)


        # self.layout_h.addWidget(QLabel("Layout Secundário:"))
        # self.layout_h.addWidget(self.edit_local)


        

        # Adicionando ambos os layouts ao layout principal (vertical)
        self.layout_v.addLayout(self.layout_h)

        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)
      

    def cadastrar(self):
        # print(self.edit_nome.text())
        #VAMOS CRIAR UMA VARIÁVEL QUE FARÁ REFERÊNCIA AO ARQUIVO DE TEXTO
        arquivo = open("clientes.txt","+a")
        arquivo.write(f"id: {self.edit_id.text()} \n")
        arquivo.write(f"numero de serie: {self.edit_serie.text()} \n")
        arquivo.write(f"nome do patrimonio: {self.edit_nome.text()} \n")
        arquivo.write(f"tipo: {self.edit_tipo.text()} \n")
        arquivo.write(f"descricao: {self.edit_descricao.text()} \n")
        arquivo.write(f"localizacao: {self.edit_local.text()} \n")
        arquivo.write(f"data de fabricacao: {self.edit_fabricacao.text()} \n")
        arquivo.write(f"data de aquisicao: {self.edit_aquisicao.text()} \n")
        arquivo.write("------------------------------------------------------------------------------------------\n")
        arquivo.close()

app = QApplication(sys.argv)
# NSTANCIA DA CLASSE CADASTROCLIENTE PARA INICIAR A JANELA
tela = patrimonio()
# EXIBIR A TELA DURANTE A EXECUÇÃO
tela.show()
# AO CLICAR NO BOTAO FECHAR A TELA DEVE FECHAR A JANELA E SAIR DA MEMORIA
app.exec()

