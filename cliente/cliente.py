# coding=utf-8
import sys
import socket

HOST = sys.argv[1]          #Endereco IP do Servidor

if len(sys.argv) < 3:
    PORT = 80
else:
    PORT = int(sys.argv[2])     #Porta que o Servidor esta


#Inicia conexão tcp/ip com o servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

#Comunicação entre o servidor cliente
while 1:
    requisicao = raw_input()    

    #Divide o método e o nome do arquivo
    requisicao_dividida = requisicao.split(' ') 
    metodo = requisicao_dividida[0]
    arquivo_solicitado = requisicao_dividida[1]

    #Define o método e envia a requisição
    if metodo == 'GET' or metodo == 'get':
      tcp.send ('GET '+arquivo_solicitado+' HTTP/1.1\r\nHOST: '+HOST+'\r\n\r\n')

    #Recebe a resposta do servidor 
    resp = tcp.recv(1000000000)
    if resp == '0':
      print 'Arquivo Não Encontrado'
      break

    print 'Arquivo Encontrado'

    #Trata os arquivos dentro de pastas
    numero = arquivo_solicitado.count('/')      
    arquivo_solicitado = arquivo_solicitado.split('/')

    #Pega a extensão do arquivo
    nome_arquivo = arquivo_solicitado[numero].split('.') 

    #Cópia o que foi recebido para dentro de um novo arquivo que será criado na pasta do cliente
    novo_arquivo = open(nome_arquivo[0]+'-copia.'+nome_arquivo[1], 'wb')
    novo_arquivo.write(resp);  
    novo_arquivo.close(); 

tcp.close()