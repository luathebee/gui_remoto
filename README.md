# gui_remoto
Interface gráfica para acessar opções de acesso remoto previamente configuradas

### Acesso ao Windows
	Inicia o remmina com o arquivo RDP com os parametros de acesso remoto ao terminal acadêmico da UFSC. 
	Solicita nome de usuário e senha do IdUFSC.
	
### Acesso ao Linux
	Inicia uma sessão do X2Go definida no arquivo "sessions". Solicita usuário e senha para o acesso remoto.
	Opção de SSH Login permite o uso das credenciais do usuário cliente no login do anfitrião automáticamente. Testar implementação.
	


### Problemas
	1. Programa trava com o de uma das opções (busy waiting). Threads podem resolver
	
	2. Se implementear Threads, criar uma trava que impeça que o programa seja chamado duas vezes.
