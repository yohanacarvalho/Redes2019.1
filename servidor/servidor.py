# coding=utf-8
import socket
import thread
import sys

HOST = ''              		#Endereco IP do Servidor

raiz = sys.argv[1]
if raiz == '/':
	raiz = ''

if len(sys.argv) < 3:
    PORT = 80
else:
	PORT = int(sys.argv[2])     #Porta que o Servidor esta


#Função que contém o que vai ser executado para cada conexão de cliente
def conectado(conexao, cliente):
    
    print 'Conectado por', cliente

    #Loop que fica recebendo e enviando mensagens entre o cliente e o servidor
    while True:
        requisicao = conexao.recv(1000000000)
        if not requisicao: break
        
        #Os dois procuram o nome do arquivo
        requisicao = requisicao.split(' ')
        requisicao = requisicao[1].split(' ')

        print 'Arquivo solicitado: '+requisicao[0]
        #Tenta abrir o Arquivo
        try:
        	if requisicao[0] == '/':
        		arquivo = open(raiz+'index.html', 'rb')	
        	else:
        		arquivo = open(raiz+requisicao[0], 'rb')
        	print 'arquivo encontrado'        	
        	conteudo = arquivo.read()

        	conexao.send(conteudo) 
        	arquivo.close()    

        except IOError:
        	print '404 - Arquivo Não Encontrado'
        	conexao.send('0')

        print cliente, requisicao

    print 'Finalizando Conexão do Cliente', cliente
    conexao.close()
    thread.exit()

#Inicia a conexão do tipo tcp/ip
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig) #Faz conexão...
tcp.listen(1)  #Fica ouvindo...

#Fica aceitando conexão e cada vez que o cliente conecta ele roda a função conectado para este cliente
while True:
    conexao, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([conexao, cliente]))

tcp.close()