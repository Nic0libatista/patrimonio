from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sys

class local(QWidget):
    def __init__(self):
        super().__init__()

        # VAMOS CONFIGURAR A GEOMETRIA DA TELA. sETANDO OS VALORES DE POSIÇÃO X E Y ALÉM DE LARGURA E ALTURA
        self.setGeometry(300,300,400,300)

        # UM TEXTO PARA A BARRA DE TITULO
        self.setWindowTitle("cadastrar localizações do patrimônio")

        # GERENCIADOR DE LAYOUT VERTICAL 
        self.layout_v = QVBoxLayout()
        # HORIZONTAL
        self.layout_h = QHBoxLayout()

        # LABEL

        self.label_id = QLabel("id do produto: ")
        self.label_id.setStyleSheet("QLabel{font-size:12pt} color:pink")

        self.label_empresa = QLabel("Empresa: ")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")

        self.label_logradouro = QLabel("logradouro: ")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt}")

        self.label_numero = QLabel("número: ")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")

        self.label_predio = QLabel("predio: ")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt}")

        self.label_andar = QLabel("andar: ")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")

        self.label_sala = QLabel("sala: ")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")

        
        # EDITAVEL
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12px}")

    
        # CADASTRO
        self.button = QPushButton("cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red; color:white; font-size:12pt; font-weight:bold;}")

        # CHAMAR A FUNÇÃO CADASTRO DO CLIENTE AO CLICAR NO BOTÃO
        self.button.clicked.connect(self.cadastrar)

        # APARECER NA TELA
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)

        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)

        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)

        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

    

        self.layout_v.addWidget(self.button)



       # self.layout_h.addWidget(QLabel("Layout Secundário:"))
        # self.layout_h.addWidget(self.edit_local)


        

        # Adicionando ambos os layouts ao layout principal (vertical)
        self.layout_v.addLayout(self.layout_h)

        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)
      

    def cadastrar(self):
        if (self.edit_id.text()=="" or self.edit_empresa.text()=="" or self.edit_logradouro.text()=="" or self.edit_numero.text()=="" or self.edit_predio.text()=="" or self.edit_andar.text()=="" or self.edit_sala.text()==""):
            QMessageBox.critical(self,"erro","Você deve preencher todos os campos")
        else:
            # print(self.edit_nome.text())
            #VAMOS CRIAR UMA VARIÁVEL QUE FARÁ REFERÊNCIA AO ARQUIVO DE TEXTO
            arquivo = open("local.txt","+a",encoding="utf8")
            arquivo.write(f"id: {self.edit_id.text()} \n")
            arquivo.write(f"empresa: {self.edit_empresa.text()} \n")
            arquivo.write(f"nome do patrimonio: {self.edit_logradouro.text()} \n")
            arquivo.write(f"tipo: {self.edit_numero.text()} \n")
            arquivo.write(f"descricao: {self.edit_predio.text()} \n")
            arquivo.write(f"localizacao: {self.edit_andar.text()} \n")
            arquivo.write(f"data de fabricacao: {self.edit_sala.text()} \n")
            arquivo.write("------------------------------------------------------------------------------------------\n")
            arquivo.close()
            QMessageBox.information(self,"Cadastrado com sucesso","Os dados da localização foram salvos")

#app = QApplication(sys.argv)
# NSTANCIA DA CLASSE CADASTROCLIENTE PARA INICIAR A JANELA
#tela = localpatrimonio()
# EXIBIR A TELA DURANTE A EXECUÇÃO
#tela.show()
# AO CLICAR NO BOTAO FECHAR A TELA DEVE FECHAR A JANELA E SAIR DA MEMORIA
#app.exec()

