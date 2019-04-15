Trabalho Pŕatico de Redes 2019.1 
ALuno: Yohana de Carvalho Horta 


O primeiro trabalho prático consiste em desenvolver um seridor cliente do tipo HTTP.

A ideia do programa é transferir dados de um lugar para outro. Ou seja, o cliente vai solicitar uma requisição para o servidor (baixar um arquivo) e o servidor irá mandar o arquivo caso ele exista ou uma mensagem falando que ele não existe. 

Este trabalho também deixa vários clientes conectarem ao mesmo tempo. Para tal foi utilizado thread para esse desenvolvimento.

Outro quesito que foi utilizado é o argv para passagem de parâmetros pelo terminal e caso o cliente não passe a porta, a porta padrão será a 80.


---- SERVIDOR:

O servidor foi desenvolvido da seguinte forma:

	- Função 'conectado' que contém o que vai ser executado para cada conexão de cliente:
		- Primeiramente um loop que fica recebendo e enviando mensagens entre o cliente e o servidor
		- Procura o nome do arquivo repartindo a mensagem
		- Procura o arquivo e tenta abrir lendo em bytes
			Caso ele exista, envia o conteúdo e fecha o arquivo lido
				- Se o cliente passar apenas a barra será enviado o arquivo raíz. Então, será passado o index.html ou index.php dependendo de qual exista.
			Caso ele não exista, manda uma mensagem falando que o arquivo não foi encontrado
		- 
		- Fecha conexão com o cliente 


Primeiramente inicia a conexão TCP/IP utlizando socket e depois fica "escutando". Ou seja, fica aceitando conexão e cada vez que o cliente conecta ele roda a função conectado para este cliente. 


---- CLIENTE:

Inicialmente ele faz também a conexão TCP/IP com o servidor 

Criação da comunicação entre o servidor e cliente
	- Divide o método e o nome do arquivo
	- Define o método e envia a requisição 
		- O método utilizado neste trabalho está sendo apenas o get
	- Recebe a resposta do servidor 
	- Trata os arquivos dentro de pastas 
		- Caso um arquivo solicitado não esteja no public e sim dentro de uma pasta é tratado para que consiga pegar este arquivo. 
			- Esse tratamento é feito quebrando o nome do arquivo requisito pelas barras. 
			- Posteriormente é dividido pelo ponto. Onde coleta o nome e a extensão do arquivo.

	- Cópia o que foi recebido para dentro de um novo arquivo que será criado na pasta do cliente e depois fecha o arquivo. 

