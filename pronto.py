
from tkinter import *
from tkinter import messagebox


def impDados():
    print("Enviado")

#cofigurar tela principal
menu_inicial= Tk()

         #

       
         #
menu_inicial.title('Controle de Estoque')
menu_inicial.geometry('700x200+260+200')
menu_inicial.state('zoomed')#abrir a app em tela cheia
menu_inicial.iconbitmap("img/icon.ico")#trabalhar com o icone
menu_inicial['bg']='blue'
menu_inicial.minsize(width=650, height=380)
my_menu=Menu(menu_inicial)
menu_inicial.config(menu=my_menu)

img=PhotoImage(file="img/marca_new.png")
label_imagem=Label(menu_inicial, image=img).pack()

#ABA 1.2

def consultarestoque():
    estoque_consulta=Tk() 
    estoque_consulta.title('Consultar Estoque')
    estoque_consulta.geometry('700x200+250+400')
    estoque_consulta.state('zoomed')
    estoque_consulta.iconbitmap("img/icon.ico")
    estoque_consulta['bg']='red'
    

    Label(estoque_consulta,text='Id Produto', background='red', foreground='black', anchor=W).place(x=1,y=30,width=120,height=20)
    Label(estoque_consulta,text='Nome Produto', background='red', foreground='black', anchor=W).place(x=1,y=60,width=100,height=20)
    Label(estoque_consulta,text='Status Produto', background='red', foreground='black', anchor=W).place(x=1,y=90,width=105,height=20)
    Label(estoque_consulta,text='Status de Solicitacao', background='red', foreground='black', anchor=W).place(x=1,y=120,width=120,height=20)
    Label(estoque_consulta,text='Qualidade', background='red', foreground='black', anchor=W).place(x=1,y=150,width=100,height=20)
    Label(estoque_consulta,text='Data de Saida ', background='red', foreground='black', anchor=W).place(x=1,y=180,width=105,height=20)
    Label(estoque_consulta,text='Qtd solicitada ', background='red', foreground='black', anchor=W).place(x=1,y=210,width=120,height=20)
    Label(estoque_consulta,text='Qtd cadastrada', background='red', foreground='black', anchor=W).place(x=1,y=240,width=100,height=20)
    Label(estoque_consulta,text='Qtd Saida', background='red', foreground='black', anchor=W).place(x=1,y=270,width=100,height=20)
    vnome=Entry  (estoque_consulta)


#Id_Produto 1
#Nome_Produto 2
#Status_Produto 3
#Status_de_Solicitacao 4
#Qualidade 5
#Data_de_Entrada 6
#Data_de_Saida 7
#Qtd_solicitada 8
#Qtd_cadastrada 9
#Qtd_Saida 10

    vnome.place(x=130,y=30, width=50,height=20) #  Id_Produto
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=60, width=200,height=20) # Nome_Produto
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=90, width=100,height=20)  # Status_Produto
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=120, width=50,height=20)  # Status_de_Solicitacao 
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=150, width=200,height=20)   #Qualidade
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=180, width=100,height=20)  # Data_de_Entrada
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=210, width=100,height=20)  # Data_de_Saida
    vnome=Entry      (estoque_consulta)   
    vnome.place(x=130,y=240, width=100,height=20)  # Qtd_solicitada
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=270, width=100,height=20)  # Qtd_cadastrada
    vnome=Entry      (estoque_consulta)
    vnome.place(x=130,y=180, width=100,height=20)  # Qtd_Saida
    vnome=Entry      (estoque_consulta)

    Button(estoque_consulta, text="BUSCAR",  command=impDados).place(x=310, y=300, width=100,height=20)


file_menu=Menu(menu_inicial, tearoff=0)
my_menu.add_cascade(label='Estoque', menu=file_menu)
file_menu.add_command(label='Consultar Estoque', command=consultarestoque) 

#ABA 1.2.2
def cadastrarestoque():
    estoque_cadastro =Tk()
    estoque_cadastro.title('Cadastrar Estoque')
    estoque_cadastro.geometry('700x200+250+400')
    estoque_cadastro.state('zoomed')
    estoque_cadastro.iconbitmap("img/icon.ico")
    estoque_cadastro['bg']='yellow'

    Label(estoque_cadastro,text='Id Produto', background='yellow', foreground='black', anchor=W).place(x=1,y=30,width=120,height=20)
    Label(estoque_cadastro,text='Nome Produto', background='yellow', foreground='black', anchor=W).place(x=1,y=60,width=100,height=20)
    Label(estoque_cadastro,text='Status Produto', background='yellow', foreground='black', anchor=W).place(x=1,y=90,width=105,height=20)
    Label(estoque_cadastro,text='Status de Solicitacao', background='yellow', foreground='black', anchor=W).place(x=1,y=120,width=120,height=20)
    Label(estoque_cadastro,text='Qualidade', background='yellow', foreground='black', anchor=W).place(x=1,y=150,width=100,height=20)
    Label(estoque_cadastro,text='Data de Saida ', background='yellow', foreground='black', anchor=W).place(x=1,y=180,width=105,height=20)
    Label(estoque_cadastro,text='Qtd solicitada ', background='yellow', foreground='black', anchor=W).place(x=1,y=210,width=120,height=20)
    Label(estoque_cadastro,text='Qtd cadastrada', background='yellow', foreground='black', anchor=W).place(x=1,y=240,width=100,height=20)
    Label(estoque_cadastro,text='Qtd Saida', background='yellow', foreground='black', anchor=W).place(x=1,y=270,width=100,height=20)
    vnome=Entry  (estoque_cadastro)
    vnome.place(x=130,y=30, width=50,height=20) #  Id_Produto
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=60, width=200,height=20) # Nome_Produto
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=90, width=100,height=20)  # Status_Produto
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=120, width=50,height=20)  # Status_de_Solicitacao 
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=150, width=200,height=20)   #Qualidade
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=180, width=100,height=20)  # Data_de_Entrada
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=210, width=100,height=20)  # Data_de_Saida
    vnome=Entry      (estoque_cadastro)   
    vnome.place(x=130,y=240, width=100,height=20)  # Qtd_solicitada
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=270, width=100,height=20)  # Qtd_cadastrada
    vnome=Entry      (estoque_cadastro)
    vnome.place(x=130,y=180, width=100,height=20)  # Qtd_Saida
    vnome=Entry      (estoque_cadastro)

    Button(estoque_cadastro, text="CADASTRAR",  command=impDados).place(x=310, y=300, width=100,height=20)


file_menu.add_command(label='Cadastrar Estoque', command=cadastrarestoque)

#
#
#
# ABA 2.1.1
def consultarproduto():
    produto_consulta=Tk()
    produto_consulta.title('Consultar Produtos')
    produto_consulta.geometry('700x200+250+400')
    produto_consulta.state('zoomed')
    produto_consulta.iconbitmap("img/icon.ico")
    produto_consulta['bg']='red'
    

    Label(produto_consulta,text='Id Produto', background='red', foreground='black', anchor=W).place(x=1,y=30,width=120,height=20)
    Label(produto_consulta,text='Quantidade em Estoque', background='red', foreground='black', anchor=W).place(x=1,y=60,width=100,height=20)
    Label(produto_consulta,text='Status do Produto', background='red', foreground='black', anchor=W).place(x=1,y=90,width=105,height=20)
    Label(produto_consulta,text='Data de Renovacao', background='red', foreground='black', anchor=W).place(x=1,y=120,width=100,height=20)
    Label(produto_consulta,text='Fornecedor', background='red', foreground='black', anchor=W).place(x=1,y=150,width=105,height=20)
    Label(produto_consulta,text='Fabricante', background='red', foreground='black', anchor=W).place(x=1,y=180,width=120,height=20)
    Label(produto_consulta,text='Lote', background='red', foreground='black', anchor=W).place(x=1,y=210,width=120,height=20)

    vnome=Entry  (produto_consulta)

#Id_produto
#Qtd_estoque
#Status_produto
#Data_renovacao
#Fornecedor
#Fabricante
#Lote

    vnome.place(x=130,y=30, width=50,height=20) #  Id_Produto
    vnome=Entry      (produto_consulta)
    vnome.place(x=130,y=60, width=200,height=20) # Qtd_estoque
    vnome=Entry      (produto_consulta)
    vnome.place(x=130,y=90, width=100,height=20)  # Status_Produto
    vnome=Entry      (produto_consulta)
    vnome.place(x=130,y=120, width=50,height=20)  # Data_renovacao 
    vnome=Entry      (produto_consulta)
    vnome.place(x=130,y=150, width=200,height=20)   #Fornecedor
    vnome=Entry      (produto_consulta)
    vnome.place(x=130,y=180, width=100,height=20)  # Fabricante
    vnome=Entry      (produto_consulta) 
    vnome.place(x=130,y=210, width=100,height=20)  # Lote
    vnome=Entry      (produto_consulta) 
    Button(produto_consulta, text="imprimir",  command=impDados).place(x=310, y=300, width=100,height=20)

file_menu=Menu(menu_inicial, tearoff=0)
my_menu.add_cascade(label='Produtos', menu=file_menu)
file_menu.add_command(label='Consultar Produtos', command=consultarproduto) 

#2.2.2

def cadastrarproduto():
    produto_cadastro =Tk()#2
    produto_cadastro.title('Cadastrar Produtos')
    produto_cadastro.geometry('700x200+250+400')
    produto_cadastro.state('zoomed')#abrir a app em tela cheia
    produto_cadastro.iconbitmap("img/icon.ico")#trabalhar com o icone
    produto_cadastro['bg']='yellow'

    Label(produto_cadastro,text='Id Produto', background='yellow', foreground='black', anchor=W).place(x=1,y=30,width=100,height=20)
    Label(produto_cadastro,text='Quantidade em Estoque', background='yellow', foreground='black', anchor=W).place(x=1,y=60,width=155,height=20)
    Label(produto_cadastro,text='Status do Produto', background='yellow', foreground='black', anchor=W).place(x=1,y=90,width=105,height=20)
    Label(produto_cadastro,text='Data de Renovacao', background='yellow', foreground='black', anchor=W).place(x=1,y=120,width=155,height=20)
    Label(produto_cadastro,text='Fornecedor', background='yellow', foreground='black', anchor=W).place(x=1,y=150,width=105,height=20)
    Label(produto_cadastro,text='Fabricante', background='yellow', foreground='black', anchor=W).place(x=1,y=180,width=120,height=20)
    Label(produto_cadastro,text='Lote', background='yellow', foreground='black', anchor=W).place(x=1,y=210,width=120,height=20)
    
    vnome=Entry  (produto_cadastro)
    vnome.place(x=135,y=30, width=50,height=20) #  Id_Produto
    vnome=Entry      (produto_cadastro)
    vnome.place(x=135,y=60, width=200,height=20) # Qtd_estoque
    vnome=Entry      (produto_cadastro)
    vnome.place(x=135,y=90, width=100,height=20)  # Status_Produto
    vnome=Entry      (produto_cadastro)
    vnome.place(x=135,y=120, width=50,height=20)  # Data_renovacao 
    vnome=Entry      (produto_cadastro)
    vnome.place(x=135,y=150, width=200,height=20)   #Fornecedor
    vnome=Entry      (produto_cadastro)
    vnome.place(x=135,y=180, width=100,height=20)  # Fabricante
    vnome=Entry      (produto_cadastro) 
    vnome.place(x=135,y=210, width=100,height=20)  # Lote
    vnome=Entry      (produto_cadastro) 

    Button(produto_cadastro, text="imprimir",  command=impDados).place(x=310, y=300, width=100,height=20)


file_menu.add_command(label='Cadastrar Produtos', command=cadastrarproduto)



def clientepesquisa():
    
    cliente_pesquisa=Tk()   #1.2/3
    cliente_pesquisa.title('Pesquisar Clientes')
    cliente_pesquisa.geometry('700x200+250+400')
    cliente_pesquisa.state('zoomed')#abrir a app em tela cheia
    cliente_pesquisa.iconbitmap("img/icon.ico")
    cliente_pesquisa['bg']='red'

    # 
    Label(cliente_pesquisa,text='Id do Cliente', background='red', foreground='black', anchor=W).place(x=1,y=20,width=105,height=20)
    Label(cliente_pesquisa,text='Nome do Cliente', background='red', foreground='black', anchor=W).place(x=1,y=60,width=120,height=20)
    Label(cliente_pesquisa,text='CPF/CNPJ', background='red', foreground='black', anchor=W).place(x=1,y=100,width=105,height=20)
    Label(cliente_pesquisa,text='Telefone', background='red', foreground='black', anchor=W).place(x=1,y=140,width=105,height=20)
    Label(cliente_pesquisa,text='Endereço', background='red', foreground='black', anchor=W).place(x=1,y=180,width=80,height=20)
    Label(cliente_pesquisa,text='Data da compra', background='red', foreground='black', anchor=W).place(x=1,y=220,width=120,height=20)
    Label(cliente_pesquisa,text='valor da compra', background='red', foreground='black', anchor=W).place(x=1,y=260,width=120,height=20)
    Label(cliente_pesquisa,text='Descrição do produto comprado', background='red', foreground='black', anchor=W).place(x=1,y=300,width=120,height=20)
    Label(cliente_pesquisa,text='Data de aniversário', background='red', foreground='black', anchor=W).place(x=1,y=340,width=120,height=20)
    Label(cliente_pesquisa,text='Data do Cadastro', background='red', foreground='black', anchor=W).place(x=1,y=380,width=120,height=20)



    #
    Label(cliente_pesquisa)
    vnome=Entry  (cliente_pesquisa)
    vnome.place(x=130,y=20, width=20,height=20)   
    
    vnome=Entry      (cliente_pesquisa)
    vnome.place(x=130,y=60, width=200,height=20)  
    vnome=Entry  (cliente_pesquisa)
    vnome.place(x=130,y=100, width=400,height=20) 
    
    vnome=Entry      (cliente_pesquisa)
    vnome.place(x=130,y=140, width=100,height=20) 

    vnome=Entry  (cliente_pesquisa)
    vnome.place(x=130,y=180, width=400,height=20)  
    
    vnome=Entry      (cliente_pesquisa)
    vnome.place(x=130,y=220, width=100,height=20)

    vnome=Entry      (cliente_pesquisa)
    vnome.place(x=130,y=260, width=100,height=20)

    vnome=Entry      (cliente_pesquisa)
    vnome.place(x=130,y=300, width=100,height=20)

    vnome=Entry      (cliente_pesquisa)
    vnome.place(x=130,y=340, width=100,height=20)

    vnome=Entry      (cliente_pesquisa)
    vnome.place(x=130,y=380, width=100,height=20) 


    Button(cliente_pesquisa, text="Buscar",  command=impDados).place(x=300, y=400, width=100,height=20)
    

file_menu=Menu(menu_inicial, tearoff=0)
my_menu.add_cascade(label='Clientes', menu=file_menu)
file_menu.add_command(label='Pesquisar clientes', command=clientepesquisa)  #3



def clientecadastrar(): #2.2/3
 cliente_cadastrar=Tk()
 cliente_cadastrar.title('Cadastrar Clientes')
 cliente_cadastrar.geometry('700x200+250+400')
 cliente_cadastrar.state('zoomed')
 cliente_cadastrar.iconbitmap("img/icon.ico")
 cliente_cadastrar['bg']='yellow'

 


#Idcliente
#Nome
#Telefone
#Endereco
#data_compra
#valor
#ProdComprado


 Label(cliente_cadastrar,text='Id do Cliente', background='yellow', foreground='black', anchor=W).place(x=1,y=20,width=105,height=20)
 Label(cliente_cadastrar,text='Nome do Cliente', background='yellow', foreground='black', anchor=W).place(x=1,y=60,width=120,height=20)
 Label(cliente_cadastrar,text='CPF/CNPJ', background='yellow', foreground='black', anchor=W).place(x=1,y=100,width=105,height=20)
 Label(cliente_cadastrar,text='Telefone', background='yellow', foreground='black', anchor=W).place(x=1,y=140,width=105,height=20)
 Label(cliente_cadastrar,text='Endereço', background='yellow', foreground='black', anchor=W).place(x=1,y=180,width=80,height=20)
 Label(cliente_cadastrar,text='Data da compra', background='yellow', foreground='black', anchor=W).place(x=1,y=220,width=120,height=20)
 Label(cliente_cadastrar,text='valor da compra', background='yellow', foreground='black', anchor=W).place(x=1,y=260,width=120,height=20)
 Label(cliente_cadastrar,text='Descrição do produto comprado', background='yellow', foreground='black', anchor=W).place(x=1,y=300,width=120,height=20)
 
#----   



 entIdcliente=Entry     (cliente_cadastrar)
 entIdcliente.place(x=130,y=20, width=100,height=20)
 
 
 entNome =Entry        (cliente_cadastrar)
 entNome.place(x=130,y=60, width=20,height=20)   
  
 entTel=Entry      (cliente_cadastrar)
 entTel.place(x=130,y=100, width=200,height=20)  
 
 entEnder=Entry  (cliente_cadastrar)
 entEnder.place(x=130,y=140, width=400,height=20) 
  
 entDataComp=Entry      (cliente_cadastrar)
 entDataComp.place(x=130,y=180, width=100,height=20) 
 
 entVal=Entry  (cliente_cadastrar)
 entVal.place(x=130,y=220, width=400,height=20)  
 entProdcomp=Entry      (cliente_cadastrar)
 entProdcomp.place(x=130,y=260, width=100,height=20)

 
import mysql.connector
banco = mysql.connector.connect(

host= "localhost",
user="root",
passwd="",
database="bancotcc",
charset='utf8',
)

cursor= banco.cursor()
def comecar():
 entIdcliente
 entNome
 entTel
 entEnder
 entDataComp
 entVal  
 entProdcomp
 

def insert():
    comando=f'INSERT INTO table cliente (Idcliente, Nome, Telefone, Endereco, data_compra, valor, ProdComprado) VALUES ({entIdcliente},{entNome},{entTel},{entEnder},{entDataComp},{entVal},{entProdcomp})'
cursor.execute(insert)

def inserir():
 query="INSERT INTO  table cliente(Idcliente, Nome, Telefone, Endereco, data_compra, valor, ProdComprad) values ('Igor', 942311567, 'af' '01/02/2021', 10, 'Macarrão')"
 cursor.execute(query)
 cursor.commit()

def buscar():
 query='SELECT * from table cliente'
 cursor.execute(query)
 cursor.commit()

 Button(cliente_cadastrar, text="Buscar",  command=impDados).place(x=300, y=400, width=100,height=20)


file_menu.add_command(label='Cadastrar Clientes', command=clientecadastrar)#2

#-----------------------

def pesquisarfornecedores():
    pesquisarfornecedor=Tk()   
    pesquisarfornecedor.title('Pesquisar Fornecedores')
    pesquisarfornecedor.geometry('700x200+250+400')
    pesquisarfornecedor.state('zoomed')
    pesquisarfornecedor.iconbitmap("img/icon.ico")
    pesquisarfornecedor['bg']='red'


    Label(pesquisarfornecedor,text='Id fornecedor', background='red', foreground='black', anchor=W).place(x=1,y=30,width=300,height=20)
    Label(pesquisarfornecedor,text='Nome fornecedor', background='red', foreground='black', anchor=W).place(x=300,y=30,width=300,height=20)
    Label(pesquisarfornecedor,text='CPF/CNPJ fornecedor', background='red', foreground='black', anchor=W).place(x=1,y=60,width=300,height=20)
    Label(pesquisarfornecedor,text='Qualidade do fornecedor', background='red', foreground='black', anchor=W).place(x=300,y=60,width=300,height=20)
    Label(pesquisarfornecedor,text='Id entregador', background='red', foreground='black', anchor=W).place(x=1,y=90,width=300,height=20)
    Label(pesquisarfornecedor,text='Nome entregador', background='red', foreground='black', anchor=W).place(x=300,y=90,width=300,height=20)
    Label(pesquisarfornecedor,text='CPF/CNPJ entregador', background='red', foreground='black', anchor=W).place(x=1,y=120,width=300,height=20)#
    Label(pesquisarfornecedor,text='Qualidade do entegador', background='red', foreground='black', anchor=W).place(x=300,y=120,width=300,height=20)
    Label(pesquisarfornecedor,text='Status de entrega', background='red', foreground='black', anchor=W).place(x=1,y=150,width=300,height=20)    
    Label(pesquisarfornecedor,text='Data do pedido', background='red', foreground='black', anchor=W).place(x=300,y=150,width=300,height=20)
    Label(pesquisarfornecedor,text='Data da entrega', background='red', foreground='black', anchor=W).place(x=1,y=180,width=300,height=20)
    Label(pesquisarfornecedor,text='Quantidade solicida', background='red', foreground='black', anchor=W).place(x=300,y=180,width=300,height=20)
    Label(pesquisarfornecedor,text='Quantidade entregue', background='red',foreground='black', anchor=W).place(x=1,y=210,width=300,height=20)
    Label(pesquisarfornecedor,text='Fabricante', background='red', foreground='black', anchor=W).place(x=300,y=210,width=300,height=20)

    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=130,y=30, width=60,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=130,y=60, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=130,y=90, width=60,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=130,y=120, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=130,y=150, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=130,y=180, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=130,y=210, width=120,height=20)#
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=450,y=30, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=450,y=60, width=120,height=20)#
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=450,y=90, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=450,y=120, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=450,y=150, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=450,y=180, width=120,height=20)
    vnome=Entry  (pesquisarfornecedor)
    vnome.place(x=450,y=210, width=120,height=20)
                                                  # Y = ALTURA LATERAL X POSICIONAMENTO HORIZONTAL
    Button(pesquisarfornecedor, text="BUSCAR",  command=impDados).place(x=600, y=270, width=100,height=20)

   


file_menu=Menu(menu_inicial, tearoff=0)
my_menu.add_cascade(label='Fornecedores', menu=file_menu)
file_menu.add_command(label='Pesquisar fornecedores', command=pesquisarfornecedores)  #1
                              
def cadastrarfornecedores():
 cadastrarfornecedor =Tk()
 cadastrarfornecedor.title('Cadastrar Fornecedores')
 cadastrarfornecedor.geometry('700x200+250+400')
 cadastrarfornecedor.state('zoomed')
 cadastrarfornecedor.iconbitmap("img/icon.ico")#trabalhar com o icone
 cadastrarfornecedor['bg']='yellow'
                             
def fornecedorcadastro():
 fornecedor_cadastro =Tk()
 fornecedor_cadastro.title('Cadastrar Fornecedores')
 fornecedor_cadastro.geometry('700x200+250+400')
 fornecedor_cadastro.state('zoomed')
 fornecedor_cadastro.iconbitmap("img/icon.ico")#trabalhar com o icone
 fornecedor_cadastro['bg']='yellow'
      
 Label(fornecedor_cadastro,text='Id fornecedor', background='yellow', foreground='black', anchor=W).place(x=1,y=30,width=300,height=20)
 Label(fornecedor_cadastro,text='Nome fornecedor', background='yellow', foreground='black', anchor=W).place(x=300,y=30,width=300,height=20)
 Label(fornecedor_cadastro,text='CPF/CNPJ fornecedor', background='yellow', foreground='black', anchor=W).place(x=1,y=60,width=300,height=20)
 Label(fornecedor_cadastro,text='Qualidade do fornecedor', background='yellow', foreground='black', anchor=W).place(x=300,y=60,width=300,height=20)
 Label(fornecedor_cadastro,text='Id entregador', background='yellow', foreground='black', anchor=W).place(x=1,y=90,width=300,height=20)
 Label(fornecedor_cadastro,text='Nome entregador', background='yellow', foreground='black', anchor=W).place(x=300,y=90,width=300,height=20)
 Label(fornecedor_cadastro,text='CPF/CNPJ entregador', background='yellow', foreground='black', anchor=W).place(x=1,y=120,width=300,height=20)#
 Label(fornecedor_cadastro,text='Qualidade do entegador', background='yellow', foreground='black', anchor=W).place(x=300,y=120,width=300,height=20)
 Label(fornecedor_cadastro,text='Status de entrega', background='yellow', foreground='black', anchor=W).place(x=1,y=150,width=300,height=20)    
 Label(fornecedor_cadastro,text='Data do pedido', background='yellow', foreground='black', anchor=W).place(x=300,y=150,width=300,height=20)
 Label(fornecedor_cadastro,text='Data da entrega', background='yellow', foreground='black', anchor=W).place(x=1,y=180,width=300,height=20)
 Label(fornecedor_cadastro,text='Quantidade solicida', background='yellow', foreground='black', anchor=W).place(x=300,y=180,width=300,height=20)
 Label(fornecedor_cadastro,text='Quantidade entregue', background='yellow',foreground='black', anchor=W).place(x=1,y=210,width=300,height=20)
 Label(fornecedor_cadastro,text='Fabricante', background='yellow', foreground='black', anchor=W).place(x=300,y=210,width=300,height=20)
 
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=130,y=30, width=60,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=130,y=60, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=130,y=90, width=60,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=130,y=120, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=130,y=150, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=130,y=180, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=130,y=210, width=120,height=20)#
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=450,y=30, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=450,y=60, width=120,height=20)#
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=450,y=90, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=450,y=120, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=450,y=150, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=450,y=180, width=120,height=20)
 vnome=Entry  (fornecedor_cadastro)
 vnome.place(x=450,y=210, width=120,height=20)
                                               # Y = ALTURA LATERAL X POSICIONAMENTO HORIZONTAL
 Button(fornecedor_cadastro, text="CADASTRAR",  command=impDados).place(x=1, y=600, width=100,height=20)
 Button(fornecedor_cadastro, text="CANCELAR",  command=impDados).place(x=200, y=600, width=100,height=20)
 Button(fornecedor_cadastro, text="EXLUIR",  command=impDados).place(x=400, y=600, width=100,height=20)


file_menu.add_command(label='Cadastrar Fornecedores', command=fornecedorcadastro)#2




def suportes():
     suporte=Tk()  
     suporte.title('Suporte Seraphine Database')
     suporte.geometry('700x200+250+400')
     suporte.state('zoomed')#abrir a app em tela cheia
     suporte.iconbitmap("img/icon.ico")#trabalhar com o icone
     suporte['bg']='red'


file_menu=Menu(menu_inicial, tearoff=0)
my_menu.add_cascade(label='Suporte', menu=file_menu)
file_menu.add_command(label='(11) 94231-1567', command=suportes)  #1



menu_inicial.mainloop()