# Dashboard utilizando o streamlit, pandas e plotly

Esse Dashboard consiste em um projeto universitário na qual visa análisar as rotinas e os cuidados que as pessoas tem em relação a sua saúde bucal em geral e propor uma visão geral das pesquisas

# Todos os comandos serão feito pelo Terminal da IDE (VS CODE)

# 1º Passo
Criar uma PASTA <br /> 

- mkdir "nome da pasta" <br />

Vamos utilizar essa PASTA <br />

- cd "nome da pasta" <br />

Obs: Após criar a pasta, importe o banco de dados em extensão xlsx (Planilha Excell) e o arquivo em python (dash.py) para dentro da pasta que você criou

# 2ª Passo
Vamos criar uma máquina virtual venv <br />
No terminal vamos instalar o virtualenv <br />

- pip install virtualenv <br />

Vamos dar nome a nossa máquina virtual <br />

- python -m venv venv <br />

Obs: Esse ultimo nome --"venv"-- você pode chama-ló de qualquer coisa, normalmente os desenvolvedores dão o nome de "venv" ou "env" <br />
Dentro da sua pasta (você pode visualiza-ló a esquerda no canto superior da sua IDE) irá aparecer o ambiente criando <br />

Agora vamos ativa-lo

- .\nome da sua máqina virtual (venv ou env)\Sripts\Activate.ps1

# 3ª Passo
Vamos instalar as ferramentas necessárias para o nosso dashboard <br />

- pip install streamlit <br />
- pip install plotly <br />
- pip install pandas <br />
- pip install xlrd
- pip install openpyxl

Obs: Os dois últimos import é pra lê e abrir o arquivo Excell em formato xlsx

# 4º Passo
Vamos acessar nosso dashboard pelo terminal <br />
- streamlit run dash.py <br />

Irá pedir seu email

Logo após o sreamlit vai lhe fornecer duas URL e abrirá no navegador padrão da Microsoft, é só fechar pois não aparecerá nada <br />
Copie e cole uma das URL no seu navegador padrão (Google, firefox, Safari etc)
